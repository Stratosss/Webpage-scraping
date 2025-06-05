import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import sys

url = 'https://www.scrapethissite.com/pages/forms/'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

categories = ['.name', '.pct', '.year', '.wins', '.losses', '.gf', '.ga']


#string makeover
def construction_function(param):
    columns = soup.select(param)
    column_list = []
    for i in range(len(columns)):
        temp_column = columns[i].getText().strip() #gets the text between <td class="name"> and </td> and strips/ removes the spaces before and after word
        column_list.append(temp_column)
    return column_list
    
    
def results(param):
    while True:
            x = input("What do you wish to do? Press 1 for: Print all data or press 2 for: Print the teams that have a win rate >50%? (Quit with q): ")
            if x == "1":
                df = pd.DataFrame({
                                    "Team Name" : categories[0], 
                                    "Year" : categories[1], 
                                    "Wins" : categories[2],
                                    "Losses": categories[3], 
                                    "Win %" : categories[4], 
                                    "Goals for" : categories[5], 
                                    "Goals against" :categories[6]})
                return df
                
            elif x == "2":
                total= np.column_stack([categories[0], categories[1]])      #attempt to combine numpy and pandas
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
                return df
                
            elif x.strip().lower() == "q":
                sys.exit()
            else:
                print("Please select: 1 or 2 for printouts, or q for exit")
                
if __name__=="__main__":                   
    for i in range(len(categories)):
        categories[i]= construction_function(categories[i])
    print(results(categories))
    
    
    
