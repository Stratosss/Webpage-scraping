import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import sys

url = 'https://www.scrapethissite.com/pages/forms/'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')
list_name = soup.select('.name')
win_rate = soup.select('.pct')
y = soup.select('.year')
w = soup.select('.wins')
l = soup.select('.losses')
goals_f = soup.select('.gf')
goals_a = soup.select('.ga')


#string makeover
name = []
for i in range(len(list_name)):
    temp= list_name[i].getText().strip() #gets the text between <td class="name"> and </td> and strips/ removes the spaces before and after word
    name.append(temp)

win_r = []
for i in range(len(win_rate)):
    temp= win_rate[i].getText().strip()  
    win_r.append(temp)

year = []
for i in range(len(y)):
    temp= y[i].getText().strip()   
    year.append(temp)

wins = []
for i in range(len(w)):
    temp= w[i].getText().strip()   
    wins.append(temp)

losses = []
for i in range(len(l)):
    temp= l[i].getText().strip()   
    losses.append(temp)
    
goals_for = []
for i in range(len(goals_f)):
    temp= goals_f[i].getText().strip()  
    goals_for.append(temp)
    
goals_against = []
for i in range(len(goals_a)):
    temp= goals_a[i].getText().strip()  
    goals_against.append(temp)


while True:
         x = input("What do you want to do? 1) Print all data or 2) Print the teams that have a win rate >50%? (Quit with q): ")
         if x == "1":
            df = pd.DataFrame({
                                "Team Name" : name, 
                                "Year" : year, 
                                "Wins" : wins,
                                "Losses": losses, 
                                "Win %" : win_r, 
                                "Goals for" : goals_for, 
                                "Goals against" :goals_against})
            print(df)
            break
         elif x == "2":
            total= np.column_stack([name, win_r])      #attempt to combine numpy and pandas
            headers = ["Team Name", "Win %"]

            rows = total.shape[0]
            cols = total.shape[1]     
            new_table =[]
            for i in range(rows):
                for j in range(cols):
                    if float(total[i,1]) > 0.5:
                            new_table = np.append(new_table, total[i,j])

            new_table = new_table.reshape(int(new_table.shape[0]/2), 2)

            df = pd.DataFrame(new_table, columns=headers)
            print(df)
            break
         elif x == "q":
            sys.exit()
         else:
            print("Please select: 1 or 2 for printouts, or q for exit")
        
    
    
    
