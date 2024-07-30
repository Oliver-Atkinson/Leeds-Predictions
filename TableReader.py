import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.image as image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import scipy.stats as stats

df = pd.read_csv('ChampTablesNoDeds.csv')
# print(np.array(df.loc[df['Rk'] == 1]))

from colour import Color
def ColourRamp(colours: list, n_steps: int = 10):
    """Creates a ramp of colours between the colours given in the colours parameter;
    (colours[0] -> colours[1] -> ... -> colours[-1]) with a total of n_steps colours in the final ramp list.
    
    Parameters:
    colours: list
        A list of colours (each hex or [R,G,B]), with each colour being a start point of a ramp
    n_steps: int (Optional)
        The total number of steps in which to go from the first colour to the last. Defaults to 10.
    
    Returns:
    Ramp: list
        A list of hex strings, of length steps, that ramps between each colour pair in colours
    """


    #Changing the given list to a list of colour objects
    Cols = [Color(col) for col in colours]

    #Number of ramps required is one less than the number of colours
    N_ramps = len(Cols)-1 

    #The number of steps per ramp required is slightly more involved to ensure the final ramp has len == steps
    ramp_step_arr = np.ones(N_ramps)*int(n_steps/N_ramps) 
    #int(steps/N_ramps) alone will lead to an undershoot, due to rounding errors and the removal of ramp end/start pairs when joining multiple ramps
    undershoot = (n_steps % N_ramps) + N_ramps-1
    #Distribute the undershoot amongst the ramp step array until it's taken care of
    while undershoot >= N_ramps:
        ramp_step_arr += 1
        undershoot -= N_ramps
    #Slightly stretch the first ramp(s) as required
    for i in range(undershoot):
        ramp_step_arr[i] += 1

    # Sanity check on number of steps per ramp
    
    #Creating the ramp, first as a list of individual ramps, then concatenating
    Ramp_lists = [list(Cols[n].range_to(Cols[n+1], int(ramp_step_arr[n]))) for n in range(N_ramps)] #List of colour ramps
    Ramp = []
    for i in range(N_ramps-1):
        Ramp += Ramp_lists[i][:-1] #The last colour in each ramp is the start of the next - to avoid repeats we don't include it
    Ramp += Ramp_lists[-1] #The full final ramp should be included (hence the -1 in range(N_ramps-1)), to ensure the final colour ends the overall ramp
    Ramp = [col.hex for col in Ramp] #Converting to hex strings

    return Ramp


champ_tab = pd.read_html('https://www.bbc.co.uk/sport/football/championship/table')[0]
Leeds = champ_tab.loc[champ_tab['Team'] == 'Leeds United']
# print(Leeds)
Leeds_ppg = int(Leeds['Points'])/int(Leeds['Played'])
leeds_pred_points = Leeds_ppg*46

n_seas = 22

points = np.empty((24,n_seas))
for i in range(24):
    points[i] = list(df.loc[df['Rk'] == i+1]['Pts'])

ss_dict = {0:'st',1:'nd',2:'rd',20:'st',21:'nd',22:'rd'}
for n in range(3,20):
    ss_dict.update({n:'th'})
ss_dict.update({23:'th'})

# pal = ColourRamp(['#188D1F','#000','#00e5ff','#ff000d'], 20)
pal = ColourRamp(['#f01111','#c1d1e1','#40004b'], 24)
# print(pal)
pal.reverse()
# pal = ['#7f3b08', '#794f07', '#746006', '#6c6e05', '#536804', '#3b6203', '#255d02', '#125702', '#015001', '#004a0f', '#00441b', '#00452c', '#00463e', '#003d46', '#002c47', '#001b48', '#000a49', '#080049', '#1a004a', '#2d004b']
# lp,lg=31,38
# predp1 = (lp/lg)*38


plt.figure(figsize=(10,10))
# plt.title('Distribution of points by final Championship position, 2002-2023\n',fontsize=16,weight='bold')
plt.rcParams.update({'font.size': 12})
plt.yticks([])
plt.annotate(' Mean\nPoints',(3,145))
plt.annotate('  1'+r"$^{st}$"+'\n2020',(93.2,-85))
plt.annotate('  3'+r"$^{rd}$"+'\n2019',(83.2,-85))
plt.annotate(' 13'+r"$^{th}$"+'\n2018',(60.2,-85))
plt.annotate('  7'+r"$^{th}$"+'\n2017',(75.2,-85))
plt.annotate(' 13'+r"$^{th}$"+'\n2016',(52.3,-85))
for x in np.arange(20,120,10):
    plt.axvline(x, color='grey',alpha=0.5)
for i in range(24):
    pos_points = points[i]
    density = stats.gaussian_kde(pos_points)
    bins = np.arange(10,110,0.1)
    # bins = np.arange(min(pos_points)-7,max(pos_points)+7)
    n,x = np.histogram(pos_points,bins=bins,density=True)
    scale, base = 130, 140-i*10
    line = scale*density(x)+base
    rank = str(i+1)+r"$^{"+ss_dict[i]+r"}$"
    plt.annotate(rank,(-1.5,base-0.8))
    plt.annotate(str(round(np.mean(pos_points),1)),(4.5,base-0.8))
    plt.plot(x, line,color='black',alpha=0.8,linewidth=1.25)
    plt.fill_between(bins,line,base,alpha=0.95,color=pal[i])
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_xlabel('Points', loc='center')
plt.xticks(np.arange(10,120,10))
plt.xlim([-1.5,110])
plt.ylim([-91, 150])
plt.axvline(leeds_pred_points, color='red',alpha=1,linewidth=3)
plt.annotate('PPG\n2023',(leeds_pred_points+0.2,leeds_pred_points-34),weight='bold')
plt.axvline(93, color='green',alpha=1,linewidth=2)
plt.axvline(83, color='green',alpha=1,linewidth=2)
plt.axvline(60, color='green',alpha=1,linewidth=2)
plt.axvline(75, color='green',alpha=1,linewidth=2)
plt.axvline(59, color='green',alpha=1,linewidth=2)
plt.savefig("Champ_pointspos_NoDeds.pdf",bbox_inches='tight')


# print(ColourRamp(['#7f3b08','#00441b','#2d004b'], 20))
#

#------------------------Box plot--------------------

# plt.figure(figsize=(10,10))
fig, ax = plt.subplots(figsize=(100,100))
plt.rcParams.update({'font.size': 120})
plt.yticks([])
# plt.annotate(' Mean\nPoints',(3,145))
for x in np.arange(20,120,10):
    plt.axvline(x, color='grey',alpha=0.5,linewidth=10)
for i in range(24):
    pos_points = points[i]
    min_p, max_p, mean_p, sd = min(pos_points), max(pos_points), np.mean(pos_points), np.std(pos_points)
    scale, base = 1300, 1400-i*100

    y_min, y_max = (base+1020)/2430 -0.04, (base+1000)/2430#1-i/24-0.04, 1-i/24
    plt.axvline(min_p, ymin=y_min, ymax=y_max, color='black',linewidth=10)
    plt.axvline(mean_p-sd, ymin=y_min, ymax=y_max, color='black',linewidth=10)
    plt.axvline(mean_p, ymin=y_min, ymax=y_max, color='black',linewidth=10)
    plt.axvline(mean_p+sd, ymin=y_min, ymax=y_max, color='black',linewidth=10)
    plt.axvline(max_p, ymin=y_min, ymax=y_max, color='black',linewidth=10)

    plt.plot([mean_p-sd,mean_p+sd],[base+10,base+10],color='black',linewidth=10)
    plt.plot([min_p,mean_p-sd],[base+50,base+50],color='black',linewidth=10)
    plt.plot([mean_p+sd,max_p],[base+50,base+50],color='black',linewidth=10)
    plt.plot([mean_p-sd,mean_p+sd],[base+90,base+90],color='black',linewidth=10)

    plt.fill_between([mean_p-sd,mean_p+sd],base+90,base+10,alpha=0.95,color=pal[i])

    row = champ_tab.iloc[[i]]
    p_proj = (float(row['Points'])/float(row['Played']))*46
    team = list(row['Team'])[0]
    # print(team)

    # plt.scatter(p_proj,base+5)

    rank = str(i+1)+r"$^{"+ss_dict[i]+r"}$"
    plt.annotate(rank,(13.5,base+25))

    ax.add_artist(AnnotationBbox(OffsetImage(image.imread('ChampBadges/'+team+'.png'),zoom=0.8), (p_proj, base+50), frameon = False))

ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_xlabel('Points', loc='center',fontsize=120)
plt.xticks(np.arange(20,120,10),fontsize=120)
plt.xlim([10,110])
plt.ylim([-910, 1520])
plt.savefig('Boxplot.pdf',bbox_inches='tight')
# print(champ_tab.head())

# from PIL import Image
# import os

# BadgeDir = 'ChampBadges'
# base_width= 300

# for filename in os.listdir(BadgeDir): 
#     img = Image.open('ChampBadges/'+filename)
#     wpercent = (base_width / float(img.size[0]))
#     hsize = int((float(img.size[1]) * float(wpercent)))
#     img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
#     img.save('ChampBadges/'+filename)