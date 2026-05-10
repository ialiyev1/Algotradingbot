"""Main settings and configuration for the trading bot"""
import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
CAPITAL_API_KEY = os.getenv('CAPITAL_API_KEY')
CAPITAL_API_SECRET = os.getenv('CAPITAL_API_SECRET')
CAPITAL_DEMO_MODE = os.getenv('CAPITAL_DEMO_MODE', 'True').lower() == 'true'
CAPITAL_BASE_URL = os.getenv('CAPITAL_BASE_URL', 'https://api-capital.backend-capital.com')

# Trading Parameters
INITIAL_CAPITAL = float(os.getenv('INITIAL_CAPITAL', 10000))
MAX_DAILY_LOSS_PERCENT = float(os.getenv('MAX_DAILY_LOSS_PERCENT', 5))
RISK_PER_TRADE_PERCENT = float(os.getenv('RISK_PER_TRADE_PERCENT', 2))

# Position Management
MAX_POSITION_SIZE_PERCENT = 5.0  # Max 5% of capital per trade
MIN_POSITION_SIZE = 100  # Minimum position size in USD
STOP_LOSS_PERCENT = 2.0  # Default stop loss
TAKE_PROFIT_RATIO = 1.5  # Risk:Reward ratio

# Logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = os.getenv('LOG_FILE', 'logs/trading.log')
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Markets Configuration
MARKETS = {
    'stocks': {
        'symbols': ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'NVDA', 'META', 'NFLX'],
        'enabled': True,
        'time_frame': 'D',  # Daily
        'trading_hours': '09:30-16:00'  # EST
    },
    'commodities': {
        'symbols': ['XAU/USD', 'WTI/USD', 'BRENT/USD'],  # Gold, WTI Oil, Brent Oil
        'enabled': True,
        'time_frame': 'H1',  # Hourly
        'trading_hours': '00:00-23:00'  # 24/5
    },
    'indices': {
        'symbols': ['SPX500', 'NDAQ100'],  # S&P 500, Nasdaq 100
        'enabled': True,
        'time_frame': 'D',  # Daily
        'trading_hours': '09:30-16:00'  # EST
    }
}

# Backtesting Configuration
BACKTEST_START_DATE = os.getenv('BACKTEST_START_DATE', '2023-01-01')
BACKTEST_END_DATE = os.getenv('BACKTEST_END_DATE', '2024-01-01')
BACKTEST_INITIAL_CAPITAL = float(os.getenv('BACKTEST_INITIAL_CAPITAL', 100000))
BACKTEST_COMMISSION_PERCENT = 0.001  # 0.1% commission
BACKTEST_SLIPPAGE_PERCENT = 0.0005  # 0.05% slippage

# Feature Flags
LIVE_TRADING_ENABLED = False  # Always start with False
USE_PAPER_TRADING = True
LOG_TO_FILE = True
LOG_TO_CONSOLE = True

print(f"✅ Settings loaded. Demo Mode: {CAPITAL_DEMO_MODE}")