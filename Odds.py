### functions 

# OddsPortal scraper functions 

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
import numpy as np

#Integrate into running - pre game then send back to sleep til post game

URLs = ["https://www.oddsportal.com/football/england/championship/leeds-cardiff-fwEb2njc/#cs;2",
    "https://www.oddsportal.com/football/england/championship/birmingham-leeds-dhsv4j8I/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-west-brom-zs7XNpai/#cs;2",
    "https://www.oddsportal.com/football/england/championship/ipswich-leeds-Uw1FY1D9/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-sheffield-wed-rsRlm1S2/#cs;2",
    "https://www.oddsportal.com/football/england/championship/millwall-leeds-6qvubItL/#cs;2",
    "https://www.oddsportal.com/football/england/championship/hull-city-leeds-x6slyGj5/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-watford-vZ3Jjejh/#cs;2",
    "https://www.oddsportal.com/football/england/championship/southampton-leeds-YZXKbAlT/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-qpr-nwbfD93M/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-bristol-city-CtsISl39/#cs;2",
    "https://www.oddsportal.com/football/england/championship/norwich-leeds-pnwTNaHs/#cs;2",
    "https://www.oddsportal.com/football/england/championship/stoke-city-leeds-dArWVEFI/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-huddersfield-8lClldVn/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leicester-leeds-tWHN0ZEh/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-plymouth-WIXaN8qK/#cs;2",
    "https://www.oddsportal.com/football/england/championship/rotherham-leeds-CIMMFHsB/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-swansea-YJqO8ImA/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-middlesbrough-niPSszR3/#cs;2",
    "https://www.oddsportal.com/football/england/championship/blackburn-leeds-WdMEYVmj/#cs;2",
    "https://www.oddsportal.com/football/england/championship/sunderland-leeds-hWMn8Wv9/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-coventry-xIHW7NpQ/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-ipswich-ddJ1LtFP/#cs;2",
    "https://www.oddsportal.com/football/england/championship/preston-leeds-4WgMApI4/#cs;2",
    "https://www.oddsportal.com/football/england/championship/west-brom-leeds-p2gu4Z0k/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-birmingham-I7cOQd82/#cs;2",
    "https://www.oddsportal.com/football/england/championship/cardiff-leeds-EcTvzen9/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-preston-6BpmjDyE/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-norwich-6VCY1AzQ/#cs;2",
    "https://www.oddsportal.com/football/england/championship/bristol-city-leeds-OUZozbso/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-rotherham-nwbMoSK8/#cs;2",
    "https://www.oddsportal.com/football/england/championship/swansea-leeds-YPh00LmM/#cs;2",
    "https://www.oddsportal.com/football/england/championship/plymouth-leeds-4f8JhzYh/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-leicester-GEgg5DHb/#cs;2",
    "https://www.oddsportal.com/football/england/championship/huddersfield-leeds-GEFOKhHo/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-stoke-city-x2oIUTpA/#cs;2",
    "https://www.oddsportal.com/football/england/championship/sheffield-wed-leeds-QovVNITf/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-millwall-8OObwbTs/#cs;2",
    "https://www.oddsportal.com/football/england/championship/watford-leeds-hEcefYJu/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-hull-city-zcgGkAYA/#cs;2",
    "https://www.oddsportal.com/football/england/championship/coventry-leeds-jXNvrJW1/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-sunderland-YTrCHJNK/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-blackburn-bX3RMEa0/#cs;2",
    "https://www.oddsportal.com/football/england/championship/middlesbrough-leeds-hCE5NojB/#cs;2",
    "https://www.oddsportal.com/football/england/championship/qpr-leeds-hzJNTMCp/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-southampton-vkENn2JM/#cs;2",
    "https://www.oddsportal.com/football/england/championship/norwich-leeds-OK01cix1/#cs;2",
    "https://www.oddsportal.com/football/england/championship/leeds-norwich-pzkAeV6D/#cs;2",
    'https://www.oddsportal.com/football/england/championship/leeds-southampton-YJBMWNJa/#cs;2']

# driver = webdriver.Chrome()
# driver.get("https://www.oddsportal.com/football/england/championship/")
# sleep(5)
# gameRows = driver.find_elements(By.XPATH,'//div[@class="group flex"]')
# data = {}
# rowData = [row.text.split("\n") for row in gameRows]
# print(len(gameRows))
# for row in rowData:
#     if row[2] == "\u2013":
#         try:
#             data.update({row[1]+" vs. "+row[3]:{
#                                         "Team1_Odds":row[4],
#                                         "Draw_Odds":row[5],
#                                         "Team2_Odds":row[6]
#                                         }})
#         except:
#             continue
#     else:
#         try:
#             data.update({row[1]+" vs. "+row[5]:{
#                                         "Team1_Odds":row[6],
#                                         "Draw_Odds":row[7],
#                                         "Team2_Odds":row[8]
#                                         }})
#         except:
#             continue


# with open("Champ.json","w") as jsonFile:
#     json.dump(data,jsonFile,indent=4)


fixs_df = pd.read_table("Fixtures.dat", dtype = {'Date': str, 'Time': str, 'Result': str}, sep=' ')
fix_list = fixs_df['Team'].tolist()
fix_list = [fix.replace("_", " " ) for fix in fix_list]
ven_list = fixs_df['H/A'].tolist()
fix_list = [fix_list[i]+"_"+ven_list[i] for i in range(len(fix_list))]


#May need to update
#Ofc watch for the home away switches - got the venue in the last char of the fixture
good_scores = ["1-0", "2-0", "2-1", '3-0', '3-1', '3-2', '4-0', '4-1', '4-2', '4-3', '5-0', '5-1', '5-2', '5-3', '5-4', '6-0', '6-1', '6-2', '7-0', '7-1', '0-0', '1-1', '2-2', '3-3', '4-4', '5-5', '0-1', '0-2', '1-2', '0-3', '1-3', '2-3', '0-4', '1-4', '2-4', '3-4', '0-5', '1-5', '2-5', '0-6', '1-6', '2-6', '0-7', '1-7']

def Odds_Getter(fix_ind):
    driver = webdriver.Chrome()
    driver.get(URLs[fix_ind])
    sleep(1)
    gameRows = driver.find_elements(By.XPATH,'//div[@class="relative flex flex-col"]')
    rowData = [row.text.split("\n") for row in gameRows]

    rowDict = {}
    if fix_list[fix_ind][-1]=="H":
        for row in rowData:
            rowDict.update({row[0].replace(":", "-" ): row[2]})
    else:
         for row in rowData:
            rowDict.update({row[0][::-1].replace(":", "-" ): row[2]})

    dec_odds_list = fix_list[fix_ind]+" "
    scores = 'Score '


    for score in good_scores:
        if score in list(rowDict.keys()):
            if '-' not in rowDict[score]:
                odd_str = rowDict[score].split('/')
                dec_odds = float(odd_str[0])/float(odd_str[1])+1
                # print(score, dec_odds)
            
            else: dec_odds = 5000
            dec_odds_list += str(dec_odds)+" "
            scores += score+" "

    return scores, dec_odds_list

# file = open('Odds.dat',"w")
# Head = "Score "
# for score in good_scores:
#     Head += score+" "
# file.write(Head+'\n')

# for i in range(42):
#     scores, dec_odds_list = Odds_Getter(i)
#     file.write(dec_odds_list+'\n')

# file.close()
scores, dec_odds_list  = Odds_Getter(-1)
print(dec_odds_list)
exit()

ID_flag = '0'
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

# print(Predictions)
# print(Results)

# print(len(good_scores))
#Read data in 

Odds = np.loadtxt('Odds.dat', delimiter=" ", usecols=range(1,len(good_scores)))
bookies = []
for i in range(len(URLs)):
    index_min = np.argmin(Odds[i+1,:])
    # print(Odds[i+1,:][index_min])
    b_fav = Odds[0,:][index_min]
    # print(b_fav)
    bookies.append('{0:.0f}'.format(b_fav))
print(bookies)




exit()









exit()




def create_clean_table_two_ways(df):
  # (a) Count the number of bookmakers
  nbooks = df['Bookmaker'].nunique()
  
  # (b) Assign a number to each game
  L = [0 for i in range(df['Bookmaker'].size)]
  for i in range(1,df['Bookmaker'].size):
    if (df['Date'][i] != df['Date'][i-1]) | (df['Home_id'][i] != df['Home_id'][i-1]) | (df['Away_id'][i] != df['Away_id'][i-1]):
      L[i] = 1

  df['MatchId'] = np.cumsum(L) + 1

  # (c) Create final dataframe containing only one line per match
  df_final = pd.DataFrame(index=range(max(df['MatchId'])), columns=range(7)) #  Home_id, Away_id, Date, Score_home, Score_away, Season, MatchId
  df_final.columns = ['MatchId','Season','Home_id', 'Away_id', 'Date', 'Score_home', 'Score_away']
  c = 0
  for book in df['Bookmaker'].unique():
    print(book)
    df_final['{}_H'.format(book)] = 'Na' # Home victory odds
    df_final['{}_A'.format(book)] = 'Na' # Away victory odds
    for id in range(1, max(df['MatchId']) + 1):
      new_df = df[(df['Bookmaker'] == book) & (df['MatchId'] == id)]
      if new_df.shape[0] > 0:
        #print(id)
        df_final['{}_H'.format(book)].iloc[id-1] = new_df['OddHome'].iloc[0]
        df_final['{}_A'.format(book)].iloc[id-1] = new_df['OddAway'].iloc[0]
        df_final['MatchId'].iloc[id-1] = new_df['MatchId'].iloc[0]
        df_final['Season'].iloc[id-1] = new_df['Season'].iloc[0]
        df_final['Home_id'].iloc[id-1] = new_df['Home_id'].iloc[0]
        df_final['Away_id'].iloc[id-1] = new_df['Away_id'].iloc[0]
        df_final['Date'].iloc[id-1] = new_df['Date'].iloc[0]
        df_final['Score_home'].iloc[id-1] = new_df['Score_home'].iloc[0]
        df_final['Score_away'].iloc[id-1] = new_df['Score_away'].iloc[0]
    c+=1
    
  try : 
    days = df_final['Date'].str[:2]
    months = df_final['Date'].str[3:6]
    years = df_final['Date'].str[7:]
    months[months == 'Jan'] = '01'
    months[months == 'Feb'] = '02'
    months[months == 'Mar'] = '03'
    months[months == 'Apr'] = '04'
    months[months == 'May'] = '05'
    months[months == 'Jun'] = '06'
    months[months == 'Jul'] = '07'
    months[months == 'Aug'] = '08'
    months[months == 'Sep'] = '09'
    months[months == 'Oct'] = '10'
    months[months == 'Nov'] = '11'
    months[months == 'Dec'] = '12'
    date = days + '/' + months + '/' + years
    df_final['Date'] = pd.to_datetime(date, format='%d/%m/%Y')
    df.sort_values(by=['Date'])
  except:
    print('Cannot convert Date into regular Date format')

  return(df_final)

def create_clean_table_three_ways(df):
  # (a) Count the number of bookmakers
  nbooks = df['Bookmaker'].nunique()
  
  # (b) Assign a number to each game
  L = [0 for i in range(df['Bookmaker'].size)]
  for i in range(1,df['Bookmaker'].size):
    if (df['Date'][i] != df['Date'][i-1]) | (df['Home_id'][i] != df['Home_id'][i-1]) | (df['Away_id'][i] != df['Away_id'][i-1]):
      L[i] = 1

  df['MatchId'] = np.cumsum(L) + 1

  # (c) Create final dataframe containing only one line per match
  df_final = pd.DataFrame(index=range(max(df['MatchId'])), columns=range(7)) #  Home_id, Away_id, Date, Score_home, Score_away, Season, MatchId
  df_final.columns = ['MatchId','Season','Home_id', 'Away_id', 'Date', 'Score_home', 'Score_away']
  c = 0
  for book in df['Bookmaker'].unique():
    print(book)
    df_final['{}_H'.format(book)] = 'Na' # Home victory odds
    df_final['{}_D'.format(book)] = 'Na' # Draw odds
    df_final['{}_A'.format(book)] = 'Na' # Away victory odds
    for id in range(1, max(df['MatchId']) + 1):
      new_df = df[(df['Bookmaker'] == book) & (df['MatchId'] == id)]
      if new_df.shape[0] > 0:
        #print(id)
        df_final['{}_H'.format(book)].iloc[id-1] = new_df['OddHome'].iloc[0]
        df_final['{}_D'.format(book)].iloc[id-1] = new_df['OddDraw'].iloc[0]
        df_final['{}_A'.format(book)].iloc[id-1] = new_df['OddAway'].iloc[0]
        df_final['MatchId'].iloc[id-1] = new_df['MatchId'].iloc[0]
        df_final['Season'].iloc[id-1] = new_df['Season'].iloc[0]
        df_final['Home_id'].iloc[id-1] = new_df['Home_id'].iloc[0]
        df_final['Away_id'].iloc[id-1] = new_df['Away_id'].iloc[0]
        df_final['Date'].iloc[id-1] = new_df['Date'].iloc[0]
        df_final['Score_home'].iloc[id-1] = new_df['Score_home'].iloc[0]
        df_final['Score_away'].iloc[id-1] = new_df['Score_away'].iloc[0]
    c+=1
    
  try : 
    days = df_final['Date'].str[:2]
    months = df_final['Date'].str[3:6]
    years = df_final['Date'].str[7:]
    months[months == 'Jan'] = '01'
    months[months == 'Feb'] = '02'
    months[months == 'Mar'] = '03'
    months[months == 'Apr'] = '04'
    months[months == 'May'] = '05'
    months[months == 'Jun'] = '06'
    months[months == 'Jul'] = '07'
    months[months == 'Aug'] = '08'
    months[months == 'Sep'] = '09'
    months[months == 'Oct'] = '10'
    months[months == 'Nov'] = '11'
    months[months == 'Dec'] = '12'
    date = days + '/' + months + '/' + years
    df_final['Date'] = pd.to_datetime(date, format='%d/%m/%Y')
    df.sort_values(by=['Date'])
  except:
    print('Cannot convert Date into regular Date format')

  return(df_final)
  

def create_clean_df(fileloc, sep = ";", ways = 2):
  df = pd.read_csv(fileloc + '.csv', sep = sep)
  if ways == 2:
    df = create_clean_table_two_ways(df)
  if ways == 3:
    df = create_clean_table_three_ways(df)
  
  df.to_csv(fileloc +'_CLEAN' +  '.csv', index = False)
  print('Finished cleaning table!')
  return(0)

global DRIVER_LOCATION
DRIVER_LOCATION = "C:\\Users\\Utilisateur\\Desktop\\chromedriver.exe"

global TYPE_ODDS
TYPE_ODDS = 'CLOSING' # you can change to 'OPENING' if you want to collect opening odds, any other value will make the program collect CLOSING odds

def get_opening_odd(xpath):
    # I. Get the raw data by hovering and collecting
    data = driver.find_element("xpath", xpath)
    hov = ActionChains(driver).move_to_element(data)
    hov.perform()
    data_in_the_bubble = driver.find_element("xpath", "//*[@id='tooltiptext']")
    hover_data = data_in_the_bubble.get_attribute("innerHTML")

    # II. Extract opening odds
    b = re.split('<br>', hover_data)
    c = [re.split('</strong>',y)[0] for y in b][-2]
    opening_odd = re.split('<strong>', c)[1]

    #print(opening_odd)
    return(opening_odd)
    
    
def fi(a):
    try:
        driver.find_element("xpath", a).text
    except:
        return False

def ffi(a):
    if fi(a) != False :
        return driver.find_element("xpath", a).text
            
def fffi(a):
    if TYPE_ODDS == 'OPENING':
        try:
            return get_opening_odd(a) 
        except:
            return ffi(a)  
    else:
        return(ffi(a))

def fi2(a):
    try:
        driver.find_element("xpath", a).click()
    except:
        return False

def ffi2(a):
    if fi2(a) != False :
        fi2(a)
        return(True)
    else:
        return(None)



def get_data_typeA(i, link):
    driver.get(link)
    reject_ads()

    target = '//*[@id="tournamentTable"]/tbody/tr[{}]/td[2]/a'.format(i)
    a = ffi2(target)
    if a == True:
        print('We wait 4 seconds')
        L = []
        time.sleep(4)
        # Now we collect all bookmaker
        for j in range(1,30): # only first 10 bookmakers displayed
            Book = ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[1]/div/a[2]'.format(j)) # first bookmaker name
            Odd_1 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[2]/div'.format(j)) # first home odd
            Odd_2 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[3]/div'.format(j)) # first away odd
            match = ffi('//*[@id="col-content"]/h1') # match teams
            final_score = ffi('//*[@id="event-status"]')
            date = ffi('//*[@id="col-content"]/p[1]') # Date and time
            print(match, Book, Odd_1, Odd_2, date, final_score, i, '/ 500 ')
            L = L + [(match, Book, Odd_1, Odd_2, date, final_score)]
        return(L)

    return(None)

def get_data_next_games_typeA(i, link):
    L = None
    driver.get(link)
    reject_ads()

    target = '//*[@id="tournamentTable"]/tbody/tr[{}]/td[2]/a[2]'.format(i)
    a = ffi2(target)

    L = []

    if a == True:
        print('We wait 4 seconds')
        time.sleep(4)
        # Now we collect all bookmaker
        for j in range(1,30): # only first 10 bookmakers displayed, CHANGE 01/05/2020 -> div[1] BECOMES div + WE STOP AT td[...] for odds
            Book = ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[1]/div/a[2]'.format(j)) # first bookmaker name
            Odd_1 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[2]/a'.format(j)) # first home odd
            Odd_2 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[3]/a'.format(j)) # first away odd
            match = ffi('//*[@id="col-content"]/h1') # match teams
            #final_score = ffi('//*[@id="event-status"]')
            date = ffi('//*[@id="col-content"]/p[1]') # Date and time
            print(match, Book, Odd_1, Odd_2, date, i, '/ 500 ')
            L = L + [(match, Book, Odd_1, Odd_2, date)]
            
            Book = ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[1]/div/a[2]'.format(j)) # first bookmaker name
            Odd_1 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[2]/div'.format(j)) # first home odd
            Odd_2 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[3]/div'.format(j)) # first away odd
            match = ffi('//*[@id="col-content"]/h1') # match teams
            #final_score = ffi('//*[@id="event-status"]')
            date = ffi('//*[@id="col-content"]/p[1]') # Date and time
            print(match, Book, Odd_1, Odd_2, date, i, '/ 500 ')
            L = L + [(match, Book, Odd_1, Odd_2, date)]
            
    target = '//*[@id="tournamentTable"]/tbody/tr[{}]/td[2]/a'.format(i)
    a = ffi2(target)
    if a == True:
        print('We wait 4 seconds')
        time.sleep(4)
        # Now we collect all bookmaker
        for j in range(1,30): # only first 10 bookmakers displayed, CHANGE 01/05/2020 -> div[1] BECOMES div + WE STOP AT td[...] for odds
            Book = ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[1]/div/a[2]'.format(j)) # first bookmaker name
            Odd_1 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[2]/a'.format(j)) # first home odd
            Odd_2 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[3]/a'.format(j)) # first away odd
            match = ffi('//*[@id="col-content"]/h1') # match teams
            #final_score = ffi('//*[@id="event-status"]')
            date = ffi('//*[@id="col-content"]/p[1]') # Date and time
            print(match, Book, Odd_1, Odd_2, date, i, '/ 500 ')
            L = L + [(match, Book, Odd_1, Odd_2, date)]
            
            Book = ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[1]/div/a[2]'.format(j)) # first bookmaker name
            Odd_1 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[2]/div'.format(j)) # first home odd
            Odd_2 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[3]/div'.format(j)) # first away odd
            match = ffi('//*[@id="col-content"]/h1') # match teams
            #final_score = ffi('//*[@id="event-status"]')
            date = ffi('//*[@id="col-content"]/p[1]') # Date and time
            print(match, Book, Odd_1, Odd_2, date, i, '/ 500 ')
            L = L + [(match, Book, Odd_1, Odd_2, date)]

    return(L)

def scrape_page_typeA(page, sport, country, tournament, SEASON):
    link = 'https://www.oddsportal.com/{}/{}/{}-{}/results/page/1/#/page/{}'.format(sport, country, tournament, SEASON, page)
    DATA = []
    for i in range(1,100):
        content = get_data_typeA(i, link)
        if content != None:
            DATA = DATA + content
    print(DATA)
    return(DATA)

def scrape_page_next_games_typeA(country, sport, tournament, nmax = 20):
    link = 'https://www.oddsportal.com/{}/{}/{}/'.format(sport, country,tournament)
    DATA = []
    for i in range(1,nmax):
        print(i)
        content = get_data_next_games_typeA(i, link)
        if content != None:
            DATA = DATA + content
    print(DATA)
    return(DATA)

def scrape_page_current_season_typeA(page,sport, country, tournament):
    link = 'https://www.oddsportal.com/{}/{}/{}/results/page/1/#/page/{}'.format(sport,country,tournament,page)
    DATA = []
    for i in range(1,100):
        content = get_data_typeA(i, link)
        if content != None:
            DATA = DATA + content
    print(DATA)
    return(DATA)

def scrape_current_tournament_typeA(sport, tournament, country, SEASON, max_page = 25):
    global driver
    ############### NOW WE SEEK TO SCRAPE THE ODDS AND MATCH INFO################################
    DATA_ALL = []
    for page in range(1, max_page):
        print('We start to scrape the page n°{}'.format(page))
        try:
            driver.quit() # close all widows
        except:
            pass
        driver = webdriver.Chrome()
        data = scrape_page_typeA(page,sport, country, tournament, SEASON)
        DATA_ALL = DATA_ALL + [y for y in data if y != None]
        driver.close()

    data_df = pd.DataFrame(DATA_ALL)
    try:
        data_df.columns = ['TeamsRaw', 'Bookmaker', 'OddHome', 'OddAway', 'DateRaw' ,'ScoreRaw']
    except:
        print('Function crashed, probable reason : no games scraped (empty season)')
        return(1)
    ##################### FINALLY WE CLEAN THE DATA AND SAVE IT ##########################
    '''Now we simply need to split team names, transform date, split score'''

    # (0) Filter out None rows
    data_df = data_df[~data_df['Bookmaker'].isnull()].dropna().reset_index()
    data_df["TO_KEEP"] = 1
    for i in range(len(data_df["TO_KEEP"])):
        if len(re.split(':',data_df["ScoreRaw"][i]))<2 :
            data_df["TO_KEEP"].iloc[i] = 0

    data_df = data_df[data_df["TO_KEEP"] == 1]

    # (a) Split team names
    data_df["Home_id"] = [re.split(' - ',y)[0] for y in data_df["TeamsRaw"]]
    data_df["Away_id"] = [re.split(' - ',y)[1] for y in data_df["TeamsRaw"]]
    # (b) Transform date
    data_df["Date"] = [re.split(', ',y)[1] for y in data_df["DateRaw"]]
    # (c) Split score
    data_df["Score_home"] = [re.split(':',y)[0][-3:] for y in data_df["ScoreRaw"]]
    data_df["Score_away"] = [re.split(':',y)[1][:3] for y in data_df["ScoreRaw"]]
    for j in range(len(data_df["Score_home"])):
      str_home = data_df["Score_home"].iloc[j]
      str_away = data_df["Score_away"].iloc[j]
      if str_home[0] == 't':
        data_df["Score_home"].iloc[j] = str_home[1:]
      if str_away[-1] == '(':
        data_df["Score_away"].iloc[j] = str_away[:-1]
    # (e) Set season column
    data_df["Season"] = SEASON
    # Finally we save results
    if not os.path.exists('./{}_FULL'.format(tournament)):
        os.makedirs('./{}_FULL'.format(tournament))
    if not os.path.exists('./{}'.format(tournament)):
        os.makedirs('./{}'.format(tournament))

    data_df.to_csv('./{}_FULL/{}_{}_FULL.csv'.format(tournament,tournament, SEASON), sep=';', encoding='utf-8', index=False)
    data_df[['Home_id', 'Away_id', 'Bookmaker', 'OddHome', 'OddAway', 'Date', 'Score_home', 'Score_away','Season']].to_csv('./{}/{}_{}.csv'.\
        format(tournament,tournament, SEASON), sep=';', encoding='utf-8', index=False)

    return(data_df)

def scrape_current_season_typeA(tournament, sport, country, SEASON, max_page = 25):
    global driver
    ############### NOW WE SEEK TO SCRAPE THE ODDS AND MATCH INFO################################
    DATA_ALL = []
    for page in range(1, max_page):
        print('We start to scrape the page n°{}'.format(page))
        try:
            driver.quit() # close all widows
        except:
            pass
        driver = webdriver.Chrome()
        data = scrape_page_current_season_typeA(page, sport, country, tournament)
        DATA_ALL = DATA_ALL + [y for y in data if y != None]
        driver.close()
    data_df = pd.DataFrame(DATA_ALL)
    try:
        data_df.columns = ['TeamsRaw', 'Bookmaker', 'OddHome', 'OddAway', 'DateRaw' ,'ScoreRaw']
    except:
        print('Function crashed, probable reason : no games scraped (empty season)')
        return(1)
    ##################### FINALLY WE CLEAN THE DATA AND SAVE IT ##########################
    '''Now we simply need to split team names, transform date, split score'''

    # (0) Filter out None rows
    data_df = data_df[~data_df['Bookmaker'].isnull()].dropna().reset_index()
    data_df["TO_KEEP"] = 1
    for i in range(len(data_df["TO_KEEP"])):
        if len(re.split(':',data_df["ScoreRaw"][i]))<2 :
            data_df["TO_KEEP"].iloc[i] = 0

    data_df = data_df[data_df["TO_KEEP"] == 1]
    # (a) Split team names
    data_df["Home_id"] = [re.split(' - ',y)[0] for y in data_df["TeamsRaw"]]
    data_df["Away_id"] = [re.split(' - ',y)[1] for y in data_df["TeamsRaw"]]
    # (b) Transform date
    data_df["Date"] = [re.split(', ',y)[1] for y in data_df["DateRaw"]]
    # (c) Split score
    data_df["Score_home"] = [re.split(':',y)[0][-3:] for y in data_df["ScoreRaw"]]
    data_df["Score_away"] = [re.split(':',y)[1][:3] for y in data_df["ScoreRaw"]]
    
    for j in range(len(data_df["Score_home"])):
      str_home = data_df["Score_home"].iloc[j]
      str_away = data_df["Score_away"].iloc[j]
      if str_home[0] == 't':
        data_df["Score_home"].iloc[j] = str_home[1:]
      if str_away[-1] == '(':
        data_df["Score_away"].iloc[j] = str_away[:-1]
        
    # (e) Set season column
    data_df["Season"] = SEASON
    # Finally we save results
    if not os.path.exists('./{}_FULL'.format(tournament)):
        os.makedirs('./{}_FULL'.format(tournament))
    if not os.path.exists('./{}'.format(tournament)):
        os.makedirs('./{}'.format(tournament))

    data_df.to_csv('./{}_FULL/{}_CurrentSeason_FULL.csv'.format(tournament,tournament), sep=';', encoding='utf-8', index=False)
    data_df[['Home_id', 'Away_id', 'Bookmaker', 'OddHome', 'OddAway', 'Date', 'Score_home', 'Score_away','Season']].\
        to_csv('./{}/{}_CurrentSeason.csv'.format(tournament,tournament), sep=';', encoding='utf-8', index=False)
    return(data_df)

def scrape_league_typeA(Season, sport, country1, tournament1, nseason, current_season = 'yes', max_page = 25):
    long_season = (len(Season) > 6) # indicates whether Season is in format '2010-2011' or '2011' depends on the league) 
    Season = int(Season[0:4])
    for i in range(nseason):
        SEASON1 = '{}'.format(Season)
        if long_season:
          SEASON1 = '{}-{}'.format(Season, Season+1)
        print('We start to collect season {}'.format(SEASON1))
        scrape_current_tournament_typeA(sport = sport, tournament = tournament1, country = country1, SEASON = SEASON1, max_page = max_page)
        print('We finished to collect season {} !'.format(SEASON1))
        Season+=1

    if current_season == 'yes' : 
        SEASON1 = '{}'.format(Season)
        if long_season:
          SEASON1 = '{}-{}'.format(Season, Season+1)
        print('We start to collect current season')
        scrape_current_season_typeA(tournament = tournament1, sport = sport, country = country1, SEASON = 'CurrentSeason', max_page = max_page)
        print('We finished to collect current season !')

    # Finally we merge all files
    file1 = pd.read_csv('./{}/'.format(tournament1) + os.listdir('./{}/'.format(tournament1))[0], sep=';')
    print(os.listdir('./{}/'.format(tournament1))[0])
    for filename in os.listdir('./{}/'.format(tournament1))[1:]:
        file = pd.read_csv('./{}/'.format(tournament1) + filename, sep=';')
        print(filename)
        file1 = file1.append(file)

    file1 = file1.reset_index()

    #Correct falsly collected data for away (in case of 1X2 instead of H/A odds)
    for i in range(file1.shape[0]):
        if (1/file1["OddHome"].iloc[i] + 1/file1["OddAway"].iloc[i]) < 1 :
            file1["OddAway"].iloc[i] = 1 / ((1 - 1/file1["OddHome"].iloc[i])*1.07) #  1/1.07 = 0.934 => 6.5 % margin (estimation)
            print(file1["OddHome"].iloc[i], file1["OddAway"].iloc[i], i)
    file1.to_csv("./{}/All_data_{}.csv".format(tournament1, tournament1))

    print('All good! ')
    return(file1)

def scrape_next_games_typeA(tournament, sport, country, SEASON, nmax = 30):
    global driver
    ############### NOW WE SEEK TO SCRAPE THE ODDS AND MATCH INFO################################
    DATA_ALL = []
    try:
        driver.quit() # close all widows
    except:
        pass

    driver = webdriver.Chrome()
    data = scrape_page_next_games_typeA(country, sport, tournament, nmax)
    DATA_ALL = DATA_ALL + [y for y in data if y != None]
    driver.close()

    data_df = pd.DataFrame(DATA_ALL)
    try:
        data_df.columns = ['TeamsRaw', 'Bookmaker', 'OddHome', 'OddAway', 'DateRaw']
    except:
        print('Function crashed, probable reason : no games scraped (empty season)')
        return(1)

    data_df["ScoreRaw"] = '0:0'
    ##################### FINALLY WE CLEAN THE DATA AND SAVE IT ##########################
    '''Now we simply need to split team names, transform date, split score'''

    # (0) Filter out None rows
    data_df = data_df[~data_df['Bookmaker'].isnull()].dropna().reset_index()
    data_df["TO_KEEP"] = 1
    for i in range(len(data_df["TO_KEEP"])):
        if len(re.split(':',data_df["ScoreRaw"][i]))<2 :
            data_df["TO_KEEP"].iloc[i] = 0

    data_df = data_df[data_df["TO_KEEP"] == 1]

    # (a) Split team names
    data_df["Home_id"] = [re.split(' - ',y)[0] for y in data_df["TeamsRaw"]]
    data_df["Away_id"] = [re.split(' - ',y)[1] for y in data_df["TeamsRaw"]]

    # (b) Transform date
    data_df["Date"] = [re.split(', ',y)[1] for y in data_df["DateRaw"]]

    # (c) Split score
    data_df["Score_home"] = 0
    data_df["Score_away"] = 0

    # (d) Set season column
    data_df["Season"] = SEASON


    # Finally we save results
    if not os.path.exists('./{}'.format(tournament)):
        os.makedirs('./{}'.format(tournament))
    data_df[['Home_id', 'Away_id', 'Bookmaker', 'OddHome', 'OddAway', 'Date', 'Score_home', 'Score_away','Season']].to_csv('./{}/NextGames_{}_{}_08042020.csv'.format(tournament,tournament, SEASON), sep=';', encoding='utf-8', index=False)


    return(data_df)



def get_data_typeB(i, link):
    driver.get(link)
    reject_ads()
    target = '//*[@id="tournamentTable"]/tbody/tr[{}]/td[2]/a'.format(i)
    a = ffi2(target)
    if a == True:
        print('We wait 4 seconds')
        L = []
        time.sleep(4)
        # Now we collect all bookmaker
        for j in range(1,30): # only first 10 bookmakers displayed
            Book = ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[1]/div/a[2]'.format(j)) # first bookmaker name
            Odd_1 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[2]/div'.format(j)) # first home odd
            Odd_2 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[3]/div'.format(j)) # first away odd
            match = ffi('//*[@id="col-content"]/h1') # match teams
            final_score = ffi('//*[@id="event-status"]')
            date = ffi('//*[@id="col-content"]/p[1]') # Date and time
            print(match, Book, Odd_1, Odd_2, date, final_score, i, '/ 500 ')
            if final_score[-1].isalpha(): # if last character is a letter
                print('We detect one player retired!')
                return(None)
            L = L + [(match, Book, Odd_1, Odd_2, date, final_score)]
        return(L)

    return(None)

def get_data_next_games_typeB(i, link):
    L = None
    driver.get(link)
    reject_ads()
    target = '//*[@id="tournamentTable"]/tbody/tr[{}]/td[2]/a[2]'.format(i)
    a = ffi2(target)

    L = []

    if a == True:
        print('We wait 4 seconds')
        time.sleep(4)
        # Now we collect all bookmaker
        for j in range(1,30): # only first 10 bookmakers displayed, CHANGE 01/05/2020 -> div[1] BECOMES div + WE STOP AT td[...] for odds
            Book = ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[1]/div/a[2]'.format(j)) # first bookmaker name
            Odd_1 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[2]/a'.format(j)) # first home odd
            Odd_2 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[3]/a'.format(j)) # first away odd
            match = ffi('//*[@id="col-content"]/h1') # match teams
            #final_score = ffi('//*[@id="event-status"]')
            date = ffi('//*[@id="col-content"]/p[1]') # Date and time
            print(match, Book, Odd_1, Odd_2, date, i, '/ 500 ')
            L = L + [(match, Book, Odd_1, Odd_2, date)]
            
            Book = ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[1]/div/a[2]'.format(j)) # first bookmaker name
            Odd_1 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[2]/div'.format(j)) # first home odd
            Odd_2 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[3]/div'.format(j)) # first away odd
            match = ffi('//*[@id="col-content"]/h1') # match teams
            #final_score = ffi('//*[@id="event-status"]')
            date = ffi('//*[@id="col-content"]/p[1]') # Date and time
            print(match, Book, Odd_1, Odd_2, date, i, '/ 500 ')
            L = L + [(match, Book, Odd_1, Odd_2, date)]
            
    target = '//*[@id="tournamentTable"]/tbody/tr[{}]/td[2]/a'.format(i)
    a = ffi2(target)
    if a == True:
        print('We wait 4 seconds')
        time.sleep(4)
        # Now we collect all bookmaker
        for j in range(1,30): # only first 10 bookmakers displayed, CHANGE 01/05/2020 -> div[1] BECOMES div + WE STOP AT td[...] for odds
            Book = ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[1]/div/a[2]'.format(j)) # first bookmaker name
            Odd_1 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[2]/a'.format(j)) # first home odd
            Odd_2 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[3]/a'.format(j)) # first away odd
            match = ffi('//*[@id="col-content"]/h1') # match teams
            #final_score = ffi('//*[@id="event-status"]')
            date = ffi('//*[@id="col-content"]/p[1]') # Date and time
            print(match, Book, Odd_1, Odd_2, date, i, '/ 500 ')
            L = L + [(match, Book, Odd_1, Odd_2, date)]
            
            Book = ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[1]/div/a[2]'.format(j)) # first bookmaker name
            Odd_1 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[2]/div'.format(j)) # first home odd
            Odd_2 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[3]/div'.format(j)) # first away odd
            match = ffi('//*[@id="col-content"]/h1') # match teams
            #final_score = ffi('//*[@id="event-status"]')
            date = ffi('//*[@id="col-content"]/p[1]') # Date and time
            print(match, Book, Odd_1, Odd_2, date, i, '/ 500 ')
            L = L + [(match, Book, Odd_1, Odd_2, date)]
            


    return(L)

def scrape_page_typeB(page, country, tournament, SEASON, alpha_game = ['We_scrape_full_season','We_scrape_full_season','We_scrape_full_season']):
    link = 'https://www.oddsportal.com/tennis/{}/{}/results/#/page/{}/'.format(country,tournament,page)
    DATA = []
    REACH_END = 0
    print("alpha_game = ", alpha_game)
    for i in range(1,100):
      if REACH_END == 0 :
        content = get_data_typeB(i, link)
        if content != None:
          #print(content)
          p1 = re.split(' - ', content[0][0])[0] 
          p2 = re.split(' - ', content[0][0])[1]
          date = re.split(', ', content[0][4])[1]
          if (p1 == alpha_game[0]) & (p2 == alpha_game[1]) & (date == alpha_game[2]):
            REACH_END = 1
            print("REACH_END = 1, the scraping should stop!", "\n")
          if (p1 != alpha_game[0]) | (p2 != alpha_game[1]) | (date != alpha_game[2]):
            DATA = DATA + list(content)
          
    #print(DATA)
    print("REACH_END = ", REACH_END)
    return(DATA, REACH_END)
    

def scrape_page_next_games_typeB(country, tournament, nmax = 20):
    link = 'https://www.oddsportal.com/tennis/{}/{}/'.format(country,tournament)
    DATA = []
    for i in range(1,nmax):
        print(i)
        content = get_data_next_games_typeB(i, link)
        if content != None:
            DATA = DATA + content
    print(DATA)
    return(DATA)
  

def scrape_current_tournament_typeB(Surface, bestof = 3, tournament = 'wta-lyon', country = 'france', name_to_write = 'WTA Lyon', SEASON = '2020', max_page = 20):
    global driver
    REACH_END = 0
    
    if not os.path.exists('./{}/{}_{}.csv'.format(tournament,tournament, SEASON)):
        alpha_game = ['We_scrape_full_season','We_scrape_full_season','We_scrape_full_season']
    elif os.path.exists('./{}/{}_{}.csv'.format(tournament,tournament, SEASON)):
      file = pd.read_csv('./{}/{}_{}.csv'.format(tournament,tournament, SEASON), sep=';', encoding='utf-8')
      alpha_game = [file["P1"].iloc[0],file["P2"].iloc[0],file["Date"].iloc[0]]

    print("We start to scrape the following tournament :", tournament)
    
    try:
        driver.quit() # close all widows
    except:
        pass

    driver = webdriver.Chrome()
    #SEASON = '''2020'''
    DATA_ALL = []
    for page in range(1, max_page + 1):
      if REACH_END == 0 :
        print('We start to scrape the page n°{}'.format(page))
        data, REACH_END = scrape_page_typeB(page, country, tournament, SEASON, alpha_game)
        DATA_ALL = DATA_ALL + [y for y in data if y != None]
        print('We finished to scrape the page n°{}'.format(page))
    driver.close()
    
    
    ##################### FINALLY WE CLEAN THE DATA AND SAVE IT ##########################
    DATA_ALL_CLEANED = DATA_ALL
    #for i in range(len(DATA_ALL)):
        #DATA_ALL_CLEANED+= DATA_ALL[i]
    #print(DATA_ALL_CLEANED)
    #print(len(DATA_ALL_CLEANED))
    scores = getScore(DATA_ALL_CLEANED)
    teams = [re.split(' - ',y) for y in [y[0] for y in DATA_ALL_CLEANED]]
    set_scores = [re.split(':',y) for y in [y[5][13:16] for y in DATA_ALL_CLEANED]]
    DATE = [re.split(', ',y) for y in [y[4] for y in DATA_ALL_CLEANED]]
    games_score = [re.split(',',y) for y in [y[5][18:] for y in DATA_ALL_CLEANED]]
    set1 = [re.split(',',y) for y in [y[0] for y in games_score]]
    set2 = [re.split(',',y) for y in [y[1] for y in games_score]]
    #set3 = [re.split(',',y) for y in [y[2] for y in games_score]]
    set1games = [re.split(':',y) for y in [y[0] for y in set1]]
    set2games = [re.split(':',y) for y in [y[0] for y in set2]]
    FINAL_DATASET = pd.DataFrame({'Date' : [y[1] for y in DATE], #'Time': [y[2] for y in DATE],
                                'Bookmaker' : [y[1] for y in DATA_ALL_CLEANED],
                                'Home_id' : [y[0] for y in teams],
                                'Away_id' : [y[1] for y in teams],
                                'OddHome' : [y[2] for y in DATA_ALL_CLEANED],
                                'OddAway' : [y[3] for y in DATA_ALL_CLEANED],
                                'Score_home': [scores[y[0] + ' - ' + y[1]]['setP1'] for y in teams], #[y[0][len(y[0])-1:len(y[0])] for y in set_scores],
                                'Score_away': [scores[y[0] + ' - ' + y[1]]['setP2'] for y in teams], #[y[1][0] for y in set_scores],
                                'Set1score1' : [scores[y[0] + ' - ' + y[1]]['jeux']['set1P1'] for y in teams], #[y[0] for y in set1games],
                                'Set1score2' : [scores[y[0] + ' - ' + y[1]]['jeux']['set1P2'] for y in teams], #[y[1] for y in set1games],
                                'Set2score1' : [scores[y[0] + ' - ' + y[1]]['jeux']['set2P1'] for y in teams], #[y[0] for y in set2games],
                                'Set2score2' : [scores[y[0] + ' - ' + y[1]]['jeux']['set2P2'] for y in teams], #[y[1] for y in set2games]
                                'Set3score1' : [scores[y[0] + ' - ' + y[1]]['jeux']['set3P1'] for y in teams],
                                'Set3score2' : [scores[y[0] + ' - ' + y[1]]['jeux']['set3P2'] for y in teams],
                                'Set4score1' : [scores[y[0] + ' - ' + y[1]]['jeux']['set4P1'] for y in teams],
                                'Set4score2' : [scores[y[0] + ' - ' + y[1]]['jeux']['set4P2'] for y in teams],
                                'Set5score1' : [scores[y[0] + ' - ' + y[1]]['jeux']['set5P1'] for y in teams],
                                'Set5score2' : [scores[y[0] + ' - ' + y[1]]['jeux']['set5P2'] for y in teams]
                                })
                                
                          
    #print(FINAL_DATASET.head())
    FINAL_DATASET["Tournament"] = name_to_write
    FINAL_DATASET["Season"] = SEASON
    FINAL_DATASET["Surface"] = Surface
    FINAL_DATASET["Best.of"] = bestof

    # (0) Filter out None rows
    FINAL_DATASET = FINAL_DATASET[~FINAL_DATASET['OddHome'].isnull()].dropna().reset_index()
    FINAL_DATASET = FINAL_DATASET[~FINAL_DATASET['OddAway'].isnull()].dropna().reset_index()

    if not os.path.exists('./{}'.format(tournament)):
        os.makedirs('./{}'.format(tournament))
    FINAL_DATASET.to_csv('./{}/{}_{}.csv'.format(tournament, tournament, SEASON), sep=';', encoding='utf-8', index=False)
    #print(os.listdir())
    #print(os.getcwd())
    return(FINAL_DATASET)
    
    
def scrape_next_games_typeB(Surface, bestof, tournament , country , name_to_write, SEASON = '2020'):
    global driver
    
    try:
        driver.quit() # close all widows
    except:
        pass

 
    driver = webdriver.Chrome()
    #SEASON = '''2020'''
    DATA_ALL = []
    for page in range(1):
        print('We start to scrape the page n°{}'.format(page+1))
        data = scrape_page_next_games_typeB(country, tournament)
        DATA_ALL.append([y for y in data if y != None])
        
    driver.close()
    ##################### FINALLY WE CLEAN THE DATA AND SAVE IT ##########################
    DATA_ALL_CLEANED = []
    for i in range(len(DATA_ALL)):
        DATA_ALL_CLEANED+= DATA_ALL[i]
    #print(DATA_ALL_CLEANED)
    #print(len(DATA_ALL_CLEANED))
    #scores = getScore(DATA_ALL_CLEANED)
    teams = [re.split(' - ',y) for y in [y[0] for y in DATA_ALL_CLEANED]]
    #set_scores = [re.split(':',y) for y in [y[5][13:16] for y in DATA_ALL_CLEANED]]
    DATE = [re.split(', ',y) for y in [y[4] for y in DATA_ALL_CLEANED]]
    #games_score = [re.split(',',y) for y in [y[5][18:] for y in DATA_ALL_CLEANED]]
    #set1 = [re.split(',',y) for y in [y[0] for y in games_score]]
    #set2 = [re.split(',',y) for y in [y[1] for y in games_score]]
    #set3 = [re.split(',',y) for y in [y[2] for y in games_score]]
    #set1games = [re.split(':',y) for y in [y[0] for y in set1]]
    #set2games = [re.split(':',y) for y in [y[0] for y in set2]]
    FINAL_DATASET = pd.DataFrame({'Date' : [y[1] for y in DATE], #'Time': [y[2] for y in DATE],
                                'Bookmaker' : [y[1] for y in DATA_ALL_CLEANED],
                                'Home_id' : [y[0] for y in teams],
                                'Away_id' : [y[1] for y in teams],
                                'OddHome' : [y[2] for y in DATA_ALL_CLEANED],
                                'OddAway' : [y[3] for y in DATA_ALL_CLEANED],
                                'Score_home': 0, #[y[0][len(y[0])-1:len(y[0])] for y in set_scores],
                                'Score_away': 0, #[y[1][0] for y in set_scores],
                                'Set1score1' : 0, #[y[0] for y in set1games],
                                'Set1score2' : 0, #[y[1] for y in set1games],
                                'Set2score1' : 0, #[y[0] for y in set2games],
                                'Set2score2' : 0, #[y[1] for y in set2games]
                                'Set3score1' : 0,
                                'Set3score2' : 0,
                                'Set4score1' : 0,
                                'Set4score2' : 0,
                                'Set5score1' : 0,
                                'Set5score2' : 0
                                })
                                
                          
    #print(FINAL_DATASET.head())
    FINAL_DATASET["Tournament"] = name_to_write
    FINAL_DATASET["Season"] = SEASON
    FINAL_DATASET["Surface"] = Surface
    FINAL_DATASET["Best.of"] = bestof


    # (0) Filter out None rows
    FINAL_DATASET = FINAL_DATASET[~FINAL_DATASET['OddHome'].isnull()].dropna().reset_index()
    FINAL_DATASET = FINAL_DATASET[~FINAL_DATASET['OddAway'].isnull()].dropna().reset_index()

    if not os.path.exists('./{}'.format(tournament)):
        os.makedirs('./{}'.format(tournament))
    FINAL_DATASET.to_csv('./{}/NextGames_{}_{}.csv'.format(tournament, tournament, SEASON), sep=';', encoding='utf-8', index=False)
    #print(os.listdir())
    #print(os.getcwd())
    return(FINAL_DATASET)


def get_data_typeC(i, link):
    driver.get(link)
    reject_ads()
    target = '//*[@id="tournamentTable"]/tbody/tr[{}]/td[2]/a'.format(i)
    a = ffi2(target)
    if a == True:
        print('We wait 4 seconds')
        L = []
        time.sleep(4)
        # Now we collect all bookmaker
        for j in range(1,30): # only first 10 bookmakers displayed
            Book = ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[1]/div/a[2]'.format(j)) # first bookmaker name
            Odd_1 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[2]/div'.format(j)) # first home odd
            Odd_X = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[3]/div'.format(j)) # draw odd
            Odd_2 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[4]/div'.format(j)) # first away odd
            match = ffi('//*[@id="col-content"]/h1') # match teams
            final_score = ffi('//*[@id="event-status"]')
            date = ffi('//*[@id="col-content"]/p[1]') # Date and time
            print(match, Book, Odd_1, Odd_X, Odd_2, date, final_score, i, '/ 500 ')
            L = L + [(match, Book, Odd_1, Odd_X, Odd_2, date, final_score)]
        return(L)

    return(None)

def get_data_next_games_typeC(i, link):
    driver.get(link)
    reject_ads()
    target = '//*[@id="tournamentTable"]/tbody/tr[{}]/td[2]/a[2]'.format(i)
    a = ffi2(target)

    L = []


    if a == True:
        print('We wait 4 seconds')
        time.sleep(4)
        # Now we collect all bookmaker
        for j in range(1,30): # only first 10 bookmakers displayed
            Book = ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[1]/div/a[2]'.format(j)) # first bookmaker name
            Odd_1 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[2]/a'.format(j)) # first home odd
            Odd_X = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[3]/a'.format(j)) # draw odd
            Odd_2 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[4]/a'.format(j)) # first away odd
            match = ffi('//*[@id="col-content"]/h1') # match teams
            final_score = ffi('//*[@id="event-status"]')
            date = ffi('//*[@id="col-content"]/p[1]') # Date and time
            print(match, Book, Odd_1, Odd_X, Odd_2, date, final_score, i, '/ 30 ')
            L = L + [(match, Book, Odd_1, Odd_X, Odd_2, date, final_score)]
            
            Book = ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[1]/div/a[2]'.format(j)) # first bookmaker name
            Odd_1 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[2]/div'.format(j)) # first home odd
            Odd_X = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[3]/div'.format(j)) # draw odd
            Odd_2 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[4]/div'.format(j)) # first away odd
            match = ffi('//*[@id="col-content"]/h1') # match teams
            final_score = ffi('//*[@id="event-status"]')
            date = ffi('//*[@id="col-content"]/p[1]') # Date and time
            print(match, Book, Odd_1, Odd_X, Odd_2, date, final_score, i, '/ 30 ')
            L = L + [(match, Book, Odd_1, Odd_X, Odd_2, date, final_score)]
            
    target = '//*[@id="tournamentTable"]/tbody/tr[{}]/td[2]/a'.format(i)
    a = ffi2(target)
    if a == True:
        print('We wait 4 seconds')
        time.sleep(4)
        # Now we collect all bookmaker
        for j in range(1,30): # only first 10 bookmakers displayed
            Book = ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[1]/div/a[2]'.format(j)) # first bookmaker name
            Odd_1 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[2]/a'.format(j)) # first home odd
            Odd_X = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[3]/a'.format(j)) # draw odd
            Odd_2 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[4]/a'.format(j)) # first away odd
            match = ffi('//*[@id="col-content"]/h1') # match teams
            final_score = ffi('//*[@id="event-status"]')
            date = ffi('//*[@id="col-content"]/p[1]') # Date and time
            print(match, Book, Odd_1, Odd_X, Odd_2, date, final_score, i, '/ 30 ')
            L = L + [(match, Book, Odd_1, Odd_X, Odd_2, date, final_score)]
            
            Book = ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[1]/div/a[2]'.format(j)) # first bookmaker name
            Odd_1 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[2]/div'.format(j)) # first home odd
            Odd_X = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[3]/div'.format(j)) # draw odd
            Odd_2 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[4]/div'.format(j)) # first away odd
            match = ffi('//*[@id="col-content"]/h1') # match teams
            final_score = ffi('//*[@id="event-status"]')
            date = ffi('//*[@id="col-content"]/p[1]') # Date and time
            print(match, Book, Odd_1, Odd_X, Odd_2, date, final_score, i, '/ 30 ')
            L = L + [(match, Book, Odd_1, Odd_X, Odd_2, date, final_score)]
            


    return(L)

def scrape_page_typeC(page, sport, country, tournament, SEASON):
    link = 'https://www.oddsportal.com/{}/{}/{}-{}/results/page/1/#/page/{}'.format(sport,country,tournament,SEASON,page)
    DATA = []
    for i in range(1,100):
        content = get_data_typeC(i, link)
        if content != None:
            DATA = DATA + content
    print(DATA)
    return(DATA)

def scrape_page_next_games_typeC(country,sport,  tournament, nmax = 20):
    link = 'https://www.oddsportal.com/{}/{}/{}/'.format(sport, country,tournament)
    DATA = []
    for i in range(1,nmax):
        print(i)
        content = get_data_next_games_typeC(i, link)
        if content != None:
            DATA = DATA + content
    print(DATA)
    return(DATA)

def scrape_page_current_season_typeC(page,sport, country, tournament):
    link = 'https://www.oddsportal.com/{}/{}/{}/results/page/1/#/page/{}'.format(sport,country,tournament,page)
    DATA = []
    for i in range(1,100):
        content = get_data_typeC(i, link)
        if content != None:
            DATA = DATA + content
    print(DATA)
    return(DATA)

def scrape_current_tournament_typeC(sport, tournament, country, SEASON, max_page = 25):
    global driver
    ############### NOW WE SEEK TO SCRAPE THE ODDS AND MATCH INFO################################
    DATA_ALL = []
    for page in range(1, max_page + 1):
        print('We start to scrape the page n°{}'.format(page))
        try:
            driver.quit() # close all widows
        except:
            pass
    
 
        driver = webdriver.Chrome()
        data = scrape_page_typeC(page, sport, country, tournament, SEASON)
        DATA_ALL = DATA_ALL + [y for y in data if y != None]
        driver.close()

    data_df = pd.DataFrame(DATA_ALL)

    try:
        data_df.columns = ['TeamsRaw', 'Bookmaker', 'OddHome','OddDraw', 'OddAway', 'DateRaw' ,'ScoreRaw']
    except:
        print('Function crashed, probable reason : no games scraped (empty season)')
        return(1)
    ##################### FINALLY WE CLEAN THE DATA AND SAVE IT ##########################
    '''Now we simply need to split team names, transform date, split score'''

    # (0) Filter out None rows
    data_df = data_df[~data_df['Bookmaker'].isnull()].dropna().reset_index()
    data_df["TO_KEEP"] = 1
    for i in range(len(data_df["TO_KEEP"])):
        if len(re.split(':',data_df["ScoreRaw"][i]))<2 :
            data_df["TO_KEEP"].iloc[i] = 0

    data_df = data_df[data_df["TO_KEEP"] == 1]

    # (a) Split team names
    data_df["Home_id"] = [re.split(' - ',y)[0] for y in data_df["TeamsRaw"]]
    data_df["Away_id"] = [re.split(' - ',y)[1] for y in data_df["TeamsRaw"]]
    # (b) Transform date
    data_df["Date"] = [re.split(', ',y)[1] for y in data_df["DateRaw"]]
    # (c) Split score
    data_df["Score_home"] = [re.split(':',y)[0][-2:] for y in data_df["ScoreRaw"]]
    data_df["Score_away"] = [re.split(':',y)[1][:2] for y in data_df["ScoreRaw"]]
    # (e) Set season column
    data_df["Season"] = SEASON
    # Finally we save results
    if not os.path.exists('./{}_FULL'.format(tournament)):
        os.makedirs('./{}_FULL'.format(tournament))
    if not os.path.exists('./{}'.format(tournament)):
        os.makedirs('./{}'.format(tournament))

    data_df.to_csv('./{}_FULL/{}_{}_FULL.csv'.format(tournament,tournament, SEASON), sep=';', encoding='utf-8', index=False)
    data_df[['Home_id', 'Away_id', 'Bookmaker', 'OddHome','OddDraw', 'OddAway', 'Date', 'Score_home', 'Score_away','Season']].to_csv('./{}/{}_{}.csv'.\
        format(tournament,tournament, SEASON), sep=';', encoding='utf-8', index=False)

    return(data_df)

def scrape_current_season_typeC(tournament, sport, country, SEASON, max_page = 25):
    global driver
    ############### NOW WE SEEK TO SCRAPE THE ODDS AND MATCH INFO################################
    DATA_ALL = []
    for page in range(1, max_page + 1):
        print('We start to scrape the page n°{}'.format(page))
        try:
            driver.quit() # close all widows
        except:
            pass

 
        driver = webdriver.Chrome()
        data = scrape_page_current_season_typeC(page, sport, country, tournament)
        DATA_ALL = DATA_ALL + [y for y in data if y != None]
        driver.close()
    data_df = pd.DataFrame(DATA_ALL)
    try:
        data_df.columns = ['TeamsRaw', 'Bookmaker', 'OddHome','OddDraw', 'OddAway', 'DateRaw' ,'ScoreRaw']
    except:
        print('Function crashed, probable reason : no games scraped (empty season)')
        return(1)
    ##################### FINALLY WE CLEAN THE DATA AND SAVE IT ##########################
    '''Now we simply need to split team names, transform date, split score'''

    # (0) Filter out None rows
    data_df = data_df[~data_df['Bookmaker'].isnull()].dropna().reset_index()
    data_df["TO_KEEP"] = 1
    for i in range(len(data_df["TO_KEEP"])):
        if len(re.split(':',data_df["ScoreRaw"][i]))<2 :
            data_df["TO_KEEP"].iloc[i] = 0

    data_df = data_df[data_df["TO_KEEP"] == 1]
    # (a) Split team names
    data_df["Home_id"] = [re.split(' - ',y)[0] for y in data_df["TeamsRaw"]]
    data_df["Away_id"] = [re.split(' - ',y)[1] for y in data_df["TeamsRaw"]]
    # (b) Transform date
    data_df["Date"] = [re.split(', ',y)[1] for y in data_df["DateRaw"]]
    # (c) Split score
    data_df["Score_home"] = [re.split(':',y)[0][-2:] for y in data_df["ScoreRaw"]]
    data_df["Score_away"] = [re.split(':',y)[1][:2] for y in data_df["ScoreRaw"]]
    # (e) Set season column
    data_df["Season"] = SEASON
    # Finally we save results
    if not os.path.exists('./{}_FULL'.format(tournament)):
        os.makedirs('./{}_FULL'.format(tournament))
    if not os.path.exists('./{}'.format(tournament)):
        os.makedirs('./{}'.format(tournament))

    data_df.to_csv('./{}_FULL/{}_CurrentSeason_FULL.csv'.format(tournament,tournament), sep=';', encoding='utf-8', index=False)
    data_df[['Home_id', 'Away_id', 'Bookmaker', 'OddHome','OddDraw', 'OddAway', 'Date', 'Score_home', 'Score_away','Season']].\
        to_csv('./{}/{}_CurrentSeason.csv'.format(tournament,tournament), sep=';', encoding='utf-8', index=False)
    return(data_df)
    
def scrape_league_typeC(Season, sport, country1, tournament1, nseason, current_season = 'yes', max_page = 25):
    long_season = (len(Season) > 6) # indicates whether Season is in format '2010-2011' or '2011' depends on the league) 
    Season = int(Season[0:4])
    for i in range(nseason):
        SEASON1 = '{}'.format(Season)
        if long_season:
          SEASON1 = '{}-{}'.format(Season, Season+1)
        print('We start to collect season {}'.format(SEASON1))
        scrape_current_tournament_typeC(sport = sport, tournament = tournament1, country = country1, SEASON = SEASON1, max_page = max_page)
        print('We finished to collect season {} !'.format(SEASON1))
        Season+=1

    if current_season == 'yes' : 
        SEASON1 = '{}'.format(Season)
        if long_season:
          SEASON1 = '{}-{}'.format(Season, Season+1)
        print('We start to collect current season')
        scrape_current_season_typeC(tournament = tournament1, sport = sport, country = country1, SEASON = 'CurrentSeason', max_page = max_page)
        print('We finished to collect current season !')

    # Finally we merge all files
    file1 = pd.read_csv('./{}/'.format(tournament1) + os.listdir('./{}/'.format(tournament1))[0], sep=';')
    print(os.listdir('./{}/'.format(tournament1))[0])
    for filename in os.listdir('./{}/'.format(tournament1))[1:]:
        file = pd.read_csv('./{}/'.format(tournament1) + filename, sep=';')
        print(filename)
        file1 = file1.append(file)

    file1 = file1.reset_index()

    #Correct falsly collected data for away (in case of 1X2 instead of H/A odds)
    return(file1)
    

def scrape_next_games_typeC(tournament, sport, country, SEASON, nmax = 30):
    global driver
    ############### NOW WE SEEK TO SCRAPE THE ODDS AND MATCH INFO################################
    DATA_ALL = []
    try:
        driver.quit() # close all widows
    except:
        pass

 
    driver = webdriver.Chrome()
    data = scrape_page_next_games_typeC(country, sport, tournament, nmax)
    DATA_ALL = DATA_ALL + [y for y in data if y != None]
    driver.close()

    data_df = pd.DataFrame(DATA_ALL)
  
    try:
        data_df.columns = ['TeamsRaw', 'Bookmaker', 'OddHome','OddDraw', 'OddAway', 'DateRaw', 'ScoreRaw']
    except:
        print('Function crashed, probable reason : no games scraped (empty season)')
        return(1)

    data_df["ScoreRaw"] = '0:0'
    ##################### FINALLY WE CLEAN THE DATA AND SAVE IT ##########################
    '''Now we simply need to split team names, transform date, split score'''

    # (0) Filter out None rows
    data_df = data_df[~data_df['Bookmaker'].isnull()].dropna().reset_index()
    data_df["TO_KEEP"] = 1
    for i in range(len(data_df["TO_KEEP"])):
        if len(re.split(':',data_df["ScoreRaw"][i]))<2 :
            data_df["TO_KEEP"].iloc[i] = 0

    data_df = data_df[data_df["TO_KEEP"] == 1]

    # (a) Split team names
    data_df["Home_id"] = [re.split(' - ',y)[0] for y in data_df["TeamsRaw"]]
    data_df["Away_id"] = [re.split(' - ',y)[1] for y in data_df["TeamsRaw"]]

    # (b) Transform date
    data_df["Date"] = [re.split(', ',y)[1] for y in data_df["DateRaw"]]

    # (c) Split score
    data_df["Score_home"] = 0
    data_df["Score_away"] = 0

    # (d) Set season column
    data_df["Season"] = SEASON


    # Finally we save results
    if not os.path.exists('./{}'.format(tournament)):
        os.makedirs('./{}'.format(tournament))
    data_df[['Home_id', 'Away_id', 'Bookmaker', 'OddHome','OddDraw', 'OddAway', 'Date', 'Score_home', 'Score_away','Season']].to_csv('./{}/NextGames_{}_{}.csv'.format(tournament,tournament, SEASON), sep=';', encoding='utf-8', index=False)


    return(data_df)


def get_data_typeD(i, link):
    driver.get(link)
    reject_ads()
    target = '//*[@id="tournamentTable"]/tbody/tr[{}]/td[2]/a'.format(i)
    a = ffi2(target)
    if a == True:
        print('We wait 4 seconds')
        L = []
        time.sleep(4)
        a = ffi2('//*[@id="bettype-tabs"]/ul/li[3]') # click on home/away odds
        if a == True :
            # Now we collect all bookmaker
            for j in range(1,15): # only first 10 bookmakers displayed
                Book = ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[1]/div/a[2]'.format(j)) # first bookmaker name
                Odd_1 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[2]/div'.format(j)) # first home odd
                Odd_2 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[3]/div'.format(j)) # first away odd
                match = ffi('//*[@id="col-content"]/h1') # match teams
                final_score = ffi('//*[@id="event-status"]')
                date = ffi('//*[@id="col-content"]/p[1]') # Date and time
                print(match, Book, Odd_1, Odd_2, date, final_score, i, '/ 500 ')
                L = L + [(match, Book, Odd_1, Odd_2, date, final_score)]

            for j in range(1,15): # only first 10 bookmakers displayed
                Book = ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[1]/div/a[2]'.format(j)) # first bookmaker name
                Odd_1 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[2]'.format(j)) # first home odd
                Odd_2 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[3]'.format(j)) # first away odd
                match = ffi('//*[@id="col-content"]/h1') # match teams
                final_score = ffi('//*[@id="event-status"]')
                date = ffi('//*[@id="col-content"]/p[1]') # Date and time
                print(match, Book, Odd_1, Odd_2, date, final_score, i, '/ 500 ')
                L = L + [(match, Book, Odd_1, Odd_2, date, final_score)]

            return(L)

    return(None)
    
def get_data_next_games_typeD(i, link):
    driver.get(link)
    reject_ads()
    L = []
    target = '//*[@id="tournamentTable"]/tbody/tr[{}]/td[2]/a'.format(i)
    a = ffi2(target)
    if a == True:
        print('We wait 4 seconds')
        L = []
        time.sleep(4)
        a = ffi2('//*[@id="bettype-tabs"]/ul/li[3]') # click on home/away odds
        if a == True :
            # Now we collect all bookmaker
            for j in range(1,30): # only first 10 bookmakers displayed
                Book = ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[1]/div/a[2]'.format(j)) # first bookmaker name
                Odd_1 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[2]/div'.format(j)) # first home odd
                Odd_2 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[3]/div'.format(j)) # first away odd
                match = ffi('//*[@id="col-content"]/h1') # match teams
                final_score = ffi('//*[@id="event-status"]')
                date = ffi('//*[@id="col-content"]/p[1]') # Date and time
                print(match, Book, Odd_1, Odd_2, date, final_score, i, '/ 500 ')
                L = L + [(match, Book, Odd_1, Odd_2, date, final_score)]
                
    target = '//*[@id="tournamentTable"]/tbody/tr[{}]/td[2]/a[2]'.format(i)
    a = ffi2(target)
    if a == True:
        print('We wait 4 seconds')
        L = []
        time.sleep(4)
        a = ffi2('//*[@id="bettype-tabs"]/ul/li[3]') # click on home/away odds
        if a == True :
            # Now we collect all bookmaker
            for j in range(1,30): # only first 10 bookmakers displayed
                Book = ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[1]/div/a[2]'.format(j)) # first bookmaker name
                Odd_1 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[2]/div'.format(j)) # first home odd
                Odd_2 = fffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr[{}]/td[3]/div'.format(j)) # first away odd
                match = ffi('//*[@id="col-content"]/h1') # match teams
                final_score = ffi('//*[@id="event-status"]')
                date = ffi('//*[@id="col-content"]/p[1]') # Date and time
                print(match, Book, Odd_1, Odd_2, date, final_score, i, '/ 500 ')
                L = L + [(match, Book, Odd_1, Odd_2, date, final_score)]
                
    return(L)
    

def scrape_page_typeD(page, sport, country, tournament, SEASON):
    link = 'https://www.oddsportal.com/{}/{}/{}-{}/results/page/1/#/page/{}'.format(sport,country,tournament,SEASON,page)
    DATA = []
    for i in range(1,100):
        content = get_data_typeD(i, link)
        if content != None:
            DATA = DATA + content
    print(DATA)
    return(DATA)

def scrape_page_current_season_typeD(page, sport, country, tournament):
    link = 'https://www.oddsportal.com/{}/{}/{}/results/page/1/#/page/{}'.format(sport,country,tournament,page)
    DATA = []
    for i in range(1,100):
        content = get_data_typeD(i, link)
        if content != None:
            DATA = DATA + content
    print(DATA)
    return(DATA)

def scrape_current_tournament_typeD(sport, tournament, country, SEASON, max_page = 25):
    global driver
    
    DATA_ALL = []
    for page in range(1, max_page + 1):
        print('We start to scrape the page n°{}'.format(page))
        try:
            driver.quit() # close all widows
        except:
            pass

 
        driver = webdriver.Chrome()
        data = scrape_page_typeD(page, sport, country, tournament, SEASON)
        DATA_ALL = DATA_ALL + [y for y in data if y != None]
        driver.close()

    data_df = pd.DataFrame(DATA_ALL)
    try:
        data_df.columns = ['TeamsRaw', 'Bookmaker', 'OddHome', 'OddAway', 'DateRaw' ,'ScoreRaw']
    except:
        print('Function crashed, probable reason : no games scraped (empty season)')
        return(1)
    ##################### FINALLY WE CLEAN THE DATA AND SAVE IT ##########################
    '''Now we simply need to split team names, transform date, split score'''

    # (0) Filter out None rows
    data_df = data_df[~data_df['Bookmaker'].isnull()].dropna().reset_index()
    data_df["TO_KEEP"] = 1
    for i in range(len(data_df["TO_KEEP"])):
        if len(re.split(':',data_df["ScoreRaw"][i]))<2 :
            data_df["TO_KEEP"].iloc[i] = 0

    data_df = data_df[data_df["TO_KEEP"] == 1]
    # (a) Split team names
    data_df["Home_id"] = [re.split(' - ',y)[0] for y in data_df["TeamsRaw"]]
    data_df["Away_id"] = [re.split(' - ',y)[1] for y in data_df["TeamsRaw"]]
    # (b) Transform date
    data_df["Date"] = [re.split(', ',y)[1] for y in data_df["DateRaw"]]
    # (c) Split score
    data_df["Score_home"] = [re.split(':',y)[0][-1:] for y in data_df["ScoreRaw"]]
    data_df["Score_away"] = [re.split(':',y)[1][:1] for y in data_df["ScoreRaw"]]
    # (e) Set season column
    data_df["Season"] = SEASON
    if not os.path.exists('./{}'.format(tournament)):
        os.makedirs('./{}'.format(tournament))
    data_df[['Home_id', 'Away_id', 'Bookmaker', 'OddHome', 'OddAway', 'Date', 'Score_home', 'Score_away','Season']].\
    to_csv('./{}/{}_{}_08042020.csv'.format(tournament,tournament, SEASON), sep=';', encoding='utf-8', index=False)
    return(data_df)
    
def scrape_page_next_games_typeD(country, sport, tournament, nmax = 20):
  link = 'https://www.oddsportal.com/{}/{}/{}/'.format(sport, country,tournament)
  DATA = []
  for i in range(1,nmax):
    print(i)
    content = get_data_next_games_typeD(i, link)
    if content != None:
        DATA = DATA + content
  print(DATA)
  return(DATA)



def scrape_current_season_typeD(tournament, sport, country, SEASON, max_page = 25):
    global driver

    ############### NOW WE SEEK TO SCRAPE THE ODDS AND MATCH INFO################################
    DATA_ALL = []
    for page in range(1, max_page + 1):
        print('We start to scrape the page n°{}'.format(page))
        
        try:
            driver.quit() # close all widows
        except:
            pass

 
        driver = webdriver.Chrome()
        data = scrape_page_current_season_typeD(page, sport, country, tournament)
        DATA_ALL = DATA_ALL + [y for y in data if y != None]
        driver.close()

    data_df = pd.DataFrame(DATA_ALL)
    try:
        data_df.columns = ['TeamsRaw', 'Bookmaker', 'OddHome', 'OddAway', 'DateRaw' ,'ScoreRaw']
    except:
        print('Function crashed, probable reason : no games scraped (empty season)')
        return(1)    
    ##################### FINALLY WE CLEAN THE DATA AND SAVE IT ##########################
    '''Now we simply need to split team names, transform date, split score'''

    # (0) Filter out None rows
    data_df = data_df[~data_df['Bookmaker'].isnull()].dropna().reset_index()
    data_df["TO_KEEP"] = 1
    for i in range(len(data_df["TO_KEEP"])):
        if len(re.split(':',data_df["ScoreRaw"][i]))<2 :
            data_df["TO_KEEP"].iloc[i] = 0
    data_df = data_df[data_df["TO_KEEP"] == 1]
    # (a) Split team names
    data_df["Home_id"] = [re.split(' - ',y)[0] for y in data_df["TeamsRaw"]]
    data_df["Away_id"] = [re.split(' - ',y)[1] for y in data_df["TeamsRaw"]]
    # (b) Transform date
    data_df["Date"] = [re.split(', ',y)[1] for y in data_df["DateRaw"]]
    # (c) Split score
    data_df["Score_home"] = [re.split(':',y)[0][-1:] for y in data_df["ScoreRaw"]]
    data_df["Score_away"] = [re.split(':',y)[1][:1] for y in data_df["ScoreRaw"]]
    # (e) Set season column
    data_df["Season"] = SEASON
    # Finally we save results
    if not os.path.exists('./{}'.format(tournament)):
        os.makedirs('./{}'.format(tournament))

    data_df[['Home_id', 'Away_id', 'Bookmaker', 'OddHome', 'OddAway', 'Date', 'Score_home', 'Score_away','Season']].\
    to_csv('./{}/{}_CurrentSeason_08042020.csv'.format(tournament,tournament), sep=';', encoding='utf-8', index=False)
    # 

    return(data_df)

def scrape_next_games_typeD(tournament, sport, country, SEASON, nmax = 30):
    global driver
    ############### NOW WE SEEK TO SCRAPE THE ODDS AND MATCH INFO################################
    DATA_ALL = []
    
    try:
        driver.quit() # close all widows
    except:
        pass

 
    driver = webdriver.Chrome()
    data = scrape_page_next_games_typeD(country, sport, tournament, nmax)
    DATA_ALL = DATA_ALL + [y for y in data if y != None]
    driver.close()

    data_df = pd.DataFrame(DATA_ALL)
    try:
        data_df.columns = ['TeamsRaw', 'Bookmaker', 'OddHome', 'OddAway', 'DateRaw', 'ScoreRaw']
    except:
        print('Function crashed, probable reason : no games scraped (empty season)')
        return(1)

    data_df["ScoreRaw"] = '0:0'
    ##################### FINALLY WE CLEAN THE DATA AND SAVE IT ##########################
    '''Now we simply need to split team names, transform date, split score'''

    # (0) Filter out None rows
    data_df = data_df[~data_df['Bookmaker'].isnull()].dropna().reset_index()
    data_df["TO_KEEP"] = 1
    for i in range(len(data_df["TO_KEEP"])):
        if len(re.split(':',data_df["ScoreRaw"][i]))<2 :
            data_df["TO_KEEP"].iloc[i] = 0

    data_df = data_df[data_df["TO_KEEP"] == 1]

    # (a) Split team names
    data_df["Home_id"] = [re.split(' - ',y)[0] for y in data_df["TeamsRaw"]]
    data_df["Away_id"] = [re.split(' - ',y)[1] for y in data_df["TeamsRaw"]]

    # (b) Transform date
    data_df["Date"] = [re.split(', ',y)[1] for y in data_df["DateRaw"]]

    # (c) Split score
    data_df["Score_home"] = 0
    data_df["Score_away"] = 0

    # (d) Set season column
    data_df["Season"] = SEASON


    # Finally we save results
    if not os.path.exists('./{}'.format(tournament)):
        os.makedirs('./{}'.format(tournament))
    data_df[['Home_id', 'Away_id', 'Bookmaker', 'OddHome', 'OddAway', 'Date', 'Score_home', 'Score_away','Season']].to_csv('./{}/NextGames_{}_{}_08042020.csv'.format(tournament,tournament, SEASON), sep=';', encoding='utf-8', index=False)


    return(data_df)



def scrape_league_typeD(Season, sport, country1, tournament1, nseason, current_season = 'yes', max_page = 25):
    long_season = (len(Season) > 6) # indicates whether Season is in format '2010-2011' or '2011' depends on the league) 
    Season = int(Season[0:4])
    for i in range(nseason):
        SEASON1 = '{}'.format(Season)
        if long_season:
            SEASON1 = '{}-{}'.format(Season, Season+1)
        print('We start to collect season {}'.format(SEASON1))
        scrape_current_tournament_typeD(sport = sport, tournament = tournament1, country = country1, SEASON = SEASON1, max_page = max_page)
        print('We finished to collect season {} !'.format(SEASON1))
        Season+=1

    if current_season == 'yes' : 
        SEASON1 = '{}'.format(Season)
        if long_season:
            SEASON1 = '{}-{}'.format(Season, Season+1)
        print('We start to collect current season')
        scrape_current_season_typeD(sport = sport, tournament = tournament1, country = country1, SEASON = 'CurrentSeason', max_page = max_page)
        print('We finished to collect current season !')


    # Finally we merge all files
    file1 = pd.read_csv('./{}/'.format(tournament1) + os.listdir('./{}/'.format(tournament1))[0], sep=';')
    print(os.listdir('./{}/'.format(tournament1))[0])
    for filename in os.listdir('./{}/'.format(tournament1))[1:]:
        file = pd.read_csv('./{}/'.format(tournament1) + filename, sep=';')
        print(filename)
        file1 = file1.append(file)

    file1 = file1.reset_index()

    #Correct falsly collected data for away (in case of 1X2 instead of H/A odds)
    for i in range(file1.shape[0]):
        if (1/file1["OddHome"].iloc[i] + 1/file1["OddAway"].iloc[i]) < 1 :
            file1["OddAway"].iloc[i] = 1 / ((1 - 1/file1["OddHome"].iloc[i])*1.07) #  1/1.07 = 0.934 => 6.5 % margin (estimation)
            print(file1["OddHome"].iloc[i], file1["OddAway"].iloc[i], i)
    file1.to_csv("./{}/All_data_{}.csv".format(tournament1, tournament1))

    print('All good! ')
    return(file1)


def scrape_oddsportal_current_season(sport = 'football', country = 'france', league = 'ligue-1', season = '2019-2020', max_page = 25):
  ''' sport : sport as mentioned on the oddsportal website 
      country : country as mentioned on oddsportal website 
      league : league as mentioned on oddsportal website
      season : season that you want in the column Season in the csv'''
  L = ['soccer', 'basketball', 'esports', 'darts', 'tennis', 'baseball', 'rugby-union', 'rugby-league', 'american-football', 'hockey', 'volleyball', 'handball']
  
  while sport not in L :
    sport = input('Please choose a sport among the following list : \n {} \n'.format(L))

  if sport == 'tennis' :
    bestof = input('Please indicate the format of tournament (3 sets or 5 sets) : \n ')
    surface = input('Please indicate the surface : \n ')
    
  if sport in ['baseball','esports','basketball','darts', 'american-football', 'volleyball']:
    df = scrape_current_season_typeA(tournament = league, sport = sport, country = country, SEASON = season, max_page = max_page)
    df = create_clean_table_two_ways(df)
  elif sport in ['tennis']:
    df = scrape_current_tournament_typeB(Surface = surface, bestof = bestof, tournament = league, \
        country = country, name_to_write = league, SEASON = season, max_page = 25)
    df = create_clean_table_two_ways(df)
  elif sport in ['soccer', 'rugby-union', 'rugby-league', 'handball']:
    df = scrape_current_season_typeC(tournament = league, sport = sport, country = country, SEASON = season, max_page = max_page)
    df = create_clean_table_three_ways(df)
  elif sport in ['hockey']:
    df = scrape_current_season_typeD(tournament = league, sport = sport, country = country, SEASON = season, max_page = max_page)
    df = create_clean_table_two_ways(df)
    
    
  if not os.path.exists('./{}'.format(sport)):
        os.makedirs('./{}'.format(sport))

  df.to_csv('./{}/CurrentSeason_{}_{}_{}.csv'.format(sport, country, league, season), sep=',', encoding='utf-8', index=False)
  
  
def scrape_oddsportal_historical(sport = 'football', country = 'france', league = 'ligue-1', start_season = '2019-2020', nseasons = 1, current_season = 'yes', max_page = 25):
  ''' sport : sport as mentioned on the oddsportal website 
      country : country as mentioned on oddsportal website 
      league : league as mentioned on oddsportal website
      start_season : starting season as mentioned in the oddsportal website
      nseasons = number of seasons to scrape from the starting season (do not include current season!)
      current_season : do you want to scrape current season aswell ? '''
  L = ['soccer', 'basketball', 'esports', 'darts', 'tennis', 'baseball', 'rugby-union', 'rugby-league', 'american-football', 'hockey', 'volleyball', 'handball']
  
  while sport not in L :
    sport = input('Please choose a sport among the following list : \n {} \n'.format(L))

  if sport == 'tennis' :
    bestof = input('Please indicate the format of tournament (3 sets or 5 sets) : \n ')
    surface = input('Please indicate the surface : \n ')
    
  if sport in ['baseball','esports','basketball','darts', 'american-football', 'volleyball']:
    df = scrape_league_typeA(Season = start_season, sport = sport, country1 = country, tournament1 = league, nseason = nseasons, current_season = 'yes', max_page = max_page)
    df = create_clean_table_two_ways(df)
  #elif sport in ['tennis']:
    #df = scrape_league_typeB(Surface = surface, bestof = bestof, Season = start_season, country1 = country, tournament1 = league, nseason = nseasons)
    #df = create_clean_table_two_ways(df)
  elif sport in ['soccer', 'rugby-union', 'rugby-league', 'handball']:
    df = scrape_league_typeC(Season = start_season, sport = sport, country1 = country, tournament1 = league, nseason = nseasons, current_season = 'yes', max_page = max_page)
    df = create_clean_table_three_ways(df)
  elif sport in ['hockey']:
    df = scrape_league_typeD(Season = start_season, sport = sport, country1 = country, tournament1 = league, nseason = nseasons, current_season = 'yes', max_page = max_page)
    df = create_clean_table_two_ways(df)
    
    
  if not os.path.exists('./{}'.format(sport)):
        os.makedirs('./{}'.format(sport))

  df.to_csv('./{}/Historical_{}_{}.csv'.format(sport, country, league), sep=',', encoding='utf-8', index=False)
  
  
def scrape_oddsportal_next_games(sport = 'football', country = 'france', league = 'ligue-1', season = '2019-2020', nmax = 30):
  ''' sport : sport as mentioned on the oddsportal website 
      country : country as mentioned on oddsportal website 
      league : league as mentioned on oddsportal website
      season : season that you want in the column Season in the csv
      nmax : how many links do you want to try - usually nmax = 4*number of games we want to scrape'''
  L = ['soccer', 'basketball', 'esports', 'darts', 'tennis', 'baseball', 'rugby-union', 'rugby-league', 'american-football', 'hockey', 'volleyball', 'handball']
  
  while sport not in L :
    sport = input('Please choose a sport among the following list : \n {} \n'.format(L))

  if sport == 'tennis' :
    bestof = input('Please indicate the format of tournament (3 sets or 5 sets) : \n ')
    surface = input('Please indicate the surface : \n ')
    
  if sport in ['baseball','esports','basketball','darts', 'american-football', 'volleyball']:
    df = scrape_next_games_typeA(tournament = league, sport = sport, country = country, SEASON = season, nmax = nmax)
    df = create_clean_table_two_ways(df)
  elif sport in ['tennis']:
    df = scrape_next_games_typeB(Surface = surface, bestof = bestof, tournament = league , country = country , name_to_write = league, SEASON = '2020')
    df = create_clean_table_two_ways(df)
  elif sport in ['soccer', 'rugby-union', 'rugby-league', 'handball']:
    df = scrape_next_games_typeC(tournament = league, sport = sport, country = country, SEASON = season, nmax = nmax)
    df = create_clean_table_three_ways(df)
  elif sport in ['hockey']:
    df = scrape_next_games_typeD(tournament = league, sport = sport, country = country, SEASON = season, nmax = nmax)
    df = create_clean_table_two_ways(df)
    
    
  if not os.path.exists('./{}'.format(sport)):
        os.makedirs('./{}'.format(sport))

  df.to_csv('./{}/NextGames_{}_{}_{}.csv'.format(sport, country, league, season), sep=',', encoding='utf-8', index=False)


def scrape_oddsportal_specific_season(sport = 'football', country = 'france', league = 'ligue-1', season = '2019-2020', max_page = 25):
  ''' sport : sport as mentioned on the oddsportal website 
      country : country as mentioned on oddsportal website 
      league : league as mentioned on oddsportal website
      season : season that you want in the column Season in the csv
      max_page = how many pages do you want to scrape for this season?'''
  L = ['soccer', 'basketball', 'esports', 'darts', 'tennis', 'baseball', 'rugby-union', 'rugby-league', 'american-football', 'hockey', 'volleyball', 'handball']
  
  while sport not in L :
    sport = input('Please choose a sport among the following list : \n {} \n'.format(L))

  if sport == 'tennis' :
    bestof = input('Please indicate the format of tournament (3 sets or 5 sets) : \n ')
    surface = input('Please indicate the surface : \n ')
    
  if sport in ['baseball','esports','basketball','darts', 'american-football', 'volleyball']:
    df = scrape_current_tournament_typeA(sport = sport, tournament = league, country = country, SEASON = season, max_page = max_page)
    df = create_clean_table_two_ways(df)
  #elif sport in ['tennis']:
    #df = scrape_current_tournament_typeB(Surface = surface, bestof = bestof, tournament = league, country = country,\
         #name_to_write = league, SEASON = season)
    #df = create_clean_table_two_ways(df)
  elif sport in ['soccer', 'rugby-union', 'rugby-league', 'handball']:
    df = scrape_current_tournament_typeC(sport = sport, tournament = league, country = country, SEASON = season, max_page = max_page)
    df = create_clean_table_three_ways(df)
  elif sport in ['hockey']:
    df = scrape_current_tournament_typeD(sport = sport, tournament = league, country = country, SEASON = season, max_page = max_page)
    df = create_clean_table_two_ways(df)
    
    
  if not os.path.exists('./{}'.format(sport)):
        os.makedirs('./{}'.format(sport))

  df.to_csv('./{}/Season_{}_{}_{}.csv'.format(sport, country, league, season), sep=',', encoding='utf-8', index=False)
  
  
  
def reject_ads(switch_to_decimal = True):
    # Reject ads
    ffi2('//*[@id="onetrust-reject-all-handler"]')
    
    if switch_to_decimal:
        # Change odds to decimal format
        driver.find_element("xpath", '//*[@id="user-header-oddsformat-expander"]').click()
        driver.find_element("xpath", '//*[@id="user-header-oddsformat"]/li[1]/a/span').click()

#scrape_oddsportal_current_season(sport = 'soccer', country = 'england', league = 'championship', season = '2022',max_page = 25)
#scrape_oddsportal_current_season(sport = 'soccer', country = 'finland', league = 'veikkausliiga', season = '2020', max_page = 25)
scrape_oddsportal_specific_season(sport = 'soccer', country = 'finland', league = 'veikkausliiga', season = '2019', max_page = 25)
#scrape_oddsportal_next_games(sport = 'tennis', country = 'germany', league = 'exhibition-bett1-aces-berlin-women', season = '2020')

