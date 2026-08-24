# Stakeholder Memo: Daily Market Volatility Forecast

**To:** Portfolio Manager
**Project:** S&P 500 Daily Volatility Forecasting
**Stage:** Problem Framing & Scoping

## Decision Context

Portfolio exposure and hedging decisions depend partly on the amount of market risk expected over the next trading period. Volatility can change quickly, so risk estimates based only on recent historical conditions may not always provide an adequate indication of next-day risk.

## Stakeholder Need

The portfolio manager needs a concise and interpretable estimate of expected next-day S&P 500 volatility before making daily risk management decisions. The estimate should help identify periods when expected market risk is elevated and additional attention to portfolio exposure, risk limits, or hedging may be warranted.

## Proposed Output

The project will produce a next-day volatility forecast using information available at the time of prediction. Forecast accuracy will be evaluated out of sample using MAE and RMSE and compared with a simple historical-volatility baseline.

## How the Output Will Be Used

The forecast is intended to serve as a decision-support signal rather than an automated trading rule. A higher expected-volatility estimate may prompt the portfolio manager to review position sizes, portfolio risk limits, or hedging needs. A lower estimate may indicate that current exposure remains consistent with the portfolio's existing risk tolerance.

## Key Risks

Forecasts may become less reliable during extreme market events or structural changes in market behavior. Model complexity also does not guarantee better forecasting performance. These risks will be addressed through time-ordered out-of-sample testing, baseline comparison, and explicit documentation of model limitations.

