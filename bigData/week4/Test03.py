#Test03 : 사용자 정의 함수

import random

def lottoFunc() :
  return random.randint(1, 45)

print("로또 추첨을 시작합니다!!")
lotto = list()

while (1) :
  if (len(lotto) == 6) :
    break 
  x = lottoFunc()
  if (x in lotto) :
    continue
  lotto.append(x)

lotto.sort()
print("이번 로또 번호 --> ", end = '')
for i in range(6) :
  print(lotto[i], " ", end = '')
