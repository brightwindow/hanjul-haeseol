# -*- coding: utf-8 -*-
"""강의 슬라이드 PDF 를 쪽마다 PNG 와 TXT 로 뜯어낸다.

    python pdf_pages.py <입력.pdf> <작업폴더> [dpi]

PyMuPDF(fitz) 만 쓴다. pdftoppm 이 없는 환경에서도 돌아간다.
fitz 가 없다고 나오면 Anaconda 쪽 파이썬으로 부른다.
    C:/Users/Administrator/anaconda3/python pdf_pages.py ...
"""
import io
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

try:
    import fitz
except ImportError:
    sys.exit('fitz(PyMuPDF) 가 없음. Anaconda 파이썬으로 다시 부를 것.\n'
             '  예) C:/Users/Administrator/anaconda3/python ' + sys.argv[0] + ' ...')

if len(sys.argv) < 3:
    sys.exit('사용법: python pdf_pages.py <입력.pdf> <작업폴더> [dpi]')

src = sys.argv[1]
out = sys.argv[2]
dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 140

os.makedirs(out, exist_ok=True)
doc = fitz.open(src)

print('원본 : %s' % os.path.basename(src))
print('쪽수 : %d' % doc.page_count)
print()

hand = []                                        # 손글씨가 섞였을 법한 쪽을 표시해 둠
for i, page in enumerate(doc, 1):
    page.get_pixmap(dpi=dpi).save(os.path.join(out, 'p%02d.png' % i))
    t = page.get_text().strip()
    io.open(os.path.join(out, 'p%02d.txt' % i), 'w', encoding='utf-8').write(t)

    # 추출 텍스트가 유난히 짧거나 깨진 조각이 많으면 손글씨 쪽일 가능성이 큼
    frag = sum(1 for w in t.split() if len(w) <= 2)
    flag = ''
    if len(t) < 200 or (t and frag / max(1, len(t.split())) > 0.45):
        hand.append(i)
        flag = '   <- 손글씨 쪽으로 보임. 이미지를 특히 꼼꼼히 볼 것'
    print('  p%02d.png / p%02d.txt   추출 %4d자%s' % (i, i, len(t), flag))

print()
print('작업폴더 : %s' % out)
print('다음 할 일 : p01.png 부터 마지막 쪽까지 Read 도구로 전부 눈으로 볼 것.')
if hand:
    print('특히 이 쪽들은 텍스트 추출이 거의 쓸모없음 : %s'
          % ', '.join('%d쪽' % x for x in hand))
