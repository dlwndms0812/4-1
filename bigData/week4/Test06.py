#Test06 : csv 파일 읽기

import csv

f = open('card.csv', encoding='UTF8') #1단계: 파일 오픈
data = csv.reader(f) #2단계: 파일 데이터 읽기
next(data) #3단계: 헤더 제거 - 한 행 건너띄고 다음 행부터 읽기 
data = list(data) #4단계: 읽어들인 데이터를 리스트로 변환

print("1. 레코드의 타입 확인")
print(type(data))

print("2. 'card.csv'의 레코드 개수")
print(len(data))

print("3. 첫 번째 이용내역 출력")
print(data[0])

print("4. 처음부터 세 번째 이용내역까지 출력")
print(data[:3])

print("5. 이용일시, 가맹점명, 금액 세 항목을 출력")
for row in data :
  print(row[0], row[5], row[6])

print("6. 2019년 12월 사용 금액의 합")
sum = 0
for row in data :
  date = row[0]
  month = date.split('-')[1]
  if month == '12' :
    sum += int(row[6])
print("2019년 12월 총 이용금액 : ", sum, "원")


f.close()