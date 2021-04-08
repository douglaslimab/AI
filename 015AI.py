import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

filename = 'covid19data.txt'
df = pd.read_csv(filename)
print(df[['Province_State','Confirmed','Deaths','Active','Case_Fatality_Ratio']])
plt.plot(df.Deaths)
plt.xlabel("State")
plt.show()