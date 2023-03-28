#Test01 : 제어문
import random

a = 0
b = 0
c = 0
cnt = 0

while (1) :
    print("주사위를 던지자!")
    a = random.randint(1, 6);
    b = random.randint(1, 6);
    c = random.randint(1, 6);
    cnt = cnt + 1
    print(a, ",", b, ",", c)
    if (a == b and b == c) :
      break ;
    print("땡! 다시~\n")
print("빙고!: 던진 횟수 : ", cnt)
