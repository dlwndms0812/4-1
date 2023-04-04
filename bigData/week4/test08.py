import pandas as pd

data1 = [10, 20, 30, 40, 50]
print(data1)

data2 = ['1반', '2반', '3반', '4반', '5반']
print(data2)

sr1 = pd.Series(data1)
print(sr1)

sr2 = pd.Series(data2)
print(sr2)

sr3 = pd.Series([101, 102, 103, 104, 105])
print(sr3)

sr4 = pd.Series(['월', '화', '수', '목', '금'])
print(sr4)

sr5 = pd.Series(data1, index =[1000, 1001, 1002, 1003, 1004])
print(sr5)

sr6 = pd.Series(data1, index = data2)
print(sr6)

sr7 = pd.Series(data2, index = sr4)
print(sr7)

print(sr7[2], sr7['수'], sr7[-1])

print(sr7[0:2])

print(sr7.index)

print(sr7.values)