import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

x_label_out = []
index = 7

ce_data = []
ma_data = []
rn_data = []
pr_data = []
pb_data = []
ba_data = []
se_data = []
al_data = []
pi_data = []
sp_data = []
rj_data = []
mg_data = []
es_data = []

ce_out = []
ma_out = []
rn_out = []
pr_out = []
pb_out = []
ba_out = []
se_out = []
al_out = []
pi_out = []
sp_out = []
rj_out = []
mg_out = []
es_out = []

covid_files = [

"05-21-2020.csv",
"05-22-2020.csv",
"05-23-2020.csv",
"05-24-2020.csv",
"05-25-2020.csv",
"05-26-2020.csv",
"05-27-2020.csv",
"05-28-2020.csv",
"05-29-2020.csv",
"05-30-2020.csv",
"05-31-2020.csv",
"06-01-2020.csv",
"06-02-2020.csv",
"06-03-2020.csv",
"06-04-2020.csv",
"06-05-2020.csv",
"06-06-2020.csv",
"06-07-2020.csv",
"06-08-2020.csv",
"06-09-2020.csv",
"06-10-2020.csv",
"06-11-2020.csv",
"06-12-2020.csv",
"06-13-2020.csv",
"06-14-2020.csv",
"06-15-2020.csv",
"06-16-2020.csv",
"06-17-2020.csv",
"06-18-2020.csv",
"06-19-2020.csv",
"06-20-2020.csv",
"06-21-2020.csv",
"06-22-2020.csv",
"06-23-2020.csv",
"06-24-2020.csv",
"06-25-2020.csv",
"06-26-2020.csv",
"06-27-2020.csv",
"06-28-2020.csv",
"06-29-2020.csv",
"06-30-2020.csv",
"07-01-2020.csv",
"07-02-2020.csv",
"07-03-2020.csv",
"07-04-2020.csv",
"07-05-2020.csv",
"07-06-2020.csv",
"07-07-2020.csv",
"07-08-2020.csv",
"07-09-2020.csv",
"07-10-2020.csv",
"07-11-2020.csv",
"07-12-2020.csv",
"07-13-2020.csv",
"07-14-2020.csv",
"07-15-2020.csv",
"07-16-2020.csv",
"07-17-2020.csv",
"07-18-2020.csv",
"07-19-2020.csv",
"07-20-2020.csv",
"07-21-2020.csv",
"07-22-2020.csv",
"07-23-2020.csv",
"07-24-2020.csv",
"07-25-2020.csv",
"07-26-2020.csv",
"07-27-2020.csv",
"07-28-2020.csv",
"07-29-2020.csv",
"07-30-2020.csv",
"07-31-2020.csv",
"08-01-2020.csv",
"08-02-2020.csv",
"08-03-2020.csv",
"08-04-2020.csv",
"08-05-2020.csv",
"08-06-2020.csv",
"08-07-2020.csv",
"08-08-2020.csv",
"08-09-2020.csv",
"08-10-2020.csv",
"08-11-2020.csv",
"08-12-2020.csv",
"08-13-2020.csv",
"08-14-2020.csv",
"08-15-2020.csv",
"08-16-2020.csv",
"08-17-2020.csv",
"08-18-2020.csv",
"08-19-2020.csv",
"08-20-2020.csv",
"08-21-2020.csv",
"08-22-2020.csv",
"08-23-2020.csv",
"08-24-2020.csv",
"08-25-2020.csv",
"08-26-2020.csv",
"08-27-2020.csv",
"08-28-2020.csv",
"08-29-2020.csv",
"08-30-2020.csv",
"08-31-2020.csv",
"09-01-2020.csv",
"09-02-2020.csv",
"09-03-2020.csv",
"09-04-2020.csv",
"09-05-2020.csv",
"09-06-2020.csv",
"09-07-2020.csv",
"09-08-2020.csv",
"09-09-2020.csv",
"09-10-2020.csv",
"09-11-2020.csv",
"09-12-2020.csv",
"09-13-2020.csv",
"09-14-2020.csv",
"09-15-2020.csv",
"09-16-2020.csv",
"09-17-2020.csv",
"09-18-2020.csv",
"09-19-2020.csv",
"09-20-2020.csv",
"09-21-2020.csv",
"09-22-2020.csv",
"09-23-2020.csv",
"09-24-2020.csv",
"09-25-2020.csv",
"09-26-2020.csv",
"09-27-2020.csv",
"09-28-2020.csv",
"09-29-2020.csv",
"09-30-2020.csv",
"10-01-2020.csv",
"10-02-2020.csv",
"10-03-2020.csv",
"10-04-2020.csv",
"10-05-2020.csv",
"10-06-2020.csv",
"10-07-2020.csv",
"10-08-2020.csv",
"10-09-2020.csv",
"10-10-2020.csv",
"10-11-2020.csv",
"10-12-2020.csv",
"10-13-2020.csv",
"10-14-2020.csv",
"10-15-2020.csv",
"10-16-2020.csv",
"10-17-2020.csv",
"10-18-2020.csv",
"10-19-2020.csv",
"10-20-2020.csv",
"10-21-2020.csv",
"10-22-2020.csv",
"10-23-2020.csv",
"10-24-2020.csv",
"10-25-2020.csv",
"10-26-2020.csv",
"10-27-2020.csv",
"10-28-2020.csv",
"10-29-2020.csv",
"10-30-2020.csv",
"10-31-2020.csv",
"11-01-2020.csv",
"11-02-2020.csv",
"11-03-2020.csv",
"11-04-2020.csv",
"11-05-2020.csv",
"11-06-2020.csv",
"11-07-2020.csv",
"11-08-2020.csv",
"11-09-2020.csv",
"11-09-2020.csv",
"11-10-2020.csv",
"11-11-2020.csv",
"11-12-2020.csv",
"11-13-2020.csv",
"11-14-2020.csv",
"11-15-2020.csv",
"11-16-2020.csv",
"11-17-2020.csv",
"11-18-2020.csv",
"11-19-2020.csv",
"11-20-2020.csv",
"11-21-2020.csv",
"11-22-2020.csv",
"11-23-2020.csv",
"11-24-2020.csv",
"11-25-2020.csv",
"11-26-2020.csv",
"11-27-2020.csv",
"11-28-2020.csv",
"11-29-2020.csv",
"11-30-2020.csv",
"12-01-2020.csv",
"12-02-2020.csv",
"12-03-2020.csv",
"12-04-2020.csv",
"12-05-2020.csv",
"12-06-2020.csv",
"12-07-2020.csv",
"12-08-2020.csv",
"12-09-2020.csv",
"12-10-2020.csv",
"12-11-2020.csv",
"12-12-2020.csv",
"12-13-2020.csv",
"12-14-2020.csv",
"12-15-2020.csv",
"12-16-2020.csv",
"12-17-2020.csv",
"12-18-2020.csv",
"12-19-2020.csv",
"12-20-2020.csv",
"12-21-2020.csv",
"12-22-2020.csv",
"12-23-2020.csv",
"12-24-2020.csv",
"12-25-2020.csv",
"12-26-2020.csv",
"12-27-2020.csv",
"12-28-2020.csv",
"12-29-2020.csv",
"12-30-2020.csv",
"12-31-2020.csv",
               "01-01-2021.csv",
               "01-02-2021.csv",
               "01-03-2021.csv",
               "01-04-2021.csv",
               "01-05-2021.csv",
               "01-06-2021.csv",
               "01-07-2021.csv",
               "01-08-2021.csv",
               "01-09-2021.csv",
               "01-10-2021.csv",
               "01-11-2021.csv",
               "01-12-2021.csv",
               "01-13-2021.csv",
               "01-14-2021.csv",
               "01-15-2021.csv",
               "01-16-2021.csv",
               "01-17-2021.csv",
               "01-18-2021.csv",
               "01-19-2021.csv",
               "01-20-2021.csv",
               "01-21-2021.csv",
               "01-22-2021.csv",
               "01-23-2021.csv",
               "01-24-2021.csv",
               "01-25-2021.csv",
               "01-26-2021.csv",
               "01-27-2021.csv",
               "01-28-2021.csv",
               "01-29-2021.csv",
               "01-30-2021.csv",
               "01-31-2021.csv",
               "02-01-2021.csv",
               "02-02-2021.csv",
               "02-03-2021.csv",
               "02-04-2021.csv",
               "02-05-2021.csv",
               "02-06-2021.csv",
               "02-07-2021.csv",
               "02-08-2021.csv",
               "02-09-2021.csv",
               "02-10-2021.csv",
               "02-11-2021.csv",
               "02-12-2021.csv",
               "02-13-2021.csv",
               "02-14-2021.csv",
               "02-15-2021.csv",
               "02-16-2021.csv",
               "02-17-2021.csv",
               "02-18-2021.csv",
               "02-19-2021.csv",
               "02-20-2021.csv",
               "02-21-2021.csv",
               "02-22-2021.csv",
               "02-23-2021.csv",
               "02-24-2021.csv",
               "02-25-2021.csv",
               "02-26-2021.csv",
               "02-27-2021.csv",
               "02-28-2021.csv",
               "03-01-2021.csv",
               "03-02-2021.csv",
               "03-03-2021.csv",
               "03-04-2021.csv",
               "03-05-2021.csv",
               "03-06-2021.csv",
               "03-07-2021.csv",
               "03-08-2021.csv",
               "03-09-2021.csv",
               "03-10-2021.csv",
               "03-11-2021.csv",
               "03-12-2021.csv",
               "03-13-2021.csv",
               "03-14-2021.csv",
               "03-15-2021.csv",
               "03-16-2021.csv",
               "03-17-2021.csv",
               "03-18-2021.csv",
               "03-19-2021.csv",
               "03-20-2021.csv",
               "03-21-2021.csv",
               "03-22-2021.csv",
               "03-23-2021.csv",
               "03-24-2021.csv",
               "03-25-2021.csv",
               "03-26-2021.csv",
               "03-27-2021.csv",
               "03-28-2021.csv",
               "03-29-2021.csv",
               "03-30-2021.csv",
               "03-31-2021.csv",
               "04-01-2021.csv",
               "04-02-2021.csv",
               "04-03-2021.csv",
               "04-04-2021.csv",
               "04-05-2021.csv",
               "04-06-2021.csv",
               "04-07-2021.csv",
               "04-08-2021.csv",
               "04-09-2021.csv",
               "04-10-2021.csv",
               "04-11-2021.csv",
               "04-12-2021.csv",
               "04-13-2021.csv",
               "04-14-2021.csv",
               "04-15-2021.csv",
               "04-16-2021.csv",
               "04-17-2021.csv",
               "04-18-2021.csv",
               "04-19-2021.csv",
               "04-20-2021.csv",
               "04-21-2021.csv",
               "04-22-2021.csv",
               "04-23-2021.csv",
               "04-24-2021.csv",
               "04-25-2021.csv",
               "04-26-2021.csv",
               "04-27-2021.csv",
               "04-28-2021.csv",
               "04-29-2021.csv",
               "04-30-2021.csv",
               "05-01-2021.csv",
               "05-02-2021.csv",
               "05-03-2021.csv",
               "05-04-2021.csv",
               "05-05-2021.csv",
               "05-06-2021.csv",
               "05-07-2021.csv",
               "05-08-2021.csv",
               "05-09-2021.csv"]

for pointer in covid_files:
    df = pd.read_csv(pointer)
    ce_line = np.array(df[df['Province_State'] == 'Ceara'])                 #   put all of these strings in a list and get the lines using 'for' loop
    ma_line = np.array(df[df['Province_State'] == 'Maranhao'])
    rn_line = np.array(df[df['Province_State'] == 'Rio Grande do Norte'])
    pr_line = np.array(df[df['Province_State'] == 'Paraiba'])
    pb_line = np.array(df[df['Province_State'] == 'Pernambuco'])
    ba_line = np.array(df[df['Province_State'] == 'Bahia'])
    se_line = np.array(df[df['Province_State'] == 'Sergipe'])
    al_line = np.array(df[df['Province_State'] == 'Alagoas'])
    pi_line = np.array(df[df['Province_State'] == 'Piaui'])
    sp_line = np.array(df[df['Province_State'] == 'Sao Paulo'])
    rj_line = np.array(df[df['Province_State'] == 'Rio de Janeiro'])
    mg_line = np.array(df[df['Province_State'] == 'Minas Gerais'])
    es_line = np.array(df[df['Province_State'] == 'Espirito Santo'])
    ce_data.append(ce_line)                                                 #   put the lines in an only one data frame
    ma_data.append(ma_line)
    rn_data.append(rn_line)
    pr_data.append(pr_line)
    pb_data.append(pb_line)
    ba_data.append(ba_line)
    se_data.append(se_line)
    al_data.append(al_line)
    pi_data.append(pi_line)
    sp_data.append(sp_line)
    rj_data.append(rj_line)
    mg_data.append(mg_line)
    es_data.append(es_line)

for pointer in range(len(ce_data)):
    ce_out.append(ce_data[pointer][0][index])

for pointer in range(len(ma_data)):
    ma_out.append(ma_data[pointer][0][index])

for pointer in range(len(rn_data)):
    rn_out.append(rn_data[pointer][0][index])

for pointer in range(len(pr_data)):
    pr_out.append(pr_data[pointer][0][index])

for pointer in range(len(pb_data)):
    pb_out.append(pb_data[pointer][0][index])

for pointer in range(len(ba_data)):
    ba_out.append(ba_data[pointer][0][index])

for pointer in range(len(se_data)):
    se_out.append(se_data[pointer][0][index])

for pointer in range(len(al_data)):
    al_out.append(al_data[pointer][0][index])

for pointer in range(len(pi_data)):
    pi_out.append(pi_data[pointer][0][index])

for pointer in range(len(sp_data)):
    sp_out.append(sp_data[pointer][0][index])

for pointer in range(len(rj_data)):
    rj_out.append(rj_data[pointer][0][index])

for pointer in range(len(mg_data)):
    mg_out.append(mg_data[pointer][0][index])

for pointer in range(len(es_data)):
    es_out.append(es_data[pointer][0][index])

plt.plot(ce_out)
plt.plot(ma_out)
#plt.plot(rn_out)
#plt.plot(pr_out)
plt.plot(pb_out)
plt.plot(ba_out)
#plt.plot(se_out)
#plt.plot(al_out)
#plt.plot(pi_out)
#plt.plot(sp_out)
#plt.plot(rj_out)
#plt.plot(mg_out)
#plt.plot(es_out)

print(x_label_out)
plt.legend(['Ceará',
            'Maranhão',
#            'Rio Grande do Norte',
#            'Paraíba',
            'Pernambuco',
            'Bahia',
#            'Sergipe',
#            'Alagoas',
#            'Piauí',
#            'São Paulo',
#            'Rio de Janeiro',
#            'Minas Gerais',
#            'Espirito Santo'
            ])

plt.xticks(np.arange(0,390,30))
plt.show()