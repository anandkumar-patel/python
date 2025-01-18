import yfinance as yf
import matplotlib.pyplot as plt

# download historical data of STOCK>NS
ticker = input("Enter the stock name : ")
data = yf.download(ticker, start="2023-01-01", end="2023-08-08")

# plot the stock chart
plt.figure(figsize=(10, 5))
plt.plot(data["Close"])
plt.title(f"{ticker} Stock Chart")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.show()
