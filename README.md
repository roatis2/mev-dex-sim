# MEV-Aware DEX Trade Simulator

This project is a simulation framework for analyzing how decentralized exchange (DEX) trades are executed under adversarial conditions, with a specific focus on **Maximal Extractable Value (MEV)** and **sandwich attacks**.

The simulator models how a seemingly simple swap can suffer additional, often invisible losses due to transaction ordering in the public mempool. By comparing execution outcomes across different routing assumptions—such as public mempool submission versus private relays—the project aims to make MEV risk **explicit, quantifiable, and reproducible**.

Rather than interacting directly with onchain liquidity, this tool focuses on **mechanistic modeling**:
- Constant-product AMM math
- Transaction ordering
- Adversarial front-run / back-run strategies
- User value loss vs MEV bot profit

The goal is not to build a trading bot or a production DEX, but to develop a clear mental and mathematical model of how MEV emerges, how it impacts users, and how different design choices affect execution quality.

This project is intended for:
- Protocol engineers
- DeFi researchers
- Traders interested in execution risk
- Anyone looking to understand MEV beyond surface-level explanations
