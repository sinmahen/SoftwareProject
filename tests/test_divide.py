# Edited and created by Muazam Syed

import json
import os
import time
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

FIXTURE_PATH = os.path.join("tests", "fixtures", "divide_cases.json")

def load_cases():
    with open(FIXTURE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# Test #1: Smoke Test: To make sure that the endpoint is up and returns a quotient
def test_divide_smoke_endpoint():
    resp = client.get("/divide", params={"a": 6, "b": 2})
    assert resp.status_code == 200

    data = resp.json()
    assert data["operation"] == "divide"
    assert "result" in data

# Test #2: Functional Test: To make sure that simple division works
@pytest.mark.parametrize("case", load_cases()["valid_cases"])
def test_divide_functional_simple_division(case):
    resp = client.get("/divide", params={"a": case["a"], "b": case["b"]})
    assert resp.status_code == 200

    data = resp.json()
    assert data["operation"] == "divide"
    assert data["result"] == case["expected"]

# Test #3: Non-Functional Test: To make sure the function runs in 200 ms
def test_divide_nonfunctional_response_time():
    start = time.perf_counter()
    resp = client.get("/divide", params={"a": 20, "b": 5})
    end = time.perf_counter()

    assert resp.status_code == 200

    elapsed_ms = (end - start) * 1000
    assert elapsed_ms < 200

# Test #4: Functional Test: To make sure dividing by zero returns a status code
@pytest.mark.parametrize("case", load_cases()["zero_division_cases"])
def test_divide_functional_divide_by_zero(case):
    resp = client.get("/divide", params={"a": case["a"], "b": case["b"]})
    assert resp.status_code == 400

    data = resp.json()
    assert "detail" in data
