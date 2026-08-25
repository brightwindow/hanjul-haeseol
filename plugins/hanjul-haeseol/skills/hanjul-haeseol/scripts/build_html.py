# -*- coding: utf-8 -*-
"""쪽별 해설 조각(JSON)을 한 벌의 해설 HTML 로 조립한다.

    python build_html.py <fragments.json> <출력.html> [문서제목]

fragments.json 은 아래 모양의 배열이다. 쪽 번호 순서는 알아서 정렬한다.

    [
      {"page": 1, "title": "표지", "html": "<div class=\\"row\\">...</div>"},
      {"page": 2, "title": "Overview — 전체 지도", "html": "..."}
    ]

html 칸에 쓸 수 있는 마크업은 다섯 가지뿐이다.

    <div class="row"><div class="orig">원문</div><div class="exp">해설</div></div>
    <span class="hand">[필기] ...</span>        원문 칸 안에서 손글씨
    <div class="fig">이 그림은 ...</div>         그래프·그림 설명
    <div class="exam">★ 시험 포인트 — ...</div>  붉은 강조가 있던 곳만
    <div class="key">정리 ...</div>              배경·요약
    <h3>소제목</h3>                              쪽 안에서 갈래를 나눌 때

h1·h2·section 은 쓰지 않는다. 조립할 때 자동으로 붙는다.
"""
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
CSS_PATH = os.path.join(HERE, '..', 'references', 'style.css')

INTRO = ('고등학교 수학(<b>미분 = 변화의 빠르기</b>)만 알면 읽히도록 풀었다. '
         '전문 용어는 나올 때마다 일상어로 다시 설명한다. '
         '원문에 있는 줄은 손글씨까지 하나도 빠뜨리지 않았다.')

LEGEND = ('<div class="legend">'
          '<span><i class="chip c1"></i>원문</span>'
          '<span><i class="chip c2"></i>손글씨 필기</span>'
          '<span><i class="chip c3"></i>시험 포인트</span>'
          '<span><i class="chip c4"></i>정리 · 배경</span></div>')


def load_css():
    """서식을 읽어 온다. 스킬 폴더 안에서 부르는 것이 정상이다."""
    if os.path.exists(CSS_PATH):
        return io.open(CSS_PATH, encoding='utf-8').read()
    sys.exit('style.css 를 못 찾음: %s' % CSS_PATH)


def check(frags):
    """조립 전에 흔한 사고를 걸러 낸다."""
    warn = []
    pages = [f['page'] for f in frags]
    if len(pages) != len(set(pages)):
        warn.append('쪽 번호가 겹침')
    gap = [p for p in range(min(pages), max(pages) + 1) if p not in pages]
    if gap:
        warn.append('빠진 쪽 %s' % ', '.join(str(p) for p in gap))
    for f in frags:
        h = f['html']
        for tag in ('div', 'span', 'h3'):
            o = len(re.findall(r'<%s[ >]' % tag, h))
            c = len(re.findall(r'</%s>' % tag, h))
            if o != c:
                warn.append('%d쪽 <%s> 태그 짝이 안 맞음 (%d/%d)' % (f['page'], tag, o, c))
        if re.search(r'<(h1|h2|section)[ >]', h):
            warn.append('%d쪽 에 h1/h2/section 이 있음. h3 만 쓸 것' % f['page'])
    return warn


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    src, out = sys.argv[1], sys.argv[2]
    title = sys.argv[3] if len(sys.argv) > 3 else '한 줄 해설'

    frags = json.load(io.open(src, encoding='utf-8'))
    frags = sorted(frags, key=lambda f: f['page'])

    for w in check(frags):
        print('  경고 : %s' % w)

    toc = ''.join('<a href="#s%d">%d쪽 · %s</a>'
                  % (f['page'], f['page'], f['title'].split('—')[0].strip())
                  for f in frags)
    body = []
    for f in frags:
        body.append('<h2 id="s%d">%d쪽<small>%s</small></h2>' % (f['page'], f['page'], f['title']))
        body.append(f['html'])

    doc = ('<!DOCTYPE html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n'
           '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
           '<title>%s</title>\n<style>%s</style>\n</head>\n<body>\n'
           '<div class="wrap" id="top">\n<h1>%s</h1>\n'
           '<div class="intro">%s</div>\n%s\n'
           '<div class="toc"><b>목차</b>%s</div>\n%s\n'
           '<a class="top" href="#top">맨 위로</a>\n</div>\n</body>\n</html>\n'
           % (title, load_css(), title, INTRO, LEGEND, toc, '\n'.join(body)))

    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    io.open(out, 'w', encoding='utf-8').write(doc)

    print()
    print('저장 : %s' % out)
    print('쪽 %d · 해설 줄 %d · 시험포인트 %d · 필기 %d · 그림설명 %d · %.0f KB'
          % (len(frags), doc.count('class="row"'), doc.count('class="exam"'),
             doc.count('class="hand"'), doc.count('class="fig"'),
             len(doc.encode('utf-8')) / 1024))


if __name__ == '__main__':
    main()
