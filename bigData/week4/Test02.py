#Test02 : 리스트

import time
import random

food = ['피자', '치킨', '스테이크', '된장찌개', '바나나', '파스타', '감자튀김']

print(food)
print("점심 메뉴를 추천해 드립니다.")

print("추천 음식은 바로바로 -->", end = ' ')
time.sleep(1)
print(food[random.randint(0, len(food)-1)])

print()
food.sort()
print(food)

x = input("추가하고 싶은 음식이 있습니까? y/n ")
print()

if (x == 'y') :
  while(1) :
    n = input("음식이름(그만 추가하려면 q): ")
    if (n == 'q') :
      break
    if (n in food) :
      print("이미 추가된 음식입니다.")
    else :
      food.append(n)

print()
print(food)
x = input("찾는 음식은? ")
if (x in food) :
  print(food.index(x)+1, "번째 있습니다.")
else :
  print("찾는 음식이 없습니다.")
