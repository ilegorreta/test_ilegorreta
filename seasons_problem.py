# -*- coding: utf-8 -*-
import pandas as pd
from datetime import datetime, date

def season(row):
    day = row.ORD_DT
    today = date.today()
    day_parsed = datetime.strptime(day, "%m/%d/%y").date().replace(year=today.year)
    if day_parsed >= datetime(2021, 3, 19).date() and day_parsed < datetime(2021, 6, 20).date():
        return "Spring"
    elif day_parsed >= datetime(2021, 6, 20).date() and day_parsed < datetime(2021, 9, 22).date():
        return "Summer"
    elif day_parsed >= datetime(2021, 9, 22).date() and day_parsed < datetime(2021, 12, 21).date():
        return "Fall"
    else:
        return "Winter"

def main():
    df = pd.read_csv('datasets/seasons.csv')
    df["Season"] = df.apply(lambda x: season(x), axis=1)
    df = df[['ORD_ID', 'Season']]
    print(df)

if __name__ == "__main__":
    main()