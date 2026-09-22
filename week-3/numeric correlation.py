import pandas as pd
df=pd.read_csv("titanic.csv")
print(df.corr(method='pearson', numeric_only=float))

