from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_float_dtype,
    is_integer_dtype,
)
from src.endpoints import X


def test_schema(json_metadata):
    typechecks = {
        "Loan Amount": is_integer_dtype,
        "Funded Amount": is_integer_dtype,
        "Term": is_integer_dtype,
        "Employment Length": is_categorical_dtype,
        "Home Ownership": is_categorical_dtype,
        "Annual Income": is_float_dtype,
        "Issue Date": is_datetime64_any_dtype,
        "Purpose": is_categorical_dtype,
        "Debt-to-Income Ratio": is_float_dtype,
    }

    # assert correct columns are present
    assert set(typechecks.keys()) == set(X.columns)

    # assert correct column types
    for col, typecheck in typechecks.items():
        assert typecheck(X[col])

    json_metadata["section"] = "Data"
    json_metadata["pass_message"] = f"Column names and column types are correct"
    json_metadata["fail_message"] = f"Incorrect schema"
