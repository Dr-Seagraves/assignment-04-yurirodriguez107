"""
Test suite for Assignment 04: Simple Linear Regression (REIT Annual Returns and Predictors)

Each test is graded separately for partial credit. GitHub Classroom splits the total
points evenly across tests—pass N of 10 tests, get N/10 of the points.

Tests verify: script runs, each output file exists (6 files), regression content valid,
and data structure. Uses REIT_sample_annual_*.csv and interest_rates_monthly.csv.
Run fetch_interest_rates.py to download interest rate data if missing.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pandas as pd

REQUIRED_OUTPUTS = [
    "Results/regression_div12m_me.txt",
    "Results/regression_prime_rate.txt",
    "Results/regression_ffo_at_reit.txt",
    "Results/scatter_div12m_me.png",
    "Results/scatter_prime_rate.png",
    "Results/scatter_ffo_at_reit.png",
]


def _get_repo_root() -> Path:
    """Classroom template root (parent of tests/)."""
    return Path(__file__).resolve().parents[1]


def _get_script_and_output_dir() -> tuple[Path, Path, Path]:
    """
    Return (script_path, cwd, results_dir).
    If annual solution exists (instructor repo), run it. Else run student script.
    """
    repo_root = _get_repo_root()
    annual_solution = repo_root.parent / "solution" / "assignment04_regression_annual_solution.py"
    if annual_solution.exists():
        return annual_solution, annual_solution.parent, annual_solution.parent / "Results_annual"
    return repo_root / "assignment04_regression.py", repo_root, repo_root / "Results"


def _run_script() -> tuple[int, Path]:
    """Run the regression script; return (exit_code, results_dir)."""
    data_dir = _get_repo_root() / "data"
    if not list(data_dir.glob("REIT_sample_annual_*.csv")):
        raise FileNotFoundError(
            f"No REIT_sample_annual_*.csv in {data_dir}. Use REIT_sample_annual_2004_2024.csv."
        )
    if not (data_dir / "interest_rates_monthly.csv").exists():
        raise FileNotFoundError(
            f"Missing interest_rates_monthly.csv in {data_dir}. Run fetch_interest_rates.py."
        )
    script_path, cwd, results_dir = _get_script_and_output_dir()
    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=60,
    )
    return result.returncode, results_dir


def test_script_runs_without_error() -> None:
    """Script runs successfully (exit code 0)."""
    exit_code, _ = _run_script()
    assert exit_code == 0, (
        "Script failed. Check for NotImplementedError, syntax errors, or missing implementations."
    )


def test_regression_div12m_me_exists() -> None:
    """Regression summary for div12m_me exists."""
    _, results_dir = _run_script()
    assert (results_dir / "regression_div12m_me.txt").exists(), "Missing regression_div12m_me.txt"


def test_regression_prime_rate_exists() -> None:
    """Regression summary for prime_rate exists."""
    _, results_dir = _run_script()
    assert (results_dir / "regression_prime_rate.txt").exists(), "Missing regression_prime_rate.txt"


def test_regression_ffo_at_reit_exists() -> None:
    """Regression summary for ffo_at_reit exists."""
    _, results_dir = _run_script()
    assert (results_dir / "regression_ffo_at_reit.txt").exists(), "Missing regression_ffo_at_reit.txt"


def test_scatter_div12m_me_exists() -> None:
    """Scatter plot for div12m_me exists."""
    _, results_dir = _run_script()
    assert (results_dir / "scatter_div12m_me.png").exists(), "Missing scatter_div12m_me.png"


def test_scatter_prime_rate_exists() -> None:
    """Scatter plot for prime_rate exists."""
    _, results_dir = _run_script()
    assert (results_dir / "scatter_prime_rate.png").exists(), "Missing scatter_prime_rate.png"


def test_scatter_ffo_at_reit_exists() -> None:
    """Scatter plot for ffo_at_reit exists."""
    _, results_dir = _run_script()
    assert (results_dir / "scatter_ffo_at_reit.png").exists(), "Missing scatter_ffo_at_reit.png"


def test_regression_summary_has_valid_content() -> None:
    """Regression summary contains OLS header, R-squared, and coefficients."""
    _, results_dir = _run_script()
    summary_path = results_dir / "regression_div12m_me.txt"
    assert summary_path.exists(), "Regression summary file not found"
    summary_text = summary_path.read_text(encoding="utf-8")

    assert "OLS" in summary_text or "Regression" in summary_text, (
        "Regression summary does not contain expected header"
    )
    assert "R-squared" in summary_text or "R²" in summary_text, (
        "Regression summary does not contain R-squared"
    )
    assert "coef" in summary_text.lower(), (
        "Regression summary does not contain coefficient column"
    )


def test_data_loaded_correctly() -> None:
    """Test that the real REIT annual data can be loaded and has expected structure."""
    data_dir = _get_repo_root() / "data"
    candidates = list(data_dir.glob("REIT_sample_annual_*.csv"))
    if not candidates:
        raise FileNotFoundError(
            f"No REIT_sample_annual_*.csv in {data_dir}. Use REIT_sample_annual_2004_2024.csv."
        )
    data_path = max(candidates, key=lambda p: p.stat().st_mtime)

    df = pd.read_csv(data_path)

    required_cols = {"ret12", "div12m_me", "ffo_at_reit", "year"}
    assert required_cols.issubset(set(df.columns)), (
        f"Missing required columns. Expected {required_cols}, got {set(df.columns)}"
    )
    assert len(df) > 0, "Data file is empty"

    for col in required_cols:
        assert pd.api.types.is_numeric_dtype(df[col]), (
            f"{col} should be numeric"
        )


def test_interest_rates_loaded_correctly() -> None:
    """Test that interest rate data exists and has required columns."""
    data_dir = _get_repo_root() / "data"
    rates_path = data_dir / "interest_rates_monthly.csv"
    if not rates_path.exists():
        raise FileNotFoundError(
            f"Missing {rates_path}. Run fetch_interest_rates.py."
        )
    df = pd.read_csv(rates_path)
    required_cols = {"date", "mortgage_30y", "prime_rate"}
    assert required_cols.issubset(set(df.columns)), (
        f"Missing columns. Expected {required_cols}, got {set(df.columns)}"
    )
    assert len(df) > 0, "Interest rate file is empty"
