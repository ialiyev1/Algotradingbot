"""Strategy configurations and parameters"""
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class StrategyConfig:
    """Base strategy configuration"""
    name: str
    asset_class: str
    enabled: bool
    parameters: Dict
    risk_reward_ratio: float = 1.5

# ==================== STOCKS STRATEGY ====================
# Trend-following with Moving Average Crossover
STOCKS_STRATEGY_CONFIG = StrategyConfig(
    name='Stocks Trend Following',
    asset_class='STOCKS',
    enabled=True,
    risk_reward_ratio=1.5,
    parameters={
        'short_ma': 20,
        'long_ma': 50,
        'rsi_period': 14,
        'rsi_overbought': 70,
        'rsi_oversold': 30,
        'volume_sma': 20,
        'min_volume_multiplier': 1.2,  # Volume > 1.2x average
        'entry_type': 'MA_CROSSOVER',  # Moving Average Crossover
        'exit_type': 'PROFIT_TARGET_STOP',  # Take profit or stop loss
        'timeframe': 'D',  # Daily
        'max_positions': 5,
        'position_size_percent': 2.0,  # 2% of capital per trade
        'stop_loss_percent': 2.0,
        'take_profit_percent': 3.0,
    }
)

# ==================== COMMODITIES STRATEGY ====================
# Mean Reversion with Bollinger Bands
COMMODITIES_STRATEGY_CONFIG = StrategyConfig(
    name='Commodities Mean Reversion',
    asset_class='COMMODITIES',
    enabled=True,
    risk_reward_ratio=1.5,
    parameters={
        'bb_period': 20,
        'bb_std_dev': 2.0,
        'rsi_period': 14,
        'rsi_overbought': 70,
        'rsi_oversold': 30,
        'atr_period': 14,  # Average True Range
        'entry_type': 'BB_BREAKOUT',  # Bollinger Band Breakout
        'exit_type': 'MEAN_REVERSION',  # Exit when price reverts to mean
        'timeframe': 'H1',  # Hourly
        'max_positions': 3,
        'position_size_percent': 3.0,  # 3% of capital per trade
        'stop_loss_percent': 1.5,
        'take_profit_percent': 2.25,  # 1.5:1 reward
    }
)

# ==================== INDICES STRATEGY ====================
# Momentum-based approach with breakouts
INDICES_STRATEGY_CONFIG = StrategyConfig(
    name='Indices Momentum Breakout',
    asset_class='INDICES',
    enabled=True,
    risk_reward_ratio=2.0,
    parameters={
        'lookback_period': 20,  # 20-day high/low
        'momentum_period': 12,  # Momentum indicator period
        'macd_fast': 12,
        'macd_slow': 26,
        'macd_signal': 9,
        'volume_sma': 20,
        'entry_type': 'BREAKOUT',  # Break above 20-day high
        'exit_type': 'MOMENTUM_REVERSAL',  # Exit on momentum reversal
        'timeframe': 'D',  # Daily
        'max_positions': 2,
        'position_size_percent': 2.5,  # 2.5% of capital per trade
        'stop_loss_percent': 1.5,
        'take_profit_percent': 3.0,  # 2:1 reward
    }
)

# Strategy registry
STRATEGY_REGISTRY = {
    'stocks': STOCKS_STRATEGY_CONFIG,
    'commodities': COMMODITIES_STRATEGY_CONFIG,
    'indices': INDICES_STRATEGY_CONFIG,
}

def get_strategy_config(strategy_name: str) -> StrategyConfig:
    """Get strategy configuration by name"""
    if strategy_name not in STRATEGY_REGISTRY:
        raise ValueError(f"Strategy '{strategy_name}' not found. Available: {list(STRATEGY_REGISTRY.keys())}")
    return STRATEGY_REGISTRY[strategy_name]

def get_all_enabled_strategies() -> Dict[str, StrategyConfig]:
    """Get all enabled strategies"""
    return {name: config for name, config in STRATEGY_REGISTRY.items() if config.enabled}

print("✅ Strategy configurations loaded")