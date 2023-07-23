import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 빈 데이터프레임 생성
df = pd.DataFrame(index=range(7), columns=range(7))

# 각 셀에 값을 채워넣기
# 이 부분에서 음성 유사도 비교를 수행하고 값을 채워넣어야 합니다.
# 예시로 임의의 값들을 사용하겠습니다.
for i in range(7):
    for j in range(7):
        df.iloc[i, j] = i + j

# 히트맵 그리기
sns.heatmap(df.values, annot=True, cmap='coolwarm', linewidths=0.01)
plt.title("음성 유사도 비교")
plt.show()
