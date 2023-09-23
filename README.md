# Stock-Price-Scraper

This application aims to retrieve real time stock prices listed on yahoo finance. 

Given a ticker symbol input, the application adjusts the url through parsing in order to form the correct url. Additionally, it converts the ticker symbol to the full company name using yfinance to display in the output.

After checking for a successful connection request, the HTML code on the website is parsed with the help of beautiful soup in order to extract the stock price.

The output is displayed in a basic customtkinter window. 

Appropriate error messages are given for non-viable inputs, unlisted stocks or connection errors.

The application uses packages such as pandas, tkinter, urllib, yfinance, requests and beautifulsoup.
