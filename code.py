import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# List of stocks to trade
symbols = ['AAPL', 'MSFT', 'GOOGL', 'TSLA']
initial_cash = 10000
cash_per_stock = initial_cash / len(symbols)  # Divide money equally

print(f"Trading {len(symbols)} stocks with ${cash_per_stock:,.2f} each")
print(f"Total Initial Investment: ${initial_cash:,.2f}\n")

all_portfolios = {}
total_portfolio = []

# Process each stock
for symbol in symbols:
    print(f"\n{'='*50}")
    print(f"Processing {symbol}")
    print('='*50)
    
    # Download stock data
    df = yf.download(symbol, start='2023-01-01', end='2024-01-01', progress=False)
    
    # Calculate moving averages
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    
    # Drop NaN values
    df = df.dropna()
    
    # Trading signals
    df['Signal'] = 0
    df.loc[df['SMA_20'] > df['SMA_50'], 'Signal'] = 1
    df.loc[df['SMA_20'] <= df['SMA_50'], 'Signal'] = -1
    
    # Backtest
    cash = cash_per_stock
    shares = 0
    portfolio_value = []
    
    for i in range(len(df)):
        price = float(df['Close'].iloc[i])
        signal = int(df['Signal'].iloc[i])
        
        # Buy signal
        if signal == 1 and shares == 0:
            shares = cash / price
            cash = 0
            print(f"BUY:  {df.index[i].date()} - Price: ${price:.2f} - Shares: {shares:.2f}")
        
        # Sell signal
        elif signal == -1 and shares > 0:
            cash = shares * price
            print(f"SELL: {df.index[i].date()} - Price: ${price:.2f} - Cash: ${cash:.2f}")
            shares = 0
        
        # Calculate current portfolio value
        current_value = cash + (shares * price)
        portfolio_value.append(current_value)
    
    df['Portfolio'] = portfolio_value
    all_portfolios[symbol] = df
    
    # Results for this stock
    final_value = portfolio_value[-1]
    profit = final_value - cash_per_stock
    profit_pct = (profit / cash_per_stock) * 100
    
    print(f"\n{symbol} Results:")
    print(f"  Starting: ${cash_per_stock:,.2f}")
    print(f"  Ending: ${final_value:,.2f}")
    print(f"  Profit/Loss: ${profit:,.2f} ({profit_pct:.2f}%)")

# Calculate total portfolio (sum of all stocks)
print(f"\n{'='*50}")
print("COMBINED PORTFOLIO RESULTS")
print('='*50)

# Find common dates across all stocks
common_dates = all_portfolios[symbols[0]].index
for symbol in symbols[1:]:
    common_dates = common_dates.intersection(all_portfolios[symbol].index)

# Sum portfolio values across all stocks
total_values = []
for date in common_dates:
    daily_total = sum(all_portfolios[symbol].loc[date, 'Portfolio'] for symbol in symbols)
    total_values.append(daily_total)

final_total = float(total_values[-1]) if total_values else 0
total_profit = final_total - initial_cash
total_profit_pct = (total_profit / initial_cash) * 100

print(f"Initial Investment: ${initial_cash:,.2f}")
print(f"Final Portfolio Value: ${final_total:,.2f}")
print(f"Total Profit/Loss: ${total_profit:,.2f} ({total_profit_pct:.2f}%)")

# Buy & Hold comparison for all stocks
print(f"\n{'='*50}")
print("BUY & HOLD COMPARISON")
print('='*50)

buy_hold_total = 0
for symbol in symbols:
    df = all_portfolios[symbol]
    buy_hold_shares = cash_per_stock / float(df['Close'].iloc[0])
    buy_hold_value = buy_hold_shares * float(df['Close'].iloc[-1])
    buy_hold_total += buy_hold_value
    
    bh_profit = buy_hold_value - cash_per_stock
    bh_pct = (bh_profit / cash_per_stock) * 100
    print(f"{symbol}: ${buy_hold_value:,.2f} ({bh_pct:+.2f}%)")

buy_hold_profit = buy_hold_total - initial_cash
buy_hold_pct = (buy_hold_profit / initial_cash) * 100

print(f"\nTotal Buy & Hold: ${buy_hold_total:,.2f} ({buy_hold_pct:+.2f}%)")
print(f"Strategy vs Buy & Hold: {total_profit_pct - buy_hold_pct:+.2f}% difference")

# Plotting
fig = plt.figure(figsize=(14, 10))

# Plot 1: Individual stock prices with MAs
for idx, symbol in enumerate(symbols, 1):
    ax = plt.subplot(3, 2, idx)
    df = all_portfolios[symbol]
    ax.plot(df.index, df['Close'], label='Price', linewidth=1.5)
    ax.plot(df.index, df['SMA_20'], label='20-Day MA', linestyle='--', alpha=0.7)
    ax.plot(df.index, df['SMA_50'], label='50-Day MA', linestyle='--', alpha=0.7)
    ax.set_title(f'{symbol} - Price & Moving Averages')
    ax.set_ylabel('Price ($)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

# Plot 5: Individual portfolio performances
ax5 = plt.subplot(3, 2, 5)
for symbol in symbols:
    df = all_portfolios[symbol]
    ax5.plot(df.index, df['Portfolio'], label=symbol, linewidth=2)
ax5.axhline(y=cash_per_stock, color='red', linestyle='--', alpha=0.5, label='Initial per stock')
ax5.set_title('Individual Stock Portfolios')
ax5.set_ylabel('Value ($)')
ax5.legend(fontsize=8)
ax5.grid(True, alpha=0.3)

# Plot 6: Combined portfolio
ax6 = plt.subplot(3, 2, 6)
ax6.plot(common_dates, total_values, linewidth=2.5, color='green', label='Total Portfolio')
ax6.axhline(y=initial_cash, color='red', linestyle='--', alpha=0.5, label='Initial Investment')
ax6.set_title('Combined Portfolio Value')
ax6.set_xlabel('Date')
ax6.set_ylabel('Total Value ($)')
ax6.legend(fontsize=8)
ax6.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()