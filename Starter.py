from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import time

fixs_df = pd.read_table("Fixtures.dat", dtype = {'Date': str, 'Time': str, 'Result': str}, sep=' ')

res_list = fixs_df['Result'].tolist() 
n_res = res_list.index(np.nan)

#Convert KO date and times to python datetime objects
#Types a bit nasty but oh well
dats = fixs_df['Date'].tolist()
tims = fixs_df['Time'].tolist()
fix_dattims = []
for i in range(len(dats)):
    hr, mn = tims[i][:2], tims[i][2:]
    day, month = dats[i][:2], dats[i][2:]
    yr = '2023'
    if float(month) <= 6: yr ='2024'
    fix_dattims.append(datetime(int(yr), int(month), int(day), int(hr), int(mn)))

next_ko = fix_dattims[n_res]
comp_time = next_ko+timedelta(hours=2.15)
present = datetime.now()

diff_s = int((comp_time - present).total_seconds()) 
if diff_s > 0:  time.sleep(diff_s)

