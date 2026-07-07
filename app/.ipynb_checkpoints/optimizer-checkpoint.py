import numpy as np
import pandas as pd


def optimize_portfolio(returns, risk_free_rate=0.04, num_portfolios=10000):
    mean_returns = returns.mean() * 252
    cov_matrix = returns.cov() * 252
    num_assets = len(mean_returns)

    portfolio_returns = []
    portfolio_risks = []
    portfolio_sharpes = []
    portfolio_weights = []

    for _ in range(num_portfolios):
        weights = np.random.random(num_assets)
        weights = weights / np.sum(weights)

        portfolio_return = np.dot(weights, mean_returns)

        portfolio_risk = np.sqrt(
            np.dot(
                weights.T,
                np.dot(cov_matrix, weights)
            )
        )

        sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_risk

        portfolio_returns.append(portfolio_return)
        portfolio_risks.append(portfolio_risk)
        portfolio_sharpes.append(sharpe_ratio)
        portfolio_weights.append(weights)

    results = pd.DataFrame({
        "Return": portfolio_returns,
        "Risk": portfolio_risks,
        "Sharpe": portfolio_sharpes
    })

    max_sharpe_idx = results["Sharpe"].idxmax()
    min_risk_idx = results["Risk"].idxmin()

    max_sharpe = results.loc[max_sharpe_idx]
    min_risk = results.loc[min_risk_idx]

    max_weights = portfolio_weights[max_sharpe_idx]
    min_weights = portfolio_weights[min_risk_idx]

    return results, max_sharpe, min_risk, max_weights, min_weights