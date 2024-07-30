import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv('matches.csv')

leeds_df = df[df['team'] == 'Liverpool']
leeds2022_df = leeds_df[leeds_df['season'] == 2022]
# print(leeds2022_df)

leeds_xg, leeds_xga = leeds_df['xg'], leeds_df['xga']
# print(leeds_xg)
# print(leeds_xga)

xg2020, xg2021, xg2022 = list(leeds_xg[-38:]), list(leeds_xg[-76:-38]), list(leeds_xg[:27])
xga2020, xga2021, xga2022 = list(leeds_xga[-38:]), list(leeds_xga[-76:-38]), list(leeds_xga[:27])

xg_series = leeds_df['xg']#xg2020+xg2021+xg2022
xga_series = leeds_df['xga']#xga2020+xga2021+xga2022

# s1,s2,s3 = range(0,38), range(45,83), range(90,117)
# gams = list(s1)+list(s2)+list(s3)
gams = len(xga_series)#range(103)
# print(gams)

def mv_avg(dat, win):  
    # Initialize an empty list to store moving averages
    mvavg = []
    # Loop through the array t o
    i = 0
    while i < len(dat) - win + 1:
        # Calculate the average of current window
        win_av = np.sum(dat[i:i+win]) / win
        # Store the average of current window in moving average list
        mvavg.append(win_av)
        # Shift window to right by one position
        i += 1
  
    return mvavg

lds_xg_mvag, lds_xga_mvag = mv_avg(xg_series, 5),  mv_avg(xga_series, 5)
mv_avs_xs = np.arange(2.5,len(lds_xg_mvag)+2,1)
mb,jm,skoob=64,95,98

mpl.style.use('seaborn')
# mpl.rcParams['axes.facecolor'] = '#FFFFFF'
mpl.rcParams['grid.alpha'] =0.7
mpl.rcParams['grid.linestyle']=':'
plt.figure()
# plt.plot(s1, xga2020, color='red')
# plt.plot(s2, xga2021, color='red')
# plt.plot(s3, xga2022, color='red')
# plt.plot(s1, xg2020, color='blue')
# plt.plot(s2, xg2021, color='blue')
# plt.plot(s3, xg2022, color='blue')
for g in [38,76,114,152,190]:
    plt.axvline(g, color = 'white',linestyle='--',alpha=0.7)
# for g in [mb,jm,skoob]:
#     plt.axvline(g, color = 'black',linestyle='-',alpha=0.5)
plt.plot(mv_avs_xs, lds_xg_mvag, color='blue',label="For")
plt.plot(mv_avs_xs, lds_xga_mvag, color='red',label="Against")
# plt.scatter(gams, xg_series, color='blue',s=3)
# plt.scatter(gams, xga_series, color='red',s=3)
# plt.annotate("Bielsa",[mb/2-5,2.9],fontsize=14)
# plt.annotate("Marsch",[mb+(jm-mb)/2-5,2.9],fontsize=14)
# plt.annotate("Skoobs",[jm+(skoob-jm)/2-2,2.625],fontsize=14,rotation=270)
# plt.annotate("Gracia",[skoob+(103-skoob)/2,2.9],fontsize=14)
# plt.ylim([0.5,3])
# plt.xlim([0,114])
plt.ylabel('xG',size=14)
plt.legend(loc='upper right')
plt.xticks([19,57,95,133,171,209],["17-18","18-19","19-20","20-21","21-22","22-23"],fontsize=14)
# plt.xticks([19,57,95],["20-21","21-22","22-23"],fontsize=14)
plt.yticks(fontsize=14)
plt.title('Liverpool xG',fontsize=14,weight='bold')
plt.savefig('LpoolXgDiff.png',bbox_inches='tight')
exit()


wh_df = df[df['team'] == 'West Ham United']
wh_dist = list(wh_df['dist'])
wh_dist.reverse()
gams = range(len(wh_dist))

print(mvavg_dist)
mv_avs_xs = np.arange(2.5,len(mvavg_dist)+2,1)

plt.figure()
mpl.rcParams['axes.facecolor'] = '#7A263A'
mpl.rcParams['grid.alpha'] =0.5
mpl.rcParams['grid.linestyle']='--'
plt.gca().xaxis.grid(False)
# plt.grid(which='minor', axis='both', color='green')
for g in [38,76,114,152,190]:
    plt.axvline(g, color = 'white',linestyle='--',alpha=0.5)
plt.ylim([5,30])
plt.xlim([0,228])
plt.ylabel('Shot Distance (m)',size=14)
plt.xticks([19,57,95,133,171,209],["17-18","18-19","19-20","20-21","21-22","22-23"],fontsize=14)
plt.yticks(fontsize=14)
plt.plot(mv_avs_xs,mvavg_dist,color='#F3D459')
plt.scatter(gams,wh_dist,s=7.5,color='#1BB1E7')
plt.title('West Ham Average Shot Distance',fontsize=16,weight='bold')
plt.savefig('WestHamDist.png',bbox_inches='tight')
print(wh_dist)
