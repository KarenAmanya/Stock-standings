# Stock standings program
***
This program fetches stock information from an API and returns the opening,closing,highest and lowest  prices of a particular equity in json format depending on the time series chosen.
***
### How it works:
1. The program will first ask the user which time format they would like to view: available time options are daily, weekly and monthly.The daily series is capable of fetching stock data back upto 4 months from the current date.The weekly upto 2 years  while the monthly series can fetch data back upto 15 years depending on when the particular stock was first listed on the NYSE.

2. After choosing a time series , the user will also input their preffered stock eg TSLA,IBM or AAPL.
3. The program will then input the user specifications into the API endpoint and submit the request form.
4. The response is in the json format with the data consisting of the current,highest,lowest,opening and closing prices of the stock for the particular time period chosen.
***
### Modules used:
1. Requests
2. Datetime