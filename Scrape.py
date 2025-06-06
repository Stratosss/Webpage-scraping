import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import sys

url = 'https://www.scrapethissite.com/pages/forms/'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

column_titles = ['.name', '.year', '.wins', '.losses', '.pct','.gf', '.ga']
columns = []

#string makeover
def construction_function(column):
    col = soup.select(column)
    col_list = []
    for i in range(len(col)):
        temp_column = col[i].getText().strip() #gets the text between <td class="name"> and </td> and strips/ removes the spaces before and after word
        col_list.append(temp_column)
    return col_list
   
    
def results(param):
    while True:
            x = input("What do you wish to do? Press 1 for: Print all data or press 2 for: Print the teams that have a win rate >50%? (Quit with q): ")
            if x == "1":
                df = pd.DataFrame({
                                    "Team Name" : param[0], 
                                    "Year" : param[1], 
                                    "Wins" : param[2],
                                    "Losses": param[3], 
                                    "Win %" : param[4], 
                                    "Goals for" : param[5], 
                                    "Goals against" : param[6]})
                return df
                
            elif x == "2":
                total= np.column_stack([param[0], param[4]])      
                headers = ["Team Name", "Win %"]

                rows = total.shape[0]
                cols = total.shape[1]     
                arr =[]
                for i in range(rows):
                    for j in range(cols):
                        if float(total[i,1]) > 0.5:
                                arr = np.append(arr, total[i,j])
                
                arr = arr.reshape(-1, 2) # -1: automatically calculates rows based on: total/requested columns

                df = pd.DataFrame(arr, columns=headers)
                return df
                
            elif x.strip().lower() == "q":
                sys.exit()
            else:
                print("Please select: 1 or 2 for printouts, or q for exit")
      
if __name__=="__main__":
    for i in range(len(column_titles)):
        columns.append(construction_function(column_titles[i]))
    print(results(columns))
