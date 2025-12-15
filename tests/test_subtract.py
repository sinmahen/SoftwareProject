# Edited and created by Van Dong Nguyen

import json
import os
import time
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

FIXTURE_PATH = os.path.join("tests", "fixtures", "subtract_cases.json")

def load_cases():
    with open(FIXTURE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# Test #1: Smoke Test: Ensure the subtract endpoint is available
def test_subtract_smoke_endpoint():
    resp = client.get("/subtract", params={"a": 9, "b": 4})
    assert resp.status_code == 200

    data = resp.json()
    assert data["operation"] == "subtract"
    assert "result" in data

# Test #2: Functional Test: Verify subtraction works for valid inputs
@pytest.mark.parametrize("case", load_cases()["valid_subtract_cases"])
def test_subtract_functional_valid_inputs(case):
    resp = client.get("/subtract", params={"a": case["a"], "b": case["b"]})
    assert resp.status_code == 200

    data = resp.json()
    assert data["operation"] == "subtract"
    assert data["result"] == case["expected"]

# Test #3: Non-Functional Test: Ensure response time is under 200 ms
def test_subtract_nonfunctional_response_time():
    start = time.perf_counter()
    resp = client.get("/subtract", params={"a": 200, "b": 50})
    end = time.perf_counter()

    assert resp.status_code == 200

    elapsed_ms = (end - start) * 1000
    assert elapsed_ms < 200

# Test #4: Functional Test: Ensure invalid input returns a validation error
@pytest.mark.parametrize("case", load_cases()["invalid_subtract_cases"])
def test_subtract_functional_invalid_input(case):
    resp = client.get("/subtract", params={"a": case["a"], "b": case["b"]})

    # FastAPI returns 422 for validation errors
    assert resp.status_code == 422

    data = resp.json()
    assert "detail" in data