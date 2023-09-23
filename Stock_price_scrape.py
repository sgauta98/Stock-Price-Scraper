import requests
import yfinance as yf
import tkinter as tk
import customtkinter as ctk
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

#recieve input for stock ticker name
ticker_name = input("Please enter the stock ticker name: ")

#Convert ticker name to comapny name for output
try:
    ticker_var = yf.Ticker(str(ticker_name))
    company_name = ticker_var.info['longName']
except:
    print("That is an invalid ticker symbol")

# Define the Yahoo Finance URL that can be modified
base_url = 'https://finance.yahoo.com/quote/'
#parse url to identify netloc and path and isolate path in order to modify ticker name
parsed_url = urlparse(base_url)

new_path = '/quote/' + ticker_name
parsed_url = parsed_url._replace(path = new_path)

modified_url = urlunparse(parsed_url)

#define tk window 
window = ctk.CTk()
window.geometry('600x250')
window.title('Stock Price Scraper')
#change window appearance
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')
custom_font = ('Georgia', 16)

# Send an HTTP GET request to the URL
response = requests.get(modified_url, headers = headers)

# Check if the request was successful

if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Locate the element containing the stock price, it is td in yahoo finance upon looking at HTML of page
    price_element = soup.find('td', {'data-test': 'OPEN-value'})
    
    # Extract the stock price text otherwise give the errors
    if price_element:
        stock_price = price_element.text
        value_label = tk.Label(window, text = (f'The current {company_name} stock price is ${stock_price}'), bg = 'lightblue', font = custom_font)
        value_label.pack()
        window.mainloop()
    else:
        print('Stock price not found on the page.')
else:
    print('Failed to retrieve the web page. Status code:', response.status_code)


