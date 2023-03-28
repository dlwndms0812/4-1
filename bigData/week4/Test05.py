#Test05 : 파일읽기

#파일에서 한 줄 씩 읽기
f = open('test.txt', 'r')

line = f.readline()
print(line)

while True :
  line = f.readline()
  if not line :
    break
  print(line)

f.close()

#파일에서 여러 줄 읽기
f = open('test.txt', 'r')
lines = f.readlines()
print(lines)

print(type(lines))

for line in lines :
  print(line)

f.close()

#파일 전체 읽기
f = open('test.txt', 'r')

data = f.read()
print(type(data))

print(data)

f.close()