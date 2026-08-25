# 실제 결과 예시

부산대 반도체공학 Ch.6 슬라이드에 돌린 결과에서 **세 종류의 쪽**을 뽑았다.
새 과목을 시작할 때 이 문서를 먼저 읽고 **밀도와 어조를 맞춘다.**

---

## 예시 A — 인쇄된 본문이 대부분인 쪽

전형적인 강의 슬라이드다. 원문 한 줄에 해설 한 덩어리씩 붙인다.

```html
<div class="row">
  <div class="orig">Carrier concentration in thermal equilibrium: the concentration of electrons (n₀) and holes (p₀) are <u>independent of time</u></div>
  <div class="exp">열평형에서 전자 농도 n<sub>0</sub>와 정공 농도 p<sub>0</sub>는 <b>시간과 무관하다</b>. 1초 뒤에 재도, 한 시간 뒤에 재도 같은 값이 나온다는 뜻이다. 아래 첨자 0이 붙으면 "평형값"이라는 약속이다.</div>
</div>

<div class="row">
  <div class="orig">Generation and recombination <u>are still happening</u> in thermal equilibrium</div>
  <div class="exp">여기가 헷갈리기 쉬운 곳이다. 농도가 안 변한다고 해서 <b>아무 일도 안 일어나는 것이 아니다</b>. 생성과 재결합은 계속 일어나고 있고 단지 속도가 같을 뿐이다.<br>수도꼭지와 배수구가 똑같은 속도로 열려 있는 욕조와 같다. 수위는 그대로지만 물은 계속 흐른다.</div>
</div>

<div class="row">
  <div class="orig">G<sub>n0</sub> = G<sub>p0</sub>,  R<sub>n0</sub> = R<sub>p0</sub>  (#/cm³·s)</div>
  <div class="exp">단위부터 보면 뜻이 분명해진다. <b>#/cm³·s</b> = <b>1 cm³ 안에서 1초에 몇 개</b>. 그래서 이 값들은 "속도"다.<br>전자와 정공은 항상 <b>쌍으로</b> 생기고 <b>쌍으로</b> 사라지므로 전자 쪽 수치와 정공 쪽 수치가 같다.</div>
</div>

<div class="fig"><b>오른쪽 그림 (Direct band-to-band generation and recombination)</b> — 왼쪽 화살표는 아래(E<sub>v</sub>)에서 위(E<sub>c</sub>)로 올라가는 <b>생성</b>, 오른쪽 화살표는 위에서 아래로 떨어지는 <b>재결합</b>이다. 가운데 필기 <span class="hand">G = R</span>이 이 그림의 결론이다.</div>
```

**여기서 볼 것**

- 단위(`#/cm³·s`)를 먼저 읽어 주면 그 값이 무엇인지가 저절로 드러난다.
- "헷갈리기 쉬운 곳이다" 처럼 **어디서 막히는지 짚어 준다.**
- 비유(욕조)를 쓰고 **바로 정확한 서술로 돌아온다.**
- 그림은 화살표 방향까지 읽어 준다. 그림을 못 보는 상태로 읽는 사람이 있다.

---

## 예시 B — 전부 손글씨인 쪽

**가장 값진 쪽**이다. 대개 그 과목의 한 장 요약이라서 시험 직전에 이 쪽만 봐도 된다.
손으로 전개한 계산은 **한 줄씩 끊어서** 따라간다.

```html
<p class="fig">이 쪽은 인쇄된 글자가 하나도 없고 전부 교수님 손글씨다. <b>6장 전체를 한 장으로 그린 지도</b>라서 시험 직전에 이 쪽만 봐도 흐름이 잡힌다.</p>

<div class="row">
  <div class="orig"><span class="hand">[필기] dn(t)/dt = d/dt (n₀ + δn(t)) = d(δn)/dt = g' − R</span></div>
  <div class="exp"><span class="eq">d/dt</span>는 <b>시간에 따라 얼마나 빨리 변하는가</b>, 즉 변화 속도를 뜻한다. 그래프의 기울기다.<br>n<sub>0</sub>는 상수라서 미분하면 0이 된다. 그래서 <b>전체 전자의 변화 속도 = 초과분 δn의 변화 속도</b>가 된다.<br>오른쪽 <span class="eq">g' − R</span>은 "새로 생기는 속도 빼기 없어지는 속도"다. 수도꼭지로 물이 들어오고 배수구로 빠지는 욕조를 떠올리면 된다.</div>
</div>

<div class="row">
  <div class="orig"><span class="hand">[필기] = α{nᵢ² − (n₀+δn)(p₀+δp)}</span></div>
  <div class="exp">n과 p 자리에 각각 n<sub>0</sub>+δn, p<sub>0</sub>+δp를 넣었다. 이제 괄호를 전개하면 된다.</div>
</div>

<div class="row">
  <div class="orig"><span class="hand">[필기] = −α δn · p₀</span></div>
  <div class="exp">여기서 저준위 주입 조건이 일한다.<br>① p형이므로 <span class="eq">p<sub>0</sub> ≫ n<sub>0</sub></span> → 괄호 안 n<sub>0</sub>는 무시.<br>② <span class="eq">p<sub>0</sub> ≫ δn</span> → (δn)²은 더 작으니 무시.<br>큰 것만 남기고 작은 것을 버리는 <b>근사</b>이며, 이 과목에서 계속 쓰는 기술이다.</div>
</div>

<div class="key"><b>이 쪽 한 줄 요약</b> — 빛을 끄면 초과 캐리어는 <span class="eq">δn(t) = δn(0)·e<sup>−t/τ</sup></span> 로 사라진다. τ는 <b>수명</b>이고 <span class="eq">τ = 1/(α p<sub>0</sub>)</span>, 즉 <b>다수 캐리어가 많을수록 초과분이 빨리 죽는다</b>.</div>
```

**여기서 볼 것**

- 쪽 첫머리에 `<p class="fig">` 로 **이 쪽이 어떤 성격인지** 먼저 알려 준다.
- 손 계산은 **줄마다 따로** 잡는다. 한 덩어리로 묶으면 어디서 뭘 버렸는지 안 보인다.
- **근사를 쓸 때 무엇을 왜 버렸는지** 번호를 매겨 밝힌다. 이 과목들에서 가장 자주 나오는 기술이다.
- 쪽 끝에 `key` 상자로 한 줄 요약을 남긴다.

---

## 예시 C — 붉은 강조가 있는 쪽

교수가 동그라미 친 자리는 **그대로 시험 포인트**다. 표시가 있던 자리만 쓴다.

```html
<div class="row">
  <div class="orig"><span class="hand">[필기] R'<sub>n</sub> (동그라미)</span> = −d(δn(t))/dt = +α<sub>r</sub>p₀δn(t) <span class="hand">= δn(t)/τ<sub>n0</sub> (동그라미)</span></div>
  <div class="exp">재결합률은 <b>양수로 정의</b>한다. 그래서 앞에 마이너스를 붙여 부호를 뒤집었다.<br>동그라미 친 <span class="eq">R' = δn/τ</span>가 <b>이 쪽에서 가장 중요한 결과</b>다. <b>초과분을 수명으로 나누면 재결합 속도가 된다</b>는 뜻이고, 뒤의 모든 방정식에서 이 형태로 등장한다.</div>
</div>

<div class="exam"><b>★ 시험 포인트</b> — 이 쪽에 붉은 표시가 가장 많다. 반드시 챙길 세 가지다.<br>
① <span class="eq">δn(t) = δn(0)e<sup>−t/τ</sup></span> — 초과 캐리어는 지수함수로 죽는다<br>
② <span class="eq">τ<sub>n0</sub> = (α<sub>r</sub>p<sub>0</sub>)<sup>−1</sup></span> — 수명의 정의<br>
③ <span class="eq">R' = δn/τ</span> — 재결합률. 뒤의 모든 식에 이 꼴로 들어간다</div>
```

**여기서 볼 것**

- 손글씨 표시를 `(동그라미)` 처럼 **어떤 표시였는지까지** 적는다.
- 시험 포인트에는 **왜 그 표시가 중요한지**를 쓴다. "중요하다"만 쓰면 아무 도움이 안 된다.
- 항목이 여럿이면 번호를 매기고 **각 항목이 어디에 쓰이는지** 덧붙인다.

---

## 밀도 기준

| 쪽 성격 | 해설 줄 수 |
|---|---|
| 인쇄된 본문 위주 | 5 ~ 10 |
| 전부 손글씨인 요약 쪽 | 10 ~ 15 |
| 예제 풀이 쪽 | 8 ~ 12 |

슬라이드 18 쪽이면 해설 줄 120 개 안팎, 완성본 80 KB 정도가 나온다.
이보다 훨씬 적으면 원문을 요약해 버린 것이므로 다시 본다.
