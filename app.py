import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

from optimizer import optimize_portfolio


st.set_page_config(
    page_title="Portfolio Optimization Dashboard",
    layout="wide"
)

st.title("Portfolio Optimization Dashboard")
st.write("Modern Portfolio Theory based portfolio optimizer")


# Sidebar
st.sidebar.header("Portfolio Settings")

stocks = st.sidebar.multiselect(
    "Select Stocks",
    ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "TSLA", "META", "JPM", "NFLX"],
    default=["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA"]
)

start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2019-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2025-01-01"))

risk_free_rate = st.sidebar.slider(
    "Risk Free Rate (%)",
    0.0,
    10.0,
    4.0
) / 100

num_portfolios = st.sidebar.slider(
    "Number of Random Portfolios",
    1000,
    50000,
    10000
)


if len(stocks) < 2:
    st.warning("Please select at least 2 stocks.")
    st.stop()


@st.cache_data
def load_data(stocks, start, end):
    data = yf.download(
        stocks,
        start=start,
        end=end,
        auto_adjust=True
    )["Close"]

    return data.dropna()


data = load_data(stocks, start_date, end_date)

st.subheader("Stock Price Data")
st.dataframe(data.tail())


# Price chart
st.subheader("Stock Price Chart")
st.line_chart(data)


# Daily returns
returns = data.pct_change().dropna()


# Cumulative returns
st.subheader("Cumulative Returns")
cumulative_returns = (1 + returns).cumprod()
st.line_chart(cumulative_returns)


# Correlation heatmap
st.subheader("Correlation Heatmap")

fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(
    returns.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    ax=ax
)
st.pyplot(fig)


# Optimization
results, max_sharpe, min_risk, max_weights, min_weights = optimize_portfolio(
    returns=returns,
    risk_free_rate=risk_free_rate,
    num_portfolios=num_portfolios
)


st.subheader("Portfolio Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Expected Return", f"{max_sharpe['Return']:.2%}")
col2.metric("Risk / Volatility", f"{max_sharpe['Risk']:.2%}")
col3.metric("Sharpe Ratio", f"{max_sharpe['Sharpe']:.2f}")


# Efficient frontier
st.subheader("Efficient Frontier")

fig, ax = plt.subplots(figsize=(10, 6))

scatter = ax.scatter(
    results["Risk"],
    results["Return"],
    c=results["Sharpe"],
    cmap="viridis",
    alpha=0.6
)

ax.scatter(
    max_sharpe["Risk"],
    max_sharpe["Return"],
    marker="*",
    s=300,
    label="Max Sharpe Portfolio"
)

ax.scatter(
    min_risk["Risk"],
    min_risk["Return"],
    marker="*",
    s=300,
    label="Minimum Risk Portfolio"
)

ax.set_xlabel("Risk")
ax.set_ylabel("Return")
ax.set_title("Efficient Frontier")
ax.legend()

fig.colorbar(scatter, label="Sharpe Ratio")
st.pyplot(fig)


# Allocation table
st.subheader("Optimal Portfolio Allocation")

allocation = pd.DataFrame({
    "Stock": stocks,
    "Weight": max_weights
})

allocation["Weight (%)"] = allocation["Weight"] * 100

st.dataframe(allocation)


# Pie chart
st.subheader("Allocation Pie Chart")

fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(
    allocation["Weight"],
    labels=allocation["Stock"],
    autopct="%1.1f%%",
    startangle=90
)
ax.set_title("Optimal Portfolio Weights")
st.pyplot(fig)


# Download allocation
csv = allocation.to_csv(index=False)

st.download_button(
    label="Download Portfolio Allocation",
    data=csv,
    file_name="portfolio_allocation.csv",
    mime="text/csv"
)