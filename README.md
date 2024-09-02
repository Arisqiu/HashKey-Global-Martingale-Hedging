# Martingale with Hedge Trading Strategy for HashKey Global

## Overview

This repository provides a Python implementation of a Martingale trading strategy with a hedging mechanism, specifically designed for the HashKey Global futures market. The strategy involves progressively increasing trade sizes after a loss, while simultaneously placing hedge trades to mitigate risk. Telegram: @ChildrenQ

## Features

- **Martingale Strategy**: Automatically increases trade size following a loss to recover previous losses and gain profits when the market reverses.
- **Hedging**: Simultaneously places a hedge trade to reduce the potential risk associated with the Martingale strategy.
- **Customizable Parameters**: Allows configuration of initial trade size, leverage, price movement thresholds, and maximum number of trades.

## Requirements

- Python 3.x
- `requests` library

You can install the required Python package with the following command:

```bash
pip install requests
```

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/Martingale-Hedge-Strategy.git
   cd Martingale-Hedge-Strategy
   ```

2. **Configure API Keys:**

   Replace `YOUR_HASHKEY_API_KEY` and `YOUR_HASHKEY_SECRET_KEY` in the script with your actual HashKey Global API credentials:

   ```python
   hashkey_api_key = 'YOUR_HASHKEY_API_KEY'
   hashkey_secret_key = 'YOUR_HASHKEY_SECRET_KEY'
   ```

3. **Adjust Strategy Parameters:**

   Modify the parameters in the `martingale_with_hedge_strategy()` function to suit your trading preferences:

   - `symbol`: The trading pair (e.g., `'BTCUSDT'`).
   - `initial_trade_size`: The size of the initial trade.
   - `leverage`: The leverage to apply to each trade.
   - `price_threshold`: The price movement threshold that triggers the next trade.
   - `max_trades`: The maximum number of trades in the Martingale sequence.

## Usage

To start the Martingale with Hedge trading strategy, simply run the script:

```bash
python martingale_hedge_strategy.py
```

The strategy will place the initial trade and monitor the market, automatically executing additional trades and hedging as required.

## How It Works

1. **Initial Trade:**
   - The bot places an initial BUY order with the specified `initial_trade_size`.

2. **Price Monitoring:**
   - The bot continuously monitors the market price. If the price moves against the initial position by more than the `price_threshold`, it will place an additional BUY order with double the previous trade size, in line with the Martingale strategy.

3. **Hedging:**
   - Whenever an additional BUY order is placed due to a price drop, a SELL order (hedge) of the same size is placed to limit potential losses.

4. **Trade Management:**
   - The bot repeats this process, doubling the trade size each time the market moves against the position, until the `max_trades` limit is reached.

5. **Risk Control:**
   - The strategy is designed with risk control in mind. The hedging mechanism helps mitigate the potential risks associated with the Martingale strategy.

## Notes

- **Risk Warning**: The Martingale strategy is inherently risky, especially when combined with leverage. Ensure you understand the risks before using this strategy.
- **Sufficient Funds**: Ensure your account has sufficient funds to cover the potential losses that could occur with this strategy.
- **API Rate Limits**: Be aware of HashKey Global's API rate limits to avoid throttling or failed requests.

## Disclaimer

This trading bot is provided for educational purposes only. Trading in futures and using leverage carries significant risk. Only trade with money that you can afford to lose. The authors are not responsible for any financial losses incurred while using this bot.

## License

This project is licensed under the MIT License.

## Contributions

Contributions are welcome! Feel free to fork the repository, submit issues, or create pull requests. Telegram: @ChildrenQ

---
