import pandas as pd

data_dic = {
    'year' : [2018, 2019, 2020],
    'sales' : [350, 480, 1099]
}
print(data_dic)

df1 = pd.DataFrame(data_dic)
print(df1)

data2 = ['1반','2반','3반','4반','5반']
df2 = pd.DataFrame([[82, 92, 90],[92.8, 89.9, 95.2]], index = ['중간고사', '기말고사'],
                   columns = data2[0:3])
print(df2)

data_df = [['20201101', 'Hong', '90', '95'],['20201102', 'Kim', '93', '94'], ['20201103', 'Lee', '87', '97']]
df3 = pd.DataFrame(data_df)
print(df3)

df3.columns = ['학번', '이름', '중간고사', '기말고사']
print(df3)

print(df3.head(2))

print(df3.tail(2))

print(df3['이름'])

df3.to_csv('pandaTestWrite.csv', encoding='utf-8')

df4 = pd.read_csv('inputTest.csv', encoding='utf-8', index_col = 0, engine='python')
print(df4)