#Test04 : 파일쓰기

#파일이 없는 경우, 생성 후 쓰기
f = open('test.txt', 'w')

for i in range(1, 6) :
  data = "{} 번째 줄입니다 \n".format(i)
  f.write(data)

f.close()

#파일이 있는 경우, 이어 쓰기
f = open('test.txt', 'a')

for i in range(6, 11) :
  data = "{} 번째 줄입니다 \n".format(i)
  f.write(data)

f.close()