import requests
from bs4 import BeautifulSoup


# url = "https://www.premierleague.com/tables"
# page = requests.get(url)
# soup = BeautifulSoup(page.content, "lxml") # <-- use lxml

# standings = soup.find("div", attrs={"data-ui-tab": "First Team"}).find_all("tr")[1::2]  # <-- get every second <tr>
# # print(standings[0])
# for standing in standings:
#     position = standing.find("span", attrs={"class": "value"}).text.strip()
#     club_name = standing.find("span", {"class": "long"}).text
#     points = standing.find("td", {"class": "points"}).text
#     played = standing.find("span", {'class': 'short'})
#     print(type(standing))
#     print(position, club_name, points, played)

# # import requests
# # standing_url = "https://fbref.com/en/comps/9/Premier-League-Stats"
# # data = requests.get(standing_url)
# # from bs4 import BeautifulSoup
# # soup = BeautifulSoup(data.text,features='lxml')
# # standing_table = soup.select("table.stats_table")[0]
# # links  = standing_table.find_all("a")
# # links = [l.get("href") for l in links]
# # links = [l for l in links if '/squads/' in l]

# # team_urls = [f"https://fbref.com{l}" for l in links]

# # team_url = team_urls[0]
# # data = requests.get(team_url)
import pandas as pd
# # matches = pd.read_html(data.text, match = "Scores & Fixtures")
# # soup = BeautifulSoup(data.text,features='lxml')
# # links = soup.find_all("a")
# # links = [l.get("href") for l in links]
# # links = [l for l in links if l and "all_comps/shooting/" in l]

# # data = requests.get(f"https://fbref.com{links[0]}")
# # shooting = pd.read_html(data.text, match = "Shooting")[0]


# # shooting.columns = shooting.columns.droplevel()


# # team_data = matches[0].merge(shooting[["Date", "Sh", "SoT", "Dist","FK", "PK", "PKatt"]], on = "Date")

years = [2022]

all_matches = []
# standing_url = "https://fbref.com/en/comps/9/Premier-League-Stats"
# import time
# for year in years:
#     data = requests.get(standing_url)
#     soup = BeautifulSoup(data.text,features='lxml')
#     standing_table = soup.select("table.stats_table")[0]

#     links = standing_table.find_all("a")
#     links = [l.get("href") for l in links]
#     links = [l for l in links if '/squads/' in l]
#     team_urls = [f"https://fbref.com{l}" for l in links]
    
#     previous_season = soup.select("a.prev")[0].get("href")
#     standing_url = f"https://fbref.com/{previous_season}"

#     for team_url in team_urls:
#         team_name = team_url.split("/")[-1].replace("-Stats","").replace("-"," ")
        
#         data = requests.get(team_url)
#         matches = pd.read_html(data.text, match = "Scores & Fixtures")[0]
        
#         soup = BeautifulSoup(data.text,features='lxml')
#         links = soup.find_all("a")
#         links = [l.get("href") for l in links]
#         links = [l for l in links if l and "all_comps/shooting/" in l]
#         data = requests.get(f"https://fbref.com{links[0]}")
#         shooting = pd.read_html(data.text, match = "Shooting")[0]
#         shooting.columns = shooting.columns.droplevel()
        
#         try:
#             team_data = matches.merge(shooting[["Date", "Sh", "SoT", "Dist","FK", "PK", "PKatt"]], on = "Date")
#         except ValueError:
#             continue
            
#         team_data = team_data[team_data["Comp"] == "Premier League"]
#         team_data["Season"] = year
#         team_data["Team"] = team_name
#         all_matches.append(team_data)
#         time.sleep(5)
#         print(team_name, year)

     
            
# # team_url.split("/")[-1].replace("-Stats","").replace("-"," ")
# # 'Manchester City'
# match_df = pd.concat(all_matches)
# match_df.columns = [c.lower() for c in match_df.columns]
# # match_df.to_csv("tables.csv")
# print(match_df.head())


# print(match_df.shape)


# url = "https://www.premierleague.com/tables?co=1&se=1&ha=-1"
# page = requests.get(url)
# soup = BeautifulSoup(page.content, "lxml") # <-- use lxml

# standings = soup.find("div", attrs={"data-ui-tab": "First Team"}).find_all("tr")[1::2]  # <-- get every second <tr>

# for standing in standings:
#     position = standing.find("span", attrs={"class": "value"}).text.strip()
#     club_name = standing.find("span", {"class": "long"}).text
#     points = standing.find("td", {"class": "points"}).text
#     print(position, club_name, points)

# exit()
#Works???
# standing_url = "https://fbref.com/en/comps/9/Premier-League-Stats"
# import time
# for year in years:
#     data = requests.get(standing_url)
#     soup = BeautifulSoup(data.text,features='lxml')
#     standing_table = soup.select("table.stats_table")[0]

#     links = standing_table.find_all("a")
#     links = [l.get("href") for l in links]
#     links = [l for l in links if '/squads/' in l]
#     team_urls = [f"https://fbref.com{l}" for l in links]
    
#     previous_season = soup.select("a.prev")[0].get("href")
#     standing_url = f"https://fbref.com/{previous_season}"

#     for team_url in team_urls:
#         team_name = team_url.split("/")[-1].replace("-Stats","").replace("-"," ")
        
#         data = requests.get(team_url)
#         matches = pd.read_html(data.text, match = "Scores & Fixtures")[0]
        
#         soup = BeautifulSoup(data.text,features='lxml')
#         links = soup.find_all("a")
#         links = [l.get("href") for l in links]
#         links = [l for l in links if l and "all_comps/shooting/" in l]
#         data = requests.get(f"https://fbref.com{links[0]}")
#         shooting = pd.read_html(data.text, match = "Shooting")[0]
#         shooting.columns = shooting.columns.droplevel()
        
#         try:
#             team_data = matches.merge(shooting[["Date", "Sh", "SoT", "Dist","FK", "PK", "PKatt"]], on = "Date")
#         except ValueError:
#             continue
            
#         team_data = team_data[team_data["Comp"] == "Premier League"]
#         team_data["Season"] = year
#         team_data["Team"] = team_name
#         all_matches.append(team_data)
#         time.sleep(5)
#         print(team_name, year)

# match_df = pd.concat(all_matches)
# match_df.columns = [c.lower() for c in match_df.columns]
# match_df.to_csv("tables.csv")
# print(match_df.head())


#Adapted/stolen from https://github.com/wmblack23/Live-Soccer-Scraper/blob/main/Live_Football_Scraper.py

# Notebook scrapes fixture data from: https://www.bbc.com/sport/football/scores-fixtures

from datetime import date as mydate
from datetime import datetime as mydatetime
import os, pytz, datetime, re
import time as mytime


def scraping(date):
    
    """
    Web scraping code
    """
    
    url = "https://www.bbc.com/sport/football/scores-fixtures/" + date

    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "html.parser")
        
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

# date = '2023-08-18'
# fixs = final_print(date)
# leeds_fix = [fix for fix in fixs if 'Leeds' in fix][0]
# print(leeds_fix)