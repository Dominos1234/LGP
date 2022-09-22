import pandas as pd
import openpyxl
import re


dataframe = pd.read_excel('Czas.xlsx')
for czas in dataframe["Czas"]:

    czasy = re.sub("[A-zŚłą ]", "", czas)
    czasy = czasy.split(",")
    print(czasy)

