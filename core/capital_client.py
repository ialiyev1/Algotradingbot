"""Capital.com API Client Implementation"""
import requests
import json
from typing import Dict, Optional, List
from datetime import datetime
import os
from config.settings import CAPITAL_API_KEY, CAPITAL_API_SECRET, CAPITAL_BASE_URL, CAPITAL_DEMO_MODE
from utils.logger import get_logger

logger = get_logger(__name__)

class CapitalClient:
    """Client for Capital.com Trading API"""
    
    def __init__(self, api_key: str = None, api_secret: str = None, demo_mode: bool = True):
        """
        Initialize Capital.com client
        
        Args:
            api_key: API key from Capital.com
            api_secret: API secret from Capital.com
            demo_mode: Use demo/paper trading
        """
        self.api_key = api_key or CAPITAL_API_KEY
        self.api_secret = api_secret or CAPITAL_API_SECRET
        self.base_url = CAPITAL_BASE_URL
        self.demo_mode = demo_mode or CAPITAL_DEMO_MODE
        self.access_token = None
        self.session = requests.Session()
        self.timeout = 30
        
        if not self.api_key or not self.api_secret:
            raise ValueError("API key and secret required. Set in .env file.")
        
        logger.info(f"CapitalClient initialized - Demo Mode: {self.demo_mode}")
    
    def authenticate(self) -> bool:
        """
        Authenticate with Capital.com API
        
        Returns:
            bool: True if authentication successful
        """
        try:
            url = f"{self.base_url}/api/v1/auth/login"
            payload = {
                'email': self.api_key,
                'password': self.api_secret,
                'requestId': str(datetime.now().timestamp())
            }
            
            response = self.session.post(url, json=payload, timeout=self.timeout)
            response.raise_for_status()
            
            data = response.json()
            self.access_token = data.get('session')
            self.session.headers.update({
                'Authorization': f'Bearer {self.access_token}',
                'Content-Type': 'application/json'
            })
            
            logger.info("✅ Authentication successful")
            return True
            
        except Exception as e:
            logger.error(f"❌ Authentication failed: {str(e)}")
            return False
    
    def get_account_info(self) -> Optional[Dict]:
        """
        Get account information
        
        Returns:
            Dict with account details or None
        """
        if not self.access_token:
            logger.warning("Not authenticated. Call authenticate() first.")
            return None
        
        try:
            url = f"{self.base_url}/api/v1/accounts"
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            return response.json()
            
        except Exception as e:
            logger.error(f"Failed to get account info: {str(e)}")
            return None
    
    def get_market_data(self, symbol: str, timeframe: str = 'D') -> Optional[Dict]:
        """
        Get market data for a symbol
        
        Args:
            symbol: Trading symbol (e.g., 'AAPL', 'XAU/USD')
            timeframe: Timeframe ('D' for daily, 'H1' for hourly, etc.)
        
        Returns:
            Dict with OHLC data or None
        """
        if not self.access_token:
            logger.warning("Not authenticated.")
            return None
        
        try:
            url = f"{self.base_url}/api/v1/markets"
            params = {
                'searchTerm': symbol,
            }
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            
            return response.json()
            
        except Exception as e:
            logger.error(f"Failed to get market data for {symbol}: {str(e)}")
            return None
    
    def create_order(
        self,
        symbol: str,
        direction: str,  # 'BUY' or 'SELL'
        quantity: float,
        order_type: str = 'MARKET',  # MARKET, LIMIT, STOP
        price: Optional[float] = None,
        stop_loss: Optional[float] = None,
        take_profit: Optional[float] = None
    ) -> Optional[Dict]:
        """
        Create a new order
        
        Args:
            symbol: Trading symbol
            direction: 'BUY' or 'SELL'
            quantity: Order quantity
            order_type: Type of order
            price: Limit price (required for LIMIT orders)
            stop_loss: Stop loss price
            take_profit: Take profit price
        
        Returns:
            Order response or None
        """
        if not self.access_token:
            logger.warning("Not authenticated.")
            return None
        
        if direction not in ['BUY', 'SELL']:
            logger.error("Direction must be 'BUY' or 'SELL'")
            return None
        
        try:
            url = f"{self.base_url}/api/v1/positions/open"
            
            payload = {
                'epic': symbol,
                'direction': direction,
                'size': quantity,
                'orderType': order_type,
                'currencyCode': 'USD',
                'expiry': '-'
            }
            
            if order_type == 'LIMIT' and price:
                payload['limitLevel'] = price
            
            if stop_loss:
                payload['stopLevel'] = stop_loss
            
            if take_profit:
                payload['profitLevel'] = take_profit
            
            response = self.session.post(url, json=payload, timeout=self.timeout)
            response.raise_for_status()
            
            order_data = response.json()
            logger.info(f"✅ Order created: {symbol} {direction} x{quantity}")
            return order_data
            
        except Exception as e:
            logger.error(f"❌ Failed to create order: {str(e)}")
            return None
    
    def close_position(self, position_id: str) -> bool:
        """
        Close an open position
        
        Args:
            position_id: Position ID to close
        
        Returns:
            bool: True if successful
        """
        if not self.access_token:
            logger.warning("Not authenticated.")
            return False
        
        try:
            url = f"{self.base_url}/api/v1/positions/{position_id}/close"
            response = self.session.post(url, timeout=self.timeout)
            response.raise_for_status()
            
            logger.info(f"✅ Position {position_id} closed")
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to close position: {str(e)}")
            return False
    
    def update_stop_loss(self, position_id: str, stop_loss_price: float) -> bool:
        """
        Update stop loss for a position
        
        Args:
            position_id: Position ID
            stop_loss_price: New stop loss price
        
        Returns:
            bool: True if successful
        """
        if not self.access_token:
            logger.warning("Not authenticated.")
            return False
        
        try:
            url = f"{self.base_url}/api/v1/positions/{position_id}"
            payload = {'stopLevel': stop_loss_price}
            response = self.session.put(url, json=payload, timeout=self.timeout)
            response.raise_for_status()
            
            logger.info(f"✅ Stop loss updated for position {position_id}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to update stop loss: {str(e)}")
            return False
    
    def get_open_positions(self) -> Optional[List[Dict]]:
        """
        Get all open positions
        
        Returns:
            List of open positions or None
        """
        if not self.access_token:
            logger.warning("Not authenticated.")
            return None
        
        try:
            url = f"{self.base_url}/api/v1/positions"
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            return response.json()
            
        except Exception as e:
            logger.error(f"Failed to get open positions: {str(e)}")
            return None

# Test connection
if __name__ == "__main__":
    client = CapitalClient(demo_mode=True)
    if client.authenticate():
        account = client.get_account_info()
        if account:
            print(json.dumps(account, indent=2))
        else:
            print("Failed to get account info")
    else:
        print("Authentication failed")