"""Automating the family and friends predictions of Leeds United results, and way overthinking the data"""

#Imports
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import colors
from itertools import cycle
import yaml
import sys

#Change x-axis labels from N games to club badges?

#Check for redundancies.....



ID_flag = sys.argv[1]
if ID_flag == '0': datfile, savdir, pref = 'Predictions.dat', '', ''
elif ID_flag == '1': datfile, savdir, pref = 'DadPredictions.dat', 'Dads/Dad', "Dad"

#Read data in 
with open(datfile) as f:
        content = f.readlines()

#Reform into arrays - pretty nasty...
PredData = [x.strip() for x in content] 
Preds = [Pred_str.split() for Pred_str in PredData]

#Splitting out into different components
Names = Preds[0]
Fixtures = [match[0] for match in Preds[1:]]
Fixtures = [fix.replace("_", " (" )+')' for fix in Fixtures] 
Fixtures = [fix.replace("tB", 't B') for fix in Fixtures]
Fixtures = [fix.replace("fW", 'f W') for fix in Fixtures]
Predictions = [match[1:] for match in Preds[1:]]

#Getting the number of game
N_games = len(Fixtures)
N_play = len(Names)-2

Predictions = np.array(Predictions[:N_games])
Results = Predictions[:,0]

#Convert score string to game state (WDL)
def stater(score_str):
    return np.sign(float(score_str[0])-float(score_str[1]))

#Takes an array of predictions and turns them into points
def ScoreGen(pred_arr):

    Odds_dat = np.loadtxt('Odds.dat', delimiter=" ", usecols=range(1,44))
    g_scores = Odds_dat[0,:]

    #Initialising an array to hold the points
    scores, it_gamb = np.zeros(pred_arr.shape), np.zeros(pred_arr.shape)
    for i in range(N_games):
        result = pred_arr[i,0]
        preds = pred_arr[i,1:]
        for j in range(N_play):
            #3 points for being exactly correct, 1 point for the correct result
            if preds[j] == result: scores[i,j+1] = 3
            elif stater(result) == stater(preds[j]): scores[i,j+1] = 1

            #Betting
            odds = Odds_dat[i+1,:]
            odds_dict = dict(zip(g_scores, odds))
            if scores[i,j+1] == 3:
                odd_fac = odds_dict[float(preds[j])]
                if i == 0: 
                    it_gamb[0,j+1] = 10*(odd_fac)
                else: it_gamb[i,j+1] = it_gamb[i-1,j+1] + 10*(odd_fac)
            else: 
                if i == 0: it_gamb[0,j+1] = -10
                else: it_gamb[i,j+1] = it_gamb[i-1,j+1] - 10


    #Set the first column to minus 1 for plotting purposes
    scores[:,0] = -1
    return scores, it_gamb


#Func for converting score preds to league points
def PointsGen(pred_arr):
    s2p = {1:3, 0:1, -1:0}
    point_arr, gf_arr, ga_arr = np.zeros(pred_arr.shape), np.zeros(pred_arr.shape), np.zeros(pred_arr.shape)
    
    for i in range(N_play+1):
        for j in range(N_games): 
            pred = pred_arr[j,i]
            point_arr[j,i] = s2p[stater(pred)]
            gf_arr[j,i], ga_arr[j,i] = float(pred[0]), float(pred[1])
                    
    points = [sum(point_arr[:,x]) for x in range(N_play+1)]
    gfs, gas = [sum(gf_arr[:,x]) for x in range(N_play+1)], [sum(ga_arr[:,x]) for x in range(N_play+1)]
    gds = list(np.array(gfs) - np.array(gas))
    ws = [np.count_nonzero(point_arr[:,x] == 3) for x in range(N_play+1)]
    ds = [np.count_nonzero(point_arr[:,x] == 1) for x in range(N_play+1)]
    ls = [np.count_nonzero(point_arr[:,x] == 0) for x in range(N_play+1)]

    #-------------------------Update for table array-------------------------
    tab_str = ''
    for i in range(N_play+1):
        tab_str += '        '+Names[i+1]+' & ' + "{:.0f}".format(points[i])+' & ' + "{:.0f}".format(ws[i])+' & ' + "{:.0f}".format(ds[i])+' & ' + "{:.0f}".format(ls[i])+' & '+\
                "{:.0f}".format(gfs[i])+' & ' + "{:.0f}".format(gas[i])+' & ' + "{:.0f}".format(gds[i])+r' \\ '+'\n \hline \n' 
    return point_arr, tab_str

#If correct score, go to odds calc, else multiplier = 0
#Cumulative total += 5 * mult, Running total = RT[-1]*mult
#Bookies fav, min odds


#Load data
# FDRs= np.loadtxt('FDRs.dat', skiprows=1,usecols=1,delimiter=' ')
# #Prediction function
# def Predder(point_list):
    #Split into past and future games
    past_FDRs, fut_FDRs = FDRs[:N_games], FDRs[N_games:]

    pred_dict = {}
    #Find the predicted points for each fdr value
    def fdr_p(fdr):
        fdr_ind = [i for i, e in enumerate(past_FDRs) if e == fdr]
        fdr_av = sum(point_list[ind] for ind in fdr_ind)/len(fdr_ind)
        pred_p = fdr_av*list(fut_FDRs).count(fdr)
        pred_dict.update({fdr:fdr_av})
        return pred_p
    
    #Iterate to create dictionary of expected points
    for i in range(2,6):
        fdr_p(i)
    #Create predicted point list
    fin_p = sum(point_list)
    pred_list = [pred_dict[fdr] for fdr in fut_FDRs]

    return np.cumsum(np.array(pred_list))+fin_p

#Running funcs
Scores, Itr_gam = ScoreGen(Predictions)
Points, tab_str = PointsGen(Predictions)

#Setting params - maybe move to a style doc
mpl.rcParams["xtick.bottom"] = False
mpl.rcParams["xtick.labeltop"] = True
mpl.rcParams["ytick.left"] = False
mpl.rcParams["ytick.labelright"] = True
mpl.rcParams["font.family"] = 'sans-serif'
#Defining the colour map
cmap = colors.ListedColormap(['white','black','dodgerblue','darkgreen'])
bounds=[-1,0,1,3,5]
norm = colors.BoundaryNorm(bounds, cmap.N)
#Making the figure
plt.figure(figsize=(30,N_games))
ax = plt.gca()
img = plt.imshow(Scores, interpolation='nearest', cmap=cmap, norm=norm, aspect='auto')
#Including the score labels
for y in range(N_games):
    for x in range(1,N_play+1):
        if x == 0: col = 'black'
        else: col = 'white'
        plt.text(x, y,  "{:.1f}".format(Itr_gam[y,x]),
                 horizontalalignment='center',
                 verticalalignment='center',
                 fontsize=28,color=col,weight='bold')
    plt.text(0, y, Predictions[y,0][0]+' - '+Predictions[y,0][1],
                 horizontalalignment='center',
                 verticalalignment='center',
                 fontsize=28,color='black',weight='bold')
# Setting ticks and gridlines
plt.xticks(np.arange(0,N_play+1),Names[1:], fontsize=28)
plt.yticks(np.arange(0,N_games),Fixtures[:N_games], fontsize=28)
ax.set_xticks(np.arange(-.5, N_play+1, 1), minor=True)
ax.set_yticks(np.arange(-.5, N_games, 1), minor=True)
ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
ax.tick_params(which='minor', bottom=False, left=False)
#Black gridlines for the reality column
for x in range(N_games):
    plt.plot([-0.5,0.5],[x+0.5,x+0.5],color='black',linewidth=3)
plt.savefig(savdir+'ItrGamMatrix.pdf',bbox_inches='tight')
# exit()
# fut_arr = []
# for i in range(N_play+1):
#     fut_arr.append(Predder(Points[:,i]))
# print(fut_arr)
# exit()

#Table
# tpoints, cpoints, mpoints, rpoints, bpoints = 89, 71, 52, 36, 25
# tgam, cgam, mgam, rgam, bgam = 38, 38, 38, 38, 38


#-------------------------Results matrix-------------------------
#Setting params - maybe move to a style doc
mpl.rcParams["xtick.bottom"] = False
mpl.rcParams["xtick.labeltop"] = True
mpl.rcParams["ytick.left"] = False
mpl.rcParams["ytick.labelright"] = True
mpl.rcParams["font.family"] = 'sans-serif'
#Defining the colour map
cmap = colors.ListedColormap(['white','black','dodgerblue','darkgreen'])
bounds=[-1,0,1,3,5]
norm = colors.BoundaryNorm(bounds, cmap.N)
#Making the figure
plt.figure(figsize=(30,N_games))
ax = plt.gca()
img = plt.imshow(Scores, interpolation='nearest', cmap=cmap, norm=norm, aspect='auto')
#Including the score labels
for y in range(N_games):
    for x in range(N_play+1):
        if x == 0: col = 'black'
        else: col = 'white'
        plt.text(x, y, Predictions[y,x][0]+' - '+Predictions[y,x][1],
                 horizontalalignment='center',
                 verticalalignment='center',
                 fontsize=28,color=col,weight='bold')
# Setting ticks and gridlines
plt.xticks(np.arange(0,N_play+1),Names[1:], fontsize=28)
plt.yticks(np.arange(0,N_games),Fixtures[:N_games], fontsize=28)
ax.set_xticks(np.arange(-.5, N_play+1, 1), minor=True)
ax.set_yticks(np.arange(-.5, N_games, 1), minor=True)
ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
ax.tick_params(which='minor', bottom=False, left=False)
#Black gridlines for the reality column
for x in range(N_games):
    plt.plot([-0.5,0.5],[x+0.5,x+0.5],color='black',linewidth=3)
plt.savefig(savdir+'Matrix.pdf',bbox_inches='tight')
# exit()
#-------------------------Ranking table-------------------------
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

# Reading in palettes
with open('//Users/oliver/Documents/Admin/Old Work/Omanos/GitLab/earth-engine-internship/Palettes.yml', "r") as stream:
    Palettes = yaml.safe_load(stream)
# pal = ColourRamp(['#b35806', '#fff', '#542788'], N_play)
#Colour palette
pal = Palettes['RdYlGn_'+str(N_play)]
pal = ['#'+col for col in pal]
pal.reverse()

# exit()
#Sum over array columns for results and creating the ranking
Fin_scores = [sum(Scores[:,x]) for x in range(1,N_play+1)]
point_dict = dict(zip(Names[2:], Fin_scores))
point_dict = dict(sorted(point_dict.items(), key=lambda item: item[1]))
#Flipping the ranking list
name_list = list(point_dict.keys())
name_list.reverse()
rank_dat = [[name, "{:.0f}".format(point_dict[name])] for name in name_list]
#Display rankings
fig, ax = plt.subplots(figsize=(8,N_play*.55))
ax.axis('off')
ax.axis('tight')
cell_cols = [[col,col] for col in pal]
#Dataframe and plot
df = pd.DataFrame(rank_dat)
table = ax.table(cellText=df.values,cellLoc='center',fontsize=28,colWidths=np.zeros(N_play)+0.2, loc='center',cellColours=cell_cols)
table.set_fontsize(26)
table.scale(2.6, 2.6) 
# fig.tight_layout()
# plt.title('Scores on the doors',fontsize=28,loc='center')
plt.savefig(savdir+'Rankings.pdf',bbox_inches='tight')
# exit()

#-------------------------Summary document-------------------------

leader, loser = name_list[0], name_list[-1]
lead_point, los_point = point_dict[leader], point_dict[loser]
GF, GA = Predictions[-1,0][0], Predictions[-1,0][1]

ss_dict = {1:'st',2:'nd',3:'rd'}
if float(str(N_games)[-1]) not in ss_dict.keys(): gam_num = 'th'
else: gam_num = ss_dict[float(str(N_games)[-1])]

if GF > GA: term = 'win over'
elif GF == GA: term  = 'draw with'
else: term = 'loss to'

outs = [str(GF)+' -- '+str(GA), term, Fixtures[-1], str(N_games)+'$^{'+gam_num+'}$',  '('+"{:.0f}".format(N_games/0.46)+'\%', leader,  "{:.0f}".format(lead_point), str(loser),  "{:.0f}".format(los_point),tab_str]
hooks = ['SCORE\n', 'TERM\n', 'TEAM\n', 'NTH\n', 'PERC\n', 'NAMELeader\n', 'Npointstop\n', 'NAMEbottom\n','Npointsbot\n','TABLE\n']

glines = [r'\includegraphics[width=0.5\textwidth]{'+pref+'Rankings.pdf}\n', 
          r'\includegraphics[width=0.8\textwidth]{'+pref+'LinePoints.pdf}\n', 
          r'\includegraphics[width=0.7\textwidth]{'+pref+'LineScores.pdf}\n',
          r'\includegraphics[width=\textwidth]{'+pref+'Matrix.pdf}\n']
ghooks = ['RANKING\n', 'LINEPOINTS\n', 'LINESCORES\n', 'MATRIX\n']

#Redundancies here
with open('TexTemplate.tex') as f:
        content = f.readlines()
rep_lin_inds0 = [content.index(hook) for hook in hooks]
for i in range(len(rep_lin_inds0)):
    content[rep_lin_inds0[i]] = outs[i]+' '
rep_lin_inds1 = [content.index(hook) for hook in ghooks]
for i in range(len(rep_lin_inds1)):
    content[rep_lin_inds1[i]] = glines[i]
with open(savdir+'Summary.tex', 'w') as f:
    for line in content:
        f.write(f"{line}")


#-------------------------Point race animation-------------------------
import bar_chart_race as bcr
# print(score_df)
mpl.rcParams["ytick.labelright"] = False
mpl.rcParams["xtick.labeltop"] = False
cuml_scores = np.cumsum(Scores[:,1:],axis=0)
score_df = pd.DataFrame(cuml_scores,columns=Names[2:],index=Fixtures[:N_games])
bar_race = bcr.bar_chart_race(score_df, figsize=(4, 2.5), period_length=750,title='Leeds Predictions Points', filename=savdir+'race.mp4',fixed_max=True)

mpl.rcParams["ytick.labelright"] = False
mpl.rcParams["xtick.labeltop"] = False
# cuml_scores = np.cumsum(Scores[:,1:],axis=0)
bet_df = pd.DataFrame(Itr_gam,columns=Names[1:],index=Fixtures[:N_games])
bar_race = bcr.bar_chart_race(bet_df, figsize=(4, 2.5), period_length=750,title='Winnings', filename=savdir+'Oddsrace.mp4',fixed_max=False)

fig, ax = plt.subplots(figsize=(11, 9), dpi=120)
# ax.set_facecolor((0, 0, 1, .3))
plt.xlim([-350,500])
plt.xticks([])
plt.yticks([])
ax.tick_params(labelbottom=False, labeltop=False, labelleft=True, labelright=True,
                 bottom=False, top=True, left=False, right=False)
plt.title('Betting',fontsize=28,weight='bold')
for spine in plt.gca().spines.values():
    spine.set_visible(False)
bcr.bar_chart_race(bet_df, figsize=(9,6), period_length=1200, steps_per_period=10, title='Difference from Average', filename=savdir+'Oddsrace.mp4',fixed_max=False,fig=fig,fixed_order=False)



#-------------------------Weekly score graph-------------------------
mpl.style.use('seaborn')
lin='-'
rep_scores = [cuml_scores[:,i][-1] for i in range(N_play) if list(cuml_scores[-1,:]).count(cuml_scores[:,i][-1]) != 1]
rep_uniqs = list(set(rep_scores))
rep_dict = {rep_uniqs[i]: rep_scores.count(rep_uniqs[i]) for i in range(len(rep_uniqs))}

# print(cuml_scores)
fin_s_dict = dict(zip(Names[2:], cuml_scores[-1]))
# print(fin_s_dict)
import math

xint0 = range(1,N_games+4,3)
plt.figure()
for i in range(N_play):
    if i > 5: lin ="--"
    fin_score = cuml_scores[:,i][-1]
    if fin_score not in rep_uniqs: plt.annotate(Names[i+2],[N_games+0.15,cuml_scores[:,i][-1]],fontsize=12)
    else: 
        rep_p_names = [k for k, v in fin_s_dict.items() if v == fin_score]
        text = ''
        for nam in rep_p_names:
            text+=nam
            if nam != rep_p_names[-1]: text += ', '
        plt.annotate(text,[N_games+0.15,cuml_scores[:,i][-1]-0.1],fontsize=12)
    plt.plot(np.arange(1,N_games+1),cuml_scores[:,i],label=Names[2:][i],linestyle=lin)
plt.xlim([1,N_games+4])
plt.ylim(0)
plt.xticks(xint0)
plt.ylabel("Score")
plt.xlabel("Games played")
plt.legend(ncols=2)
plt.savefig(savdir+'LinePoints.pdf',bbox_inches='tight')

#-------------------------League table race score plot-------------------------
champ_tab = pd.read_html('https://www.bbc.co.uk/sport/football/championship/table')[0]
#Bit of an awkward way of doing this, probs a better way...
def tab_inf(pos):
    ent = champ_tab.iloc[pos-1]
    return ent['Team'], ent['Points']

ss_dict = {1:'st',2:'nd',6:'th',12:'th',21:'st',24:'th'}
champ_teams, champ_pts = [],[]
pos_ints = [1,2,6,12,21,24]
for p in pos_ints:
    ct, cpt = tab_inf(p)
    champ_teams.append(ct)
    champ_pts.append(float(cpt))

rep_points = [champ_pts[i] for i in range(len(pos_ints)) if champ_pts.count(champ_pts[i]) != 1]
rep_p_uniqs = list(set(rep_points))
rep_p_dict = {rep_p_uniqs[i]: rep_points.count(rep_p_uniqs[i]) for i in range(len(rep_p_uniqs))}
fin_point_dict = dict(zip(champ_teams, champ_pts))
rep_p_flag = 0
if champ_pts[0]==champ_pts[1]: rep_p_flag = 1

Names[1]='Reality'
cuml_points = np.cumsum(Points[:,0:],axis=0)
lin='-'
rep_ps = [int(cuml_points[:,i][-1]) for i in range (N_play+1) if list(cuml_points[-1,:]).count(cuml_points[:,i][-1]) != 1]
rep_puniqs = list(set(rep_ps))
rep_pdict = {rep_puniqs[i]: rep_ps.count(rep_puniqs[i]) for i in range(len(rep_puniqs))}

fin_p_dict = dict(zip(Names[1:], cuml_points[-1]))

pred_max = max(cuml_points[-1])
table_max = champ_pts[0]
max_plot = int(max([pred_max, table_max]))
x_max = int(N_games+2+10*(N_games/46))+2
yint = range(0, max_plot+2, 3)
xint1 = range(1,x_max,3)

plt.figure(figsize=(8,14))
mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=['black', '#0F08E0', '#44EBDB', '#FF0001','#F5D561', '#FF0AE0'])
for i in list(range(N_play+1)):
    if i > 5: lin ="--"
    fin_p = int(cuml_points[:,i][-1])
    if fin_p not in rep_ps: plt.annotate(Names[i+1],[N_games,cuml_points[:,i][-1]+0.1],fontsize=14)
    else: 
        rep_p_names = [k for k, v in fin_p_dict.items() if v == fin_p]
        text = ''
        for nam in rep_p_names:
            text+=nam
            if nam != rep_p_names[-1]: text += ', '
        plt.annotate(text,[N_games,cuml_points[:,i][-1]+0.1],fontsize=14)
    plt.plot(np.arange(1,N_games+1),cuml_points[:,i],label=Names[1:][i],linestyle=lin)

#Bodge for only the top 2 having the same amount of points
an_pos = [3,3,2,1.5,N_games-3,N_games-5]
for i in range(len(pos_ints)):
    numeral = r"$^{"+ss_dict[pos_ints[i]]+"}$"
    l_start = [pos if pos < N_games-5 else 0 for pos in an_pos]
    fin_ps = champ_pts[i]
    if fin_ps not in rep_p_uniqs: plt.annotate(champ_teams[i]+" ("+str(pos_ints[i])+numeral+")",[an_pos[i],champ_pts[i]+0.1],fontsize=14)
    elif rep_p_flag == 1:
        text = champ_teams[0]+" (1"+r"$^{"+'st'+"}$"+"), "+champ_teams[1]+" (2"+r"$^{"+'nd'+"}$"+")"
        plt.annotate(text,[an_pos[i],champ_pts[i]+0.1],fontsize=14)
    plt.plot([l_start[i],x_max],[champ_pts[i],champ_pts[i]],linestyle='-',color='black',alpha=0.3)
    

plt.xlim([1,N_games+10*(N_games/46)])
plt.xticks(xint1,fontsize=14)
plt.yticks(fontsize=14)
plt.ylim(0)
plt.ylabel("Points",fontsize=16)
plt.xlabel("Games",fontsize=16)
plt.legend(ncols=2,fontsize=14)
plt.yticks(yint)
# plt.savefig(savdir+'LineScores.pdf',bbox_inches='tight')


#-------------------------Betting graph-------------------------
mpl.style.use('seaborn')
lin='-'

xint0 = range(1,N_games+4,3)
plt.figure()
for i in range(N_play):
    if i > 5: lin ="--"
    plt.plot(np.arange(1,N_games+1),Itr_gam[:,i+1],label=Names[2:][i],linestyle=lin)
plt.xlim([1,N_games+4])
# plt.ylim(0)
plt.xticks(xint0)
plt.ylabel("Cash Money")
plt.xlabel("Games played")
plt.legend(ncols=2)
plt.savefig(savdir+'Betting.pdf',bbox_inches='tight')



#-----------------Prediction plot-----------------
# def lin_proj(ngames, ps):
#     ppg = ps/ngames
#     proj_p = np.round(ps+(38-ngames)*ppg)
#     return proj_p

# lin='-'
# plot_ps = [list(cuml_points[:,i])+list(fut_arr[i]) for i in range(N_play+1)]
# fin_ps = []
# for i in range(N_play+1):
#     plot_ps[i][-1] = np.round(plot_ps[i][-1])
#     fin_ps.append(plot_ps[i][-1])
# rep_ps = [fin_ps[i] for i in range (N_play+1) if fin_ps.count(plot_ps[i][-1]) != 1]
# rep_puniqs = list(set(rep_ps))
# rep_pdict = {rep_puniqs[i]: rep_ps.count(rep_puniqs[i]) for i in range(len(rep_puniqs))}
# flip2, flip3 = 1, 1


# plt.figure(figsize=(11,14))
# mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=['black', '#0F08E0', '#44EBDB', '#FF0001','#F5D561', '#FF0AE0'])
# for i in [0,1,3,4,6,5,7,8,2,9]:
#     if i > 5: lin ="--"
#     fin_p = int(plot_ps[i][-1])
#     if fin_p not in rep_ps: plt.annotate(Names[i+1],[38.25,plot_ps[i][-1]-0.2],fontsize=14)
#     else: 
#         if rep_pdict[fin_p] == 2:
#             plt.annotate(Names[i+1],[38.25,(plot_ps[i][-1]-0.25)+flip2*1],fontsize=14)
#             flip2+=-1
#         elif rep_pdict[fin_p] == 3:
#             plt.annotate(Names[i+1],[38.25,(plot_ps[i][-1]-0.25)+flip3*4],fontsize=14)
#             flip3-=1
#     plt.plot(np.arange(1,39),plot_ps[i],label=Names[1:][i],linestyle=lin)
#     # print(Names[1:][i],plot_ps[i][-1])

# plt.axvline(N_games, color = 'g',linestyle='-',alpha=0.5)
# plt.plot([N_games-8.5,tgam,38],[tpoints,tpoints,lin_proj(tgam, tpoints)],linestyle='-',color='black',alpha=0.3)
# plt.annotate("City (1"+r"$^{st}$"+")",[N_games-14,tpoints-0.3],fontsize=14)

# plt.plot([12.5,cgam,38],[cpoints,cpoints,lin_proj(cgam, cpoints)],linestyle='-',color='black',alpha=0.3)
# plt.annotate("Scum (4"+r"$^{th}$"+")",[6,cpoints-0.3],fontsize=14)

# plt.plot([10,mgam,38],[mpoints,mpoints,lin_proj(mgam, mpoints)],linestyle='-',color='black',alpha=0.3)
# plt.annotate("Fulham (10"+r"$^{th}$"+")",[3.5,mpoints-0.3],fontsize=14)

# plt.plot([6.75,rgam,38],[rpoints,rpoints,lin_proj(rgam, rpoints)],linestyle='-',color='black',alpha=0.3)
# plt.annotate("Everton (17"+r"$^{th}$"+")",[1,rpoints],fontsize=14)

# plt.plot([6.25,bgam,38],[bpoints,bpoints,lin_proj(bgam, bpoints)],linestyle='-',color='black',alpha=0.3)
# plt.annotate("SOU (20"+r"$^{th}$"+")",[1.25,bpoints-0.6],fontsize=14)

# plt.xticks(np.arange(0,40,5), fontsize=14)
# plt.yticks(fontsize=14)
# plt.xlim([1,42])
# plt.ylim(0)
# plt.ylabel("Points",fontsize=16)
# plt.xlabel("Games",fontsize=16)
# plt.legend(ncols=2,fontsize=14)
# plt.savefig(savdir+'PredLineScores.pdf',bbox_inches='tight')