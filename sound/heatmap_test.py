import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 빈 데이터프레임 생성
df = pd.DataFrame(index=["A", "B", "C", "D", "E"], columns=["A", "B", "C", "D", "E"])

# 값 일일이 채우기
df.loc["A", "A"] = 4.0
df.loc["A", "B"] = 3.534132
df.loc["A", "C"] = 3.543632
df.loc["A", "D"] = 3.827813
df.loc["A", "E"] = 3.76589

df.loc["B", "A"] = 3.534132
df.loc["B", "B"] = 4.0
df.loc["B", "C"] = 3.545083
df.loc["B", "D"] = 3.522586
df.loc["B", "E"] = 3.508741

# 나머지 값들도 마찬가지로 채우기 ...

# 히트맵 그리기
sns.heatmap(df, annot=True, cmap='coolwarm', linewidths=0.5)
plt.show()
