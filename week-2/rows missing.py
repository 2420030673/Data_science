import pandas as pd
import numpy as np

df= pd.DataFrame({ 'Age':[25,30,np.nan,40,35],
                  'Department':['HR','Finance','Finanace',np.nan,'IT']})

print("Original Dataset")
print(df)

df_drop_rows=df.dropna()
print("After dropping rows:\n")
print(df_drop_rows)