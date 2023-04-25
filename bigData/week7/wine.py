import pandas as pd

#1. 엑셀에서 열 구분자를 세미콜론으로 인식시키기
red_dataFrame = pd.read_csv('./winequality-red.csv', sep = ';', header = 0, engine = 'python')
red_dataFrame.to_csv('./winequality-red2.csv', index = False)

white_dataFrame = pd.read_csv('./winequality-white.csv', sep = ';', header = 0, engine = 'python')
white_dataFrame.to_csv('./winequality-white2.csv', index = False)

#2. 데이터 병합하기
print(red_dataFrame.head())
print(red_dataFrame.shape)
red_dataFrame.insert(0, column = 'type', value = 'red')
print(red_dataFrame.head())
print(red_dataFrame.shape)

print(white_dataFrame.head())
print(white_dataFrame.shape)
white_dataFrame.insert(0, column = 'type', value = 'white')
print(white_dataFrame.head())
print(white_dataFrame.shape)

wine = pd.concat([red_dataFrame, white_dataFrame])
wine.to_csv('./wine.csv', index = False)
print(wine.shape)


#데이터 탐색
print(wine.info())

