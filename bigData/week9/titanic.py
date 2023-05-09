import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc #mac 폰트깨짐 해결위해 추가

rc('font', family='AppleGothic') #mac 폰트깨짐 해결위해 추가	 
plt.rcParams['axes.unicode_minus'] = False  #mac 폰트깨짐 해결위해 추가


#seaborn 내장 데이터셋
titanic = sns.load_dataset("titanic")
titanic.to_csv("./titanic.csv", index = False)

#결측값 확인
print(titanic.isnull().sum())

#나이는 중앙값으로 대체
titanic['age'] = titanic['age'].fillna(titanic['age'].median())

#최빈값 확인
print(titanic['embarked'].value_counts())
print(titanic['deck'].value_counts())
print(titanic['embark_town'].value_counts())

#embarked, deck, embark_town은 최빈값으로 대체
titanic['embarked'] = titanic['embarked'].fillna('S')
titanic['deck'] = titanic['deck'].fillna('C')
titanic['embark_town'] = titanic['embark_town'].fillna('Southampton')

#결측값 재확인
print(titanic.isnull().sum())

#기본 정보 확인하기
print(titanic.info())
print(titanic.survived.value_counts())

#남, 여 승객의 생존율을 pie 차트로 그리기
male_color = ['red', 'grey']
female_color = ['grey', 'red']

plt.subplot(1, 2, 1)
titanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(explode = [0, 0.1], colors = male_color, autopct = '%1.1f%%', shadow = True)
plt.title('Survived(Male)')

plt.subplot(1, 2, 2)
titanic['survived'][titanic['sex'] == 'female'].value_counts().plot.pie(explode = [0, 0.1], colors = female_color, autopct = '%1.1f%%', shadow = True)
plt.title('Survived(Female)')

plt.show()


#객실 등급별 생존자 수 막대 그래프로 그리기
sns.countplot(x = 'pclass', hue = 'survived', data = titanic)
plt.title('Pclass vs Survived')
plt.show()

#전체 상관계수 구하기
titanic_corr = titanic.corr(method = 'pearson')
titanic_corr.to_csv('titanic_corr.csv', index = False)

#특정 변수 사이의 상관계수 구하기
print(titanic['survived'].corr(titanic['adult_male']))
print(titanic['survived'].corr(titanic['fare']))


#산점도로 상관분석 시각화
sns.pairplot(titanic, hue = 'survived')
plt.show()

#두 변수의 상관관계 시각화
sns.catplot(x = 'pclass', y = 'survived', hue = 'sex', data = titanic, kind = 'point')
plt.show()

#객실 등급별 남녀 사망자 비율
dead_data1 = titanic.loc[(titanic['pclass'] == 1) & (titanic['survived'] == 0), 'sex'].value_counts()
dead_data2 = titanic.loc[(titanic['pclass'] == 2) & (titanic['survived'] == 0), 'sex'].value_counts()
dead_data3 = titanic.loc[(titanic['pclass'] == 3) & (titanic['survived'] == 0), 'sex'].value_counts()

plt.subplot(1, 3, 1)
dead_data1.plot.pie(explode = [0, 0.1], colors = male_color, autopct = '%1.1f%%', shadow = True)
plt.title('1등급 남녀 사망자 비율')

plt.subplot(1, 3, 2)
dead_data2.plot.pie(explode = [0, 0.1], colors = male_color, autopct = '%1.1f%%', shadow = True)
plt.title('2등급 남녀 사망자 비율')

plt.subplot(1, 3, 3)
dead_data3.plot.pie(explode = [0, 0.1], colors = male_color, autopct = '%1.1f%%', shadow = True)
plt.title('3등급 남녀 사망자 비율')

plt.show()
