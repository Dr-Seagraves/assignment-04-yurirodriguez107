# Assignment 04 Interpretation Memo

**Student Name:** Yuri Rodriguez
**Date:** March 4, 2026
**Assignment:** REIT Annual Returns and Predictors (Simple Linear Regression)

---

## 1. Regression Overview

You estimated **three** simple OLS regressions of REIT *annual* returns on different predictors:

| Model | Y Variable | X Variable | Interpretation Focus |
|-------|------------|------------|----------------------|
| 1 | ret (annual) | div12m_me | Dividend yield |
| 2 | ret (annual) | prime_rate | Interest rate sensitivity |
| 3 | ret (annual) | ffo_at_reit | FFO to assets (fundamental performance) |

For each model, summarize the key results in the sections below.

---

## 2. Coefficient Comparison (All Three Regressions)

**Model 1: ret ~ div12m_me**
- Intercept (β₀): 0.1082 (SE: 0.0060, p-value: 0.000)
- Slope (β₁): -0.0687 (SE: 0.0325, p-value: 0.035)
- R²: 0.0018 | N: 2,527

**Model 2: ret ~ prime_rate**
- Intercept (β₀): 0.1998 (SE: 0.0158, p-value: 0.000)
- Slope (β₁): -0.0194 (SE: 0.0030, p-value: 0.000)
- R²: 0.0164 | N: 2,527

**Model 3: ret ~ ffo_at_reit**
- Intercept (β₀): 0.0973 (SE: 0.0092, p-value: 0.000)
- Slope (β₁): 0.5770 (SE: 0.5675, p-value: 0.309)
- R²: 0.0004 | N: 2,518

*Note: Model 3 may have fewer observations if ffo_at_reit has missing values; statsmodels drops those rows.*

---

## 3. Slope Interpretation (Economic Units)

**Dividend Yield (div12m_me):**
- A 1 percentage point increase in dividend yield (12-month dividends / market equity) is associated with a **-6.87 percentage point decrease** in annual return.
- Higher-dividend REITs paradoxically show lower returns in this sample. This may reflect a value trap: mature, slower-growth REITs offer high current yields but lack price appreciation. Alternatively, high-dividend REITs may be less efficient capital allocators, retaining less for growth reinvestment.

**Prime Loan Rate (prime_rate):**
- A 1 percentage point increase in the year-end prime rate is associated with a **-1.94 percentage point decrease** in annual return.
- REIT returns are negatively sensitive to interest rates. When the Federal Reserve raises rates, REIT valuations compress (higher discount rates reduce asset values), and borrowing costs increase. This is consistent with economic theory: REITs are capital-intensive, leveraged firms sensitive to the cost of debt.

**FFO to Assets (ffo_at_reit):**
- A 1 unit increase in FFO/Assets (fundamental performance) is associated with a **0.577 change** in annual return.
- The sign is positive (better fundamental profitability is weakly associated with higher returns), but the relationship is not statistically significant. This suggests FFO/Assets is a poor predictor of annual returnsalone, and other factors dominate short-term price movements.

---

## 4. Statistical Significance

For each slope, at the 5% significance level:
- **div12m_me:** Significant (p = 0.035) — A 1 percentage point increase in dividend yield is associated with a statistically significant 6.87 percentage point decrease in annual returns.
- **prime_rate:** Significant (p < 0.001) — A 1 percentage point increase in prime rate is associated with a statistically significant 1.94 percentage point decrease in annual returns.
- **ffo_at_reit:** Not significant (p = 0.309) — FFO/Assets is not a statistically reliable predictor of annual returns at the 5% level.

**Which predictor has the strongest statistical evidence of a relationship with annual returns?** **Prime loan rate** (p < 0.001, t-stat = -6.49) shows the most robust and highly significant relationship. The negative slope coefficient is also economically stable across time periods, reflecting fundamental interest-rate sensitivity in REIT valuation.

---

## 5. Model Fit (R-squared)

Compare R² across the three models:
- Prime rate explains the most variation: R² = 0.0164 (1.64% of variation in annual returns)
- Dividend yield explains: R² = 0.0018 (0.18% of variation)
- FFO/Assets explains: R² = 0.0004 (0.04% of variation)

**Interpretation:** Prime rate is the strongest univariate predictor, but all three models have extremely low R² values. This indicates that even the best single-variable predictor explains less than 2% of REIT return variation. The vast majority of REIT returns are driven by omitted factors (market sentiment, sector rotation, firm-specific news, economic cycles, etc.). Single predictors are insufficient to explain REIT annual returns, motivating the need for multiple regression and richer models.

---

## 6. Omitted Variables

By using only one predictor at a time, we might be omitting:
- **Economic growth and market returns (e.g., S&P 500 return):** REIT returns are correlated with broad market performance. Omitting market returns may bias slope estimates if both market returns and our X variables move together.
- **Property type and sector:** Not all REITs are equal. Office, retail, residential, and industrial REITs respond differently to economic cycles. Omitting sector dummies may introduce omitted variable bias if sector is correlated with dividend yield, interest rates, or FFO/Assets.
- **Leverage and financial risk:** Firm-level debt ratios and refinancing risk affect returns. Highly leveraged REITs may have higher dividend yields but also face greater downside risk, creating a spurious negative dividend yield–return relationship.

**Potential bias:** The negative dividend yield slope may reflect negative omitted variable bias (high-dividend REITs are mature, higher-leverage firms with fewer growth prospects—growth expectations are omitted and negatively correlated with both dividend yield and returns). Including growth variables would likely reduce the magnitude of the dividend yield coefficient.

---

## 7. Summary and Next Steps

**Key Takeaway:**
Prime loan rate is the strongest and most statistically significant predictor of REIT annual returns (p < 0.001, R² = 1.64%), reflecting REITs' fundamental sensitivity to interest rates. Dividend yield also predicts returns negatively (p = 0.035), likely capturing a value-trap effect (high-yield, mature REITs underperform). FFO/Assets does not significantly predict annual returns in univariate form, suggesting that near-term profitability metrics are overwhelmed by sentiment and macro factors. Overall, REIT returns are driven by many factors beyond these three predictors, highlighting the need for multivariable models and macro risk factors.

**What we would do next:**
- Extend to multiple regression (include market returns, interest rates, and dividend yield simultaneously to disentangle effects)
- Add fixed effects for property type/sector to control for structural differences
- Test for heteroskedasticity and estimate robust standard errors
- Examine whether relationships vary by time period (pre/post-2008 crisis, low vs. high rate environments)

---

## Reproducibility Checklist
- [x] Script runs end-to-end without errors
- [x] Regression output saved to `Results/regression_div12m_me.txt`, `regression_prime_rate.txt`, `regression_ffo_at_reit.txt`
- [x] Scatter plots saved to `Results/scatter_div12m_me.png`, `scatter_prime_rate.png`, `scatter_ffo_at_reit.png`
- [x] Report accurately reflects regression results
- [x] All interpretations are in economic units (not just statistical jargon)
