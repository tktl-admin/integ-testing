import numpy as np
from src.endpoints import X, repayment

prob = repayment(X)


def test_mean(json_metadata):
    mean_pred = np.mean(prob)
    assert 0.8 < mean_pred < 0.85
    json_metadata["section"] = "Plausibility"
    json_metadata["pass_message"] = f"Mean prediction is plausible ({mean_pred:.2f})"
    json_metadata["fail_message"] = f"Mean prediction is implausible ({mean_pred:.2f})"


def test_spread_10_90(json_metadata):
    p10 = np.quantile(prob, q=0.10)
    p90 = np.quantile(prob, q=0.90)
    spread = p90 - p10
    assert 0.10 < spread < 0.20
    json_metadata["section"] = "Plausibility"
    json_metadata["pass_message"] = f"10%/90% Spread is plausible ({spread:.2f})"
    json_metadata["fail_message"] = f"10%/90% Spread is implausible ({spread:.2f})"


def test_spread_25_75(json_metadata):
    p25 = np.quantile(prob, q=0.25)
    p75 = np.quantile(prob, q=0.75)
    spread = p75 - p25
    assert 0.025 < spread < 0.05

    json_metadata["section"] = "Plausibility"
    json_metadata["pass_message"] = f"25%/75% Spread is plausible ({spread:.2f})"
    json_metadata["fail_message"] = f"25%/75% Spread is implausible ({spread:.2f})"
