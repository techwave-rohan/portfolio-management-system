# 📈 Portfolio Optimization using Modern Portfolio Theory (MPT)

A quantitative finance project that builds an optimal investment portfolio using **Modern Portfolio Theory (MPT)**. The project analyzes historical stock market data, calculates financial risk metrics, generates thousands of random portfolios using Monte Carlo simulation, and identifies the portfolio with the **maximum Sharpe Ratio** and **minimum risk**. An interactive **Streamlit dashboard** allows users to explore stock performance, portfolio allocation, and the Efficient Frontier.

---

## 🚀 Features

* Download historical stock prices using **Yahoo Finance**
* Perform Exploratory Data Analysis (EDA)
* Calculate daily and cumulative returns
* Generate correlation heatmaps
* Compute annualized returns and volatility
* Calculate covariance matrix
* Compute portfolio risk and expected return
* Calculate Sharpe Ratio
* Calculate Maximum Drawdown
* Generate 10,000+ random portfolios using Monte Carlo Simulation
* Identify:

  * Maximum Sharpe Portfolio
  * Minimum Variance Portfolio
* Visualize the Efficient Frontier
* Interactive Streamlit dashboard
* Download optimal portfolio allocation as CSV

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* yfinance
* Streamlit

---

## 📂 Project Structure

```text
portfolio-optimization/
│
├── app.py
├── optimizer.py
├── requirements.txt
│
├── data/
│   ├── stock_prices.csv
│   └── daily_returns.csv
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_EDA.ipynb
│   ├── 03_risk_metrics.ipynb
│   └── 04_portfolio_optimization.ipynb
│
└── README.md
```

---

## 📊 Dashboard Features

* Historical Stock Price Visualization
* Daily & Cumulative Return Analysis
* Correlation Heatmap
* Portfolio Optimization using Modern Portfolio Theory
* Efficient Frontier Visualization
* Portfolio Risk Metrics
* Portfolio Allocation Pie Chart
* Download Portfolio Allocation

---

## 📈 Financial Metrics Implemented

* Expected Annual Return
* Annualized Volatility
* Covariance Matrix
* Portfolio Return
* Portfolio Risk
* Sharpe Ratio
* Maximum Drawdown

---

## 📐 Mathematical Concepts Used

* Modern Portfolio Theory (MPT)
* Mean-Variance Optimization
* Portfolio Diversification
* Covariance & Correlation
* Monte Carlo Simulation
* Risk-Adjusted Performance Measurement

---

## 🚀 Future Improvements

* Portfolio optimization using `scipy.optimize`
* Machine Learning-based return prediction
* Value at Risk (VaR)
* Sortino Ratio
* Sector-wise allocation analysis
* Portfolio rebalancing strategies
* Interactive Plotly visualizations
* Portfolio growth simulator with SIP
* Backtesting framework

---

## 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

* Financial data analysis
* Quantitative finance
* Portfolio optimization
* Risk management
* Python for finance
* Data visualization
* Statistical analysis
* Streamlit application development

---

## ▶️ Run the Project

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📌 Project Highlights

* Built a complete quantitative finance application from scratch.
* Implemented Modern Portfolio Theory for portfolio optimization.
* Simulated thousands of portfolios using Monte Carlo methods.
* Evaluated portfolios using the Sharpe Ratio and risk-return trade-offs.
* Developed an interactive Streamlit dashboard for portfolio analysis and visualization.
