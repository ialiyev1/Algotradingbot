# Algotradingbot

An intelligent algorithmic trading bot for stocks, commodities, and indices using multiple brokers (Capital.com, IC Markets, cTrader, MT5, TradingView).

## 🎯 Features

- **Multi-Market Support**: US Stocks, Gold/Oil, Nasdaq/S&P500
- **Multi-Broker Integration**: Capital.com (primary), IC Markets, cTrader, MT5, TradingView
- **Separate Strategies**: Optimized strategies for each market type
- **Backtesting Engine**: Validate strategies on historical data
- **Risk Management**: Position sizing, stop-loss, take-profit
- **Real-time Monitoring**: Track positions and performance
- **Easy Deployment**: Run locally or on cloud servers

## 📊 Supported Markets

- **US Stocks**: Individual equities
- **Commodities**: Gold (XAU/USD), Oil (WTI/Brent)
- **Indices**: S&P 500, Nasdaq 100

## 🏗️ Project Structure

```
Algotradingbot/
├── config/
│   ├── __init__.py
│   ├── brokers.py          # API credentials & broker configs
│   ├── strategies.py       # Strategy parameters
│   └── settings.py         # Risk management, logging
├── strategies/
│   ├── __init__.py
│   ├── base_strategy.py    # Base class for all strategies
│   ├── stocks_strategy.py     # US Stocks strategy
│   ├── commodities_strategy.py # Gold/Oil strategy
│   └── indices_strategy.py     # Nasdaq/S&P500 strategy
├── core/
│   ├── __init__.py
│   ├── capital_client.py    # Capital.com API wrapper
│   ├── data_handler.py      # Price data management
│   ├── risk_manager.py      # Position sizing & stops
│   └── order_executor.py    # Place/manage orders
├── backtesting/
│   ├── __init__.py
│   ├── backtest_engine.py   # Run historical tests
│   └── metrics.py           # Performance analysis
├── utils/
│   ├── __init__.py
│   ├── logger.py            # Logging setup
│   └── helpers.py           # Utility functions
├── tests/
│   ├── __init__.py
│   ├── test_strategies.py
��   └── test_api.py
├── main.py                  # Entry point - start bot
├── backtest.py              # Run backtests
├── requirements.txt         # Dependencies
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
└── README.md
```

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.9+
- Capital.com API credentials
- Git

### 2. Installation

```bash
git clone https://github.com/ialiyev1/Algotradingbot.git
cd Algotradingbot
pip install -r requirements.txt
```

### 3. Configuration

Copy `.env.example` to `.env` and add your credentials:

```bash
cp .env.example .env
```

Edit `.env`:
```
CAPITAL_API_KEY=your_api_key
CAPITAL_API_SECRET=your_api_secret
CAPITAL_DEMO_MODE=True
```

### 4. Test API Connection

```bash
python -c "from core.capital_client import CapitalClient; c = CapitalClient(demo_mode=True); c.authenticate()"
```

### 5. Run Backtest

```bash
python backtest.py --strategy stocks --start-date 2023-01-01 --end-date 2024-01-01
```

### 6. Run Live Bot

```bash
python main.py
```

## 📈 Strategy Types

### Stocks Strategy
- Trend-following with moving averages (20/50 MA)
- RSI confirmation (overbought/oversold)
- Volume confirmation

### Commodities Strategy
- Mean reversion on Gold/Oil
- Bollinger Bands
- ATR-based stops

### Indices Strategy
- Momentum-based approach
- Breakout detection
- MACD signals

## ⚙️ Configuration Files

### `config/strategies.py`
Define parameters for each strategy:
- Moving average periods
- Entry/exit thresholds
- Risk-reward ratios

### `config/settings.py`
Risk management rules:
- Max position size
- Stop-loss percentage
- Daily loss limit

## 🔄 Broker Integration

Currently focusing on **Capital.com** API. To add other brokers:

1. Create new client class in `core/`
2. Implement base broker interface
3. Add to `order_executor.py`

## 📊 Backtesting

Test strategies on historical data:

```bash
python backtest.py \
  --strategy stocks \
  --start-date 2023-01-01 \
  --end-date 2024-12-31 \
  --initial-capital 10000 \
  --save-results results.json
```

## 🛡️ Risk Management

The bot enforces:
- **Position Sizing**: 2-3% of capital per trade
- **Stop Losses**: Hard stops on every trade
- **Daily Loss Limit**: Stops trading if daily loss exceeded
- **Correlation Checks**: Prevent over-concentration

## 📝 Logging & Monitoring

All trades logged to `logs/trading.log`:
- Entry/exit signals
- Order fills
- Profit/loss
- Errors and warnings

## 🔐 Security

- Use environment variables for credentials
- Never commit `.env` file
- API keys stored securely
- Mock mode for testing

## 🆘 Troubleshooting

### Bot won't connect to Capital.com
- Check API credentials in `.env`
- Verify IP whitelisting in Capital.com account settings
- Ensure `CAPITAL_DEMO_MODE=True` for testing

### Backtests show huge profits
- Check for lookahead bias in strategy
- Verify data quality
- Add realistic slippage & commissions

### Orders not filling
- Check market hours
- Verify position size limits
- Review order type (market vs limit)

## 📚 Resources

- [Capital.com API Docs](https://capital.com)
- [Python Trading Libraries](https://github.com/topics/trading-bot)
- [Backtesting Best Practices](https://en.wikipedia.org/wiki/Backtesting)

## ⚠️ Disclaimer

This bot is for educational purposes. Live trading involves risk. Start with demo mode and small positions. Always have risk management in place.

## 📄 License

MIT License

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open Pull Request

---

**Happy Trading! 🚀📈**