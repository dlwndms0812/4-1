import pandas as pd
from statsmodels.formula.api import ols, glm
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

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

wine.columns = wine.columns.str.replace(' ', '_')

wine.describe()
desResult = wine.describe()
desResult.to_csv('./descriptive.csv')

sorted(wine.quality.unique())

wine.quality.value_counts()


#type별 그룹 비교하기
wine.groupby('type')['quality'].describe()

#agg()로 다중 통계랑 구하기
wine.groupby('type').agg(['mean', 'var'])
wine.groupby('type').agg({'quality' : 'mean',
                          'alcohol' : 'max'})
wine.groupby('type').agg({'quality' : ['mean', 'std'],
                          'alcohol' : ['mean', 'std']})


#회귀 분석
Rformula = 'quality~fixed_acidity+volatile_acidity+citric_acid+residual_sugar+chlorides+free_sulfur_dioxide+total_sulfur_dioxide+density+pH+sulphates+alcohol'

regression_result = ols(Rformula, data = wine).fit()
print(regression_result.summary())


#예측 함수 predict()를 적용하여 새로운 샘플 품질 예측
sample1 = wine[wine.columns.difference(['quality', 'type'])]
sample1 = sample1[0:5][:]

sample1_predict = regression_result.predict(sample1)
print(sample1_predict)
print(wine[0 : 5]['quality'])

data = {"fixed_acidity" : [8.5, 8.1],
        "volatile_acidity" : [0.8, 0.5],
        "citric_acid" : [0.3, 0.4],
        "residual_sugar" : [6.1, 5.8],
        "chlorides" : [0.055, 0.04],
        "free_sulfur_dioxide" : [30.0, 30.1],
        "total_sulfur_dioxide" : [98.0, 99],
        "density" : [0.996, 0.91],
        "pH" : [3.25, 3.01], 
        "sulphates" : [0.4, 0.35],
        "alcohol" : [9.0, 0.88]}

sample2 = pd.DataFrame(data, columns = sample1.columns)
sample2_predict = regression_result.predict(sample2)
print(sample2_predict)

#와인 유형에 따른 품질 등급 히스토그램 그리기
sns.set_style('dark')
sns.histplot(red_dataFrame['quality'], kde = True, color = 'red', label = 'red wine')
sns.histplot(white_dataFrame['quality'], kde = True, label = 'white wine')
plt.title("Quality of Wine Type")
plt.legend()
plt.show()


#부분 회귀 플롯으로 시각화 하기
fig = plt.figure(figsize = (8, 13))
sm.graphics.plot_partregress_grid(regression_result, fig = fig)
plt.show()