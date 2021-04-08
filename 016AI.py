import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

covid_data = []
deaths_data = []
covid_files = ["210101covid19data_Brazil.txt",
               "210102covid19data_Brazil.txt",
               "210103covid19data_Brazil.txt",
               "210104covid19data_Brazil.txt",
               "210105covid19data_Brazil.txt",
               "210106covid19data_Brazil.txt",
               "210107covid19data_Brazil.txt",
               "210108covid19data_Brazil.txt",
               "210109covid19data_Brazil.txt",
               "210110covid19data_Brazil.txt",
               "210111covid19data_Brazil.txt",
               "210112covid19data_Brazil.txt",
               "210113covid19data_Brazil.txt",
               "210114covid19data_Brazil.txt",
               "210115covid19data_Brazil.txt"]

for pointer in covid_files:
    df = pd.read_csv(pointer)
    csv_data = np.array(df[['Province_State','Confirmed','Deaths','Active','Case_Fatality_Ratio']])
    covid_data.append(csv_data[5])
print(covid_data)

for deaths_pointer in range(len(covid_data)):
    deaths_data.append(covid_data[deaths_pointer][1])
print(deaths_data)

plt.plot(deaths_data)
plt.show()