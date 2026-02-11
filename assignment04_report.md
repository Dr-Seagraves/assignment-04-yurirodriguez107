# Assignment 04 Interpretation Memo

**Student Name:** [Your Name]
**Date:** [Submission Date]
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
- Intercept (β₀): [value] (SE: [value], p-value: [value])
- Slope (β₁): [value] (SE: [value], p-value: [value])
- R²: [value] | N: [value]

**Model 2: ret ~ prime_rate**
- Intercept (β₀): [value] (SE: [value], p-value: [value])
- Slope (β₁): [value] (SE: [value], p-value: [value])
- R²: [value] | N: [value]

**Model 3: ret ~ ffo_at_reit**
- Intercept (β₀): [value] (SE: [value], p-value: [value])
- Slope (β₁): [value] (SE: [value], p-value: [value])
- R²: [value] | N: [value]

*Note: Model 3 may have fewer observations if ffo_at_reit has missing values; statsmodels drops those rows.*

---

## 3. Slope Interpretation (Economic Units)

**Dividend Yield (div12m_me):**
- A 1 percentage point increase in dividend yield (12-month dividends / market equity) is associated with a [slope value] change in annual return.
- [Your interpretation: Is higher dividend yield associated with higher or lower returns? Why might this be?]

**Prime Loan Rate (prime_rate):**
- A 1 percentage point increase in the year-end prime rate is associated with a [slope value] change in annual return.
- [Your interpretation: Does the evidence suggest REIT returns are sensitive to interest rates? In which direction?]

**FFO to Assets (ffo_at_reit):**
- A 1 unit increase in FFO/Assets (fundamental performance) is associated with a [slope value] change in annual return.
- [Your interpretation: Do more profitable REITs (higher FFO/Assets) earn higher returns?]

---

## 4. Statistical Significance

For each slope, at the 5% significance level:
- **div12m_me:** [Significant / Not significant] — [one sentence conclusion]
- **prime_rate:** [Significant / Not significant] — [one sentence conclusion]
- **ffo_at_reit:** [Significant / Not significant] — [one sentence conclusion]

**Which predictor has the strongest statistical evidence of a relationship with annual returns?** [Your answer]

---

## 5. Model Fit (R-squared)

Compare R² across the three models:
- [Your interpretation: Which predictor explains the most variation in annual returns? Is R² high or low in general? What does this suggest about other factors driving REIT returns?]

---

## 6. Omitted Variables

By using only one predictor at a time, we might be omitting:
- [Variable 1]: [Why it might matter]
- [Variable 2]: [Why it might matter]
- [Variable 3]: [Why it might matter]

**Potential bias:** If omitted variables are correlated with both the X variable and ret, our slope estimates may be biased. [Brief discussion of direction if possible]

---

## 7. Summary and Next Steps

**Key Takeaway:**
[2-3 sentences summarizing which predictor(s) show the strongest relationship with REIT annual returns and whether the evidence is consistent with economic theory]

**What we would do next:**
- Extend to multiple regression (include two or more predictors)
- Test for heteroskedasticity and other OLS assumption violations
- Examine whether relationships vary by time period or REIT sector

---

## Reproducibility Checklist
- [ ] Script runs end-to-end without errors
- [ ] Regression output saved to `Results/regression_div12m_me.txt`, `regression_prime_rate.txt`, `regression_ffo_at_reit.txt`
- [ ] Scatter plots saved to `Results/scatter_div12m_me.png`, `scatter_prime_rate.png`, `scatter_ffo_at_reit.png`
- [ ] Report accurately reflects regression results
- [ ] All interpretations are in economic units (not just statistical jargon)
