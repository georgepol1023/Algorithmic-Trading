# 📈 Algorithmic Trading Strategy

A Python-based algorithmic trading system using **Moving Average Crossover** strategy to backtest and analyze stock performance across multiple securities.

## 🎯 Overview

This project implements a simple yet effective trading strategy that:
- Trades multiple stocks simultaneously (AAPL, MSFT, GOOGL, TSLA)
- Uses 20-day and 50-day moving averages to generate buy/sell signals
- Backtests the strategy with historical data
- Compares performance against buy-and-hold strategy
- Visualizes results with comprehensive charts

## 🚀 Features

- **Multi-Stock Portfolio**: Trade multiple stocks with equal capital allocation
- **Moving Average Crossover**: Buy when short-term MA crosses above long-term MA
- **Backtesting Engine**: Simulate trades on historical data
- **Performance Metrics**: Track profit/loss, returns, and compare to buy-and-hold
- **Visual Analytics**: 6 comprehensive charts showing prices, signals, and portfolio performance
- **Real Market Data**: Downloads live data from Yahoo Finance

## 📋 Requirements

```
Python 3.7+
pandas
numpy
yfinance
matplotlib
scikit-learn
```

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/algorithmic-trading.git
cd algorithmic-trading
```

2. **Install dependencies**
```bash
pip install pandas numpy yfinance matplotlib scikit-learn
```

Or use requirements.txt:
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Basic Usage

Run the trading strategy:
```bash
python code.py
```

### Customize Stocks

Edit the `symbols` list in the code:
```python
symbols = ['AAPL', 'MSFT', 'GOOGL', 'TSLA']  # Change to any stocks you want
```

### Adjust Date Range

Modify the date parameters:
```python
df = yf.download(symbol, start='2023-01-01', end='2024-01-01')
```

### Change Initial Capital

Update the starting investment:
```python
initial_cash = 10000  # Change to any amount
```

## 📊 How It Works

### Strategy Logic

1. **Calculate Moving Averages**
   - 20-day MA (short-term, fast-moving)
   - 50-day MA (long-term, slow-moving)

2. **Generate Signals**
   - **BUY**: When 20-day MA crosses above 50-day MA (bullish signal)
   - **SELL**: When 20-day MA crosses below 50-day MA (bearish signal)

3. **Execute Trades**
   - Buy with all available cash when buy signal appears
   - Sell all shares when sell signal appears
   - No partial positions or stop-losses (simplified model)

4. **Track Performance**
   - Calculate portfolio value daily
   - Compare to buy-and-hold strategy
   - Generate performance metrics

## 📈 Output

### Terminal Output

The program displays:
- Trade execution details (buy/sell dates and prices)
- Individual stock performance
- Combined portfolio results
- Buy-and-hold comparison
- Profit/loss percentages

Example:
```
Trading 4 stocks with $2,500.00 each
Total Initial Investment: $10,000.00

Processing AAPL
BUY:  2023-03-15 - Price: $155.23 - Shares: 16.11
SELL: 2023-08-22 - Price: $177.23 - Cash: $2,854.17

AAPL Results:
  Starting: $2,500.00
  Ending: $2,854.17
  Profit/Loss: $354.17 (14.17%)

COMBINED PORTFOLIO RESULTS
Final Portfolio Value: $11,234.56
Total Profit/Loss: $1,234.56 (12.35%)
```

### Visual Output

Six charts are generated:
1. **AAPL** - Price with moving averages
2. **MSFT** - Price with moving averages
3. **GOOGL** - Price with moving averages
4. **TSLA** - Price with moving averages
5. **Individual Portfolios** - All stock performances overlaid
6. **Combined Portfolio** - Total portfolio value over time

## ⚠️ Limitations & Disclaimers

**This is an educational project. NOT financial advice.**

### Known Limitations:
- **No transaction costs** - Real trading has commissions and slippage
- **No stop-losses** - Can lead to large drawdowns
- **Simplified signals** - Real strategies use multiple indicators
- **Backtesting bias** - Past performance ≠ future results
- **No risk management** - Doesn't account for position sizing or portfolio heat
- **Market hours ignored** - Assumes you can trade at closing prices

### Important Notes:
- This strategy may underperform in sideways/choppy markets
- Moving averages are lagging indicators
- Not suitable for live trading without significant enhancements
- Always do your own research before investing real money

## 🔮 Future Enhancements

Potential improvements:
- [ ] Add transaction costs and slippage
- [ ] Implement stop-loss and take-profit levels
- [ ] Add more technical indicators (RSI, MACD, Bollinger Bands)
- [ ] Position sizing based on volatility
- [ ] Walk-forward optimization
- [ ] Risk metrics (Sharpe ratio, max drawdown, etc.)
- [ ] Paper trading integration
- [ ] Real-time data streaming
- [ ] Machine learning signal generation

## 📚 Learning Resources

- [Investopedia - Moving Averages](https://www.investopedia.com/terms/m/movingaverage.asp)
- [Python for Finance](https://www.oreilly.com/library/view/python-for-finance/9781492024323/)
- [Algorithmic Trading Strategies](https://www.quantstart.com/)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 👤 Author

**Your Name**
- GitHub: [@georgepol1023](https://github.com/georgepol1023)

## 🙏 Acknowledgments

- Yahoo Finance for providing free historical market data
- The open-source Python community
- All contributors and users of this project

---
