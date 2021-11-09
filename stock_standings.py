import requests
import datetime

key="xxxx"
print("This program fetches stock data on the equity of your choice during a time period also of your choice:")
choice=input("Enter '1' to access daily data ,'2' to access weekly data and '3' to access monthly data:")
equity=input("Enter your equity of choice eg 'TSLA' for Tesla:\n").upper()



def daily():
    # 1. Daily 
    """returns raw (as-traded) daily time series (date, daily open, daily high, daily low, daily close, daily volume) of the global equity specified,"""
    today=datetime.datetime.now()
    year=today.year
    month=today.month
    date=today.day

    """Because the US stock market is only open on weekdays, if the user checks the stock standings on a weekend, they will be taken back to Friday's date"""
    if today.weekday() == 6:
        date -=2 
    elif today.weekday() == 5:
        date -=1
    elif today.weekday() == 0: # if today is a monday
        date -=3
    else:
        date -=1 #The current day's data is updated on the next day

    if date < 10:
        now=(f"{year}-{month}-0{date}")
    else:
        now=(f"{year}-{month}-{date}")
    intraday_endpoint=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={equity}&interval=5min&apikey={key}"
    response_1=requests.get(url=intraday_endpoint)
    response_1.raise_for_status()
    todays_standings=response_1.json()['Time Series (Daily)'][f'{now}']
    print(todays_standings)



def weekly():
    # 2. Weekly
    """returns weekly adjusted time series (last trading day of each week, weekly open, weekly high, weekly low, weekly close, weekly adjusted close, weekly volume, weekly dividend) of the global equity specified"""

    week =input("Enter friday's date from the week you'd like to view(YYYY-MM-DD):)")
    weekly_endpoint=f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={equity}&apikey={key}"
    response_2=requests.get(url=weekly_endpoint)
    response_2.raise_for_status()
    week_standings=(response_2.json()['Weekly Time Series'][week])
    print(week_standings)



def monthly():
    # 3. Monthly
    """returns monthly adjusted time series (last trading day of each month, monthly open, monthly high, monthly low, monthly close, monthly adjusted close, monthly volume, monthly dividend) of the equity specified"""
    Year=input('Enter year (YYYY):')
    month=input("Enter the month (MM):")

    def leap_year(year):
        if year % 4 == 0:
            if year % 100==0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    if month == '04' or month == '06' or month == '09' or month =='11':
        month_to_check= f"{Year}-{month}-30"
    elif month == '01' or month == '03' or month == '05' or month == '07' or month == '08' or month== '10' or month == '12':
        month_to_check= f"{Year}-{month}-31"
    elif month == '02':
        if leap_year(Year) == True:
            month_to_check= f"{Year}-{month}-29" 
        elif leap_year(Year) == False:
            month_to_check= f"{Year}-{month}-28"

    monthly_endpoint=f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={equity}&apikey={key}"
    response_3=requests.get(url=monthly_endpoint)
    response_3.raise_for_status
    monthly_standing=response_3.json()['Monthly Time Series'][month_to_check]
    print(monthly_standing)



if choice == '1':
    daily()
elif choice == '2':
    weekly()
elif choice == '3':
    monthly()
