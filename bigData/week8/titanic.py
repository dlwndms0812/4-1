import seaborn as sns
import pandas as pd

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