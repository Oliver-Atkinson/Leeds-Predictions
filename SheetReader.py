"""Reads in the prediction data from the google sheet"""

#Copying some stuff from the internet:

#https://learndataanalysis.org/google-drive-api-in-python-getting-started-lesson-1/
#https://www.youtube.com/watch?v=mO2YsPvR7uM&ab_channel=JieJenn

import pickle
import pandas as pd
import os
from datetime import datetime, timedelta
import random
import sys
import numpy as np
import re
import requests
from bs4 import BeautifulSoup
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request

ID_flag = sys.argv[1]

if ID_flag == '0':
#-----------------------------------------------------------
    ID_dict = {'Oja5': 'Oliver',
            'EddieG': 'Dad',
            'Gdad': 'Grandad',
            'Gma': 'Grandma',
            'Debi': 'Mum',
            'WGS': 'Holly',
            'SamC': 'Sam',
            'diddles10': 'TD'}
    sheetid = '1bFucx0mIwdylB2oSqwLAtkogXlxmTJxT_JZ6dR8OKpc'
    output_csv = 'Predictions.csv'
    Preds_outfile = 'Predictions.dat'
#-----------------------------------------------------------

elif ID_flag == '1':
    ID_dict = {'EddieG': 'John',
            'Fark3sSake': 'Neil',
            'Yeboah21': 'Ted',
            'Bartlad69': 'Alex',
            'Maff': 'Maff',
            'Martin': 'Martin',
            'Dave': 'Dave',
            'Tone4568': 'Tony',
            'beer we go': 'Sheky'}
    sheetid = '1BcWXsgpUJUixRDUYvrKrhslhVDlrSaSMEm6TWmzpPXY'
    output_csv = 'DadPredictions.csv'
    Preds_outfile = 'DadPredictions.dat'

def Create_Service(client_secret_file, api_name, api_version, *scopes):
    # print(client_secret_file, api_name, api_version, scopes, sep='-')
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]
    # print(SCOPES)

    cred = None

    pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'
    # print(pickle_file)

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)
    #     print('pickle')

    if not cred or not cred.valid:
        # if cred and cred.expired and cred.refresh_token: #
        #  cred.refresh(Request())                    #
        # else:                                 #Also remove old token (credentials fine)
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
        cred = flow.run_local_server()

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        # print(API_SERVICE_NAME, 'service created successfully')
        return service
    except Exception as e:
        print('Unable to connect.')
        print(e)
        return None

def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt

service = Create_Service('credentials.json', 'Drive', 'v3', ['https://www.googleapis.com/auth/drive'])

bdat = service.files().export_media(
    fileId = sheetid,
    mimeType = 'text/csv'
).execute()


with open(output_csv, 'wb') as f:
    f.write(bdat)
    f.close()

print('CSV file created')

def scraping(date):
    
    """
    Web scraping code
    """
    
    url = "https://www.bbc.com/sport/football/scores-fixtures/" + date

    # html_content = requests.get(url).text
    # print(url)

    # soup = BeautifulSoup(html_content, "html.parser")
    # print(soup)

    # fixs = pd.read_html(url)[0]
    # print(fixs)
    # exit()
        
    tags = ["span", "h3"]
    classes = (["gs-u-display-none gs-u-display-block@m qa-full-team-name sp-c-fixture__team-name-trunc",
                  "sp-c-fixture__status-wrapper qa-sp-fixture-status",
                  'sp-c-fixture__number sp-c-fixture__number--time', "sp-c-fixture__number sp-c-fixture__number--home",
                  "sp-c-fixture__number sp-c-fixture__number--home sp-c-fixture__number--ft",
                 "sp-c-fixture__number sp-c-fixture__number--home sp-c-fixture__number--live-sport",
                  "sp-c-fixture__number sp-c-fixture__number--away sp-c-fixture__number--live-sport",
                 "sp-c-fixture__number sp-c-fixture__number--away sp-c-fixture__number--ft",
                  'gel-minion sp-c-match-list-heading'])

    scraper = soup.find_all(tags, attrs={'class': classes})
    data = [str(l) for l in scraper]
    print(data)
    
    leagues = (['Championship'])
    
    data = [i[-145:] for i in data]
    left, right = '">', '</'
    data = [[l[l.index(left)+len(left):l.index(right)] for l in data if i in l] for i in leagues]
    
    data = [l for l in data if len(l) != 0]
    
    return data


def final_print(date):
    
    """
    Final print function
    
    If user presses Enter while in terminal the scores will refresh without the user needing to enter
    the date to search again. This way it can be called once during matchdays and work throughout the day
    """
        
    ct = 0
    league_in = 0
    h_team, h_score, a_team, a_score, time = 1, 2, 3, 4, 5
    
    data = scraping(date)
    data = [[i.replace('&amp;', '&') for i in group] for group in data] # Brighton & Hove Albion problem
    
    # print(data)
    fix_list = []

    for i in data:
        while ct < len(data[league_in][1:]) // 5:
            fix_list.append(("{:<25} {:^5} {:<25} {:^3} {:>7}".format(i[h_team], i[h_score], i[a_team], i[a_score], i[time])))
            ct += 1
            h_team += 5
            h_score += 5
            a_team += 5
            a_score += 5
            time += 5
        
    return fix_list



preds_df = pd.read_csv(output_csv)

#Reading in and cleaning the fixture list
fixs_df = pd.read_table("Fixtures.dat", dtype = {'Date': str, 'Time': str, 'Result': str}, sep=' ')
fix_list = fixs_df['Team'].tolist()
fix_list = [fix.replace("_", " " ) for fix in fix_list]
ven_list = fixs_df['H/A'].tolist()
fix_list = [fix_list[i]+' ('+ven_list[i]+')' for i in range(len(fix_list))]
# print(fix_list)

#Get the number of fixtures for which there are results
res_list = fixs_df['Result'].tolist() 
n_res = res_list.index(np.nan)

#Convert KO date and times to python datetime objects
#Types a bit nasty but oh well
dats = fixs_df['Date'].tolist()
tims = fixs_df['Time'].tolist()
fix_dattims = []
for i in range(len(fix_list)):
    hr, mn = tims[i][:2], tims[i][2:]
    day, month = dats[i][:2], dats[i][2:]
    yr = '2023'
    if float(month) <= 6: yr ='2024'
    fix_dattims.append(datetime(int(yr), int(month), int(day), int(hr), int(mn)))

#Check if the last fixture without a result has been played - of so, scrape said result and rewrite the Fixtures.dat file
#Only checks the most recent, i.e. will break if multiple games are missing results
#Also, the webpage from which the scraping is done only holds results for the last two weeks

# next_ko = fix_dattims[n_res]
# comp_time = next_ko+timedelta(hours=2)
# present = datetime.now()
# if comp_time < present:
#     date = next_ko.strftime("%Y-%m-%d")
#     fixs = final_print(date)
#     print(fixs)
#     leeds_fix = [fix for fix in fixs if 'Leeds' in fix][0]
#     nums = re.findall(r'\b\d+\b', leeds_fix)
#     if ven_list[n_res] == 'H': score = nums[0]+nums[1]
#     elif ven_list[n_res] == 'A': score = nums[1]+nums[0]
#     res_list[n_res] = score
#     fixs_df.at[n_res, 'Result'] = score

#     #Update the Fixtures.dat file, read it back in and update n_res
#     fixs_df.to_csv("Fixtures.dat", sep=' ', index=False)
#     n_res += 1

# exit()
ID_keys = list(ID_dict.keys())

#Convert the form time stamps to python datetimes
def TimeConvertor(tstr):

    mdict = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 
            'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}

    dtim = datetime(int(tstr[7:11]), mdict[tstr[:3]], int(tstr[4:6]),
                    int(tstr[12:14]), int(tstr[15:17]), int(tstr[18:20]))
    return dtim

#Extract a list of valid predictions for a single person from the df
def PredExtractor(id_key):

    #Get all the entries under a single ID
    df_rows = preds_df.loc[preds_df['ID'] == id_key]
    pred_scores = df_rows['Score'].tolist()

    #Convert the prediction times to datetime objects
    predtims = df_rows['Added Time'].tolist()
    predtims = [TimeConvertor(predtim) for predtim in predtims]
    #Get the most recent pre KO prediction for each game
    fix_preds =[]
    for i in range(n_res):
        fixtim = fix_dattims[i]
        timdiffs = [(fixtim - predtim).total_seconds() for predtim in predtims]
        close_ind = timdiffs.index(min([i for i in timdiffs if i > 0]))
        fix_preds.append(pred_scores[close_ind][0]+pred_scores[close_ind][2])
        #Check for the closest pred also being before the previous KO - if no prediction, default to 3-0
        if fixtim != fix_dattims[0]:
            pre_fixtim = fix_dattims[i-1]
            close_tim = predtims[close_ind]
            if (pre_fixtim - close_tim).total_seconds() > 0:
                fix_preds[-1] = '30'

    return fix_preds

PredDict = dict(zip(ID_keys, range(len(ID_keys))))
for name in ID_keys:
    PredDict.update({name: PredExtractor(name)})

#Including a median 
med_preds = []
for i in range(n_res):
    lscor = np.median([float(PredDict[name][i][0]) for name in PredDict.keys()])
    oppscor = np.median([float(PredDict[name][i][1]) for name in PredDict.keys()])
    med_preds.append('{0:.0f}'.format(lscor)+'{0:.0f}'.format(oppscor))
PredDict.update({'Median': med_preds})
# print(PredDict)

# asps = [11, 50, 40, 30, 31, 20, 31, 31, 31, 20, 11, 20, 30, 20, 51, 30, 31]
# asps = [str(a) for a in asps]
# lscor = np.median([float(a[0]) for a in asps])
# oscor = np.median([float(a[1]) for a in asps])
# print(lscor, oscor)
# exit()

#Get the random predictions and generate a new one if there isn't one for the most recent result
with open(Preds_outfile, 'r') as f:
    predcont = f.readlines()

N_hum = len(ID_keys)

#Find the number of extant random predictions
n_ran_preds = 0
for lin in predcont[1:]:
    hum_preds = lin[lin.index(' ')+1:]
    ran_pred = hum_preds[3*(N_hum+1):-1]
    if ran_pred != '':
        n_ran_preds += 1

#Extract the extant random preds and generate new if required
ran_preds = []
if 'Random' in predcont[0]:
    for i in range(n_ran_preds):
        lin = predcont[1+i]
        hum_preds = lin[lin.index(' ')+1:]
        ran_pred = hum_preds[3*(N_hum+2):3*(N_hum+2)+2]
        if ran_pred == '':
            ran_pred = str(random.randint(0, 4))+str(random.randint(0, 4))
        ran_preds.append(ran_pred)

#Handling the possibility of a new result entry
while len(ran_preds) < n_res:
    ran_preds.append(str(random.randint(0, 4))+str(random.randint(0, 4)))
PredDict.update({'Random': ran_preds})

Odds = np.loadtxt('Odds.dat', delimiter=" ", usecols=range(1,44))
bookies = []
for i in range(n_res):
    index_min = np.argmin(Odds[i+1,:])
    b_fav = Odds[0,:][index_min]
    bookies.append('{0:.0f}'.format(b_fav))
PredDict.update({'Bookies': bookies})


#Writing the predictions to a new file
Head = 'Fixture Result'
Head_names = list(ID_dict.values())
Head_names.append('Median')
Head_names.append('Random')
Head_names.append('Bookies')
for name in Head_names:
    Head += ' '+name
outfile = open(Preds_outfile, 'w')
outfile.write(Head+'\n')

for i in range(n_res):
    lin = fix_list[i].replace(" ", "_").replace("(", "").replace(")", "") + ' ' + res_list[i]
    for name in PredDict.keys():
        lin += ' ' + PredDict[name][i]
    outfile.write(lin+'\n')
outfile.close()