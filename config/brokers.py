"""Broker configuration and constants"""
from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class BrokerConfig:
    """Base broker configuration"""
    name: str
    base_url: str
    api_key: Optional[str] = None
    api_secret: Optional[str] = None
    timeout: int = 30
    max_retries: int = 3
    demo_mode: bool = True

# Capital.com Configuration
CAPITAL_CONFIG = BrokerConfig(
    name='Capital.com',
    base_url='https://api-capital.backend-capital.com',
    timeout=30,
    max_retries=3,
    demo_mode=True
)

# Supported Order Types
ORDER_TYPES = {
    'MARKET': 'Market Order - Execute immediately',
    'LIMIT': 'Limit Order - Execute at specific price',
    'STOP': 'Stop Order - Execute when price reaches level',
    'STOP_LIMIT': 'Stop-Limit Order - Combine stop and limit',
}

# Market Hours (EST)
MARKET_HOURS = {
    'US_STOCK': {
        'open': '09:30',
        'close': '16:00',
        'pre_market': '04:00',
        'after_hours': '20:00',
        'timezone': 'America/New_York'
    },
    'FOREX_COMMODITIES': {
        'open': '00:00',
        'close': '23:59',
        'timezone': 'UTC'
    }
}

# Risk Parameters
RISK_PARAMS = {
    'max_position_size': 0.05,  # 5% of capital
    'max_daily_loss': 0.05,  # 5% of daily capital
    'max_open_positions': 10,  # Max 10 concurrent positions
    'min_reward_to_risk': 1.5,  # Min 1.5:1 reward-to-risk ratio
}

# Asset Classes
ASSET_CLASSES = {
    'STOCKS': 'US Equities',
    'COMMODITIES': 'Metals and Energy',
    'INDICES': 'Market Indices',
    'FOREX': 'Currency Pairs',
}

print("✅ Broker configuration loaded")