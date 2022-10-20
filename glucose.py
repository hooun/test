import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib
import scipy.stats as stats

# 파일불러오기
url = "https://raw.githubusercontent.com/moksu27/midproject/main/healthcare-dataset-stroke-data.csv"
df = pd.read_csv(url)





# 크기확인
df.shape
# 데이터 일부확인
df.head()
# 정보확인
df.info()

# 가설 뇌졸중 발병 요인에 혈당 평균은 양의 상관관계가 있을 것이다.
# 필요한 데이터인 avg_glucose_level : 평균혈당치 , stroke 뇌졸중 발생여부 (0,1) 만 가져옴
df_glucose_level =  df[["avg_glucose_level","stroke"]]
df_glucose_level = df_glucose_level.copy()

df_glucose_level.head()

df_glucose_level.info()
# 결측치확인
df_glucose_level.isnull().sum()

b = df["avg_glucose_level"]
# 혈당수치 등급 분류 
blood_list= []
for b in b:
    if b <= 50:
        blood_list.append(4)
    elif b > 50 and b <= 80  :
        blood_list.append(5)
    elif b> 80 and b <= 115  :
        blood_list.append(6)
    elif b > 115 and b <= 150  :
        blood_list.append(7)
    elif b > 150 and b <= 180  :
        blood_list.append(8)
    elif b > 180 and b <= 215  :
        blood_list.append(9)
    elif b > 215 and b <= 250  :
        blood_list.append(10)       
    elif b > 250 and b <= 280  :
        blood_list.append(11)
blood_list
df_glucose_level["blood_level"] = blood_list



# 시각화 1
df_glucose_level.hist(bins=50,figsize=(15,10))
plt.show()

#  뇌줄중이 있는 사람만 
df1 = df_glucose_level[(df_glucose_level['stroke']==1)]
# 시각화
sns.histplot(data = df1, x="blood_level")
#  뇌졸중이 없는 사람만 
df0 = df_glucose_level[(df_glucose_level['stroke']==0)]
# 시각화 
sns.histplot(data = df0, x="blood_level")



# 상관관계
# blood_level로 그룹화해서 확인 
df_level_corr=df_glucose_level.groupby("blood_level").corr()
df_level_corr

#.전체 상관관계분석 및 시각화 
corr = df_glucose_level.corr()
corr
mask = np.triu(np.ones_like(corr))
sns.heatmap(corr, annot=True, fmt = '.4f', linewidths=0, cmap='coolwarm',mask=mask)


print("상관관계 분석결과" +
"시각화로 뇌졸중 환자의 분포가 혈당 고위험군보다 정상수치에서 더 많은 걸로 확인"+
"혈당과 뇌졸중과의 상관관계가 최고치가 가장 높은 혈당 수치 단계에서 0.14 정도 "+
"나머지도 소수점 2단위 수준으로 확인 "+
"즉 r이 0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형 관계로서"+
" **결론 혈당과 뇌졸중은 연관이 없다고 생각됩니다**")
