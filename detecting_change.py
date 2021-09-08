# -*- coding: utf-8 -*-
import pandas as pd

def main():
    df = pd.read_csv('datasets/weather.csv')
    flag = None
    bad_weather = []

    for row in df.iterrows():
        if row[1][1] == True and flag == False:
            bad_weather.append([row[1][0], row[1][1]])
            flag = True
        elif row[1][1] == True and flag == True:
            flag = True
        else:
            flag = False
    df = pd.DataFrame(bad_weather, columns = ['date', 'was_rainy'])   
    print(df) 

if __name__ == "__main__":
    main()