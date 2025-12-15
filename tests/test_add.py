# Edited and created by Van Dong Nguyen

import json
import os
import time
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

FIXTURE_PATH = os.path.join("tests", "fixtures", "add_cases.json")

def load_cases():
    with open(FIXTURE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# Test #1: Smoke Test: Ensure the add endpoint is available and returns a sum
def test_add_smoke_endpoint():
    resp = client.get("/add", params={"a": 4, "b": 7})
    assert resp.status_code == 200

    data = resp.json()
    assert data["operation"] == "add"
    assert "result" in data

# Test #2: Functional Test: Verify addition works for valid inputs
@pytest.mark.parametrize("case", load_cases()["valid_add_cases"])
def test_add_functional_valid_inputs(case):
    resp = client.get("/add", params={"a": case["a"], "b": case["b"]})
    assert resp.status_code == 200

    data = resp.json()
    assert data["operation"] == "add"
    assert data["result"] == case["expected"]

# Test #3: Non-Functional Test: Ensure response time is under 200 ms
def test_add_nonfunctional_response_time():
    start = time.perf_counter()
    resp = client.get("/add", params={"a": 100, "b": 250})
    end = time.perf_counter()

    assert resp.status_code == 200

    elapsed_ms = (end - start) * 1000
    assert elapsed_ms < 200

# Test #4: Functional Test: Ensure invalid input returns an error response
@pytest.mark.parametrize("case", load_cases()["invalid_add_cases"])
def test_add_functional_invalid_input(case):
    resp = client.get("/add", params={"a": case["a"], "b": case["b"]})
    assert resp.status_code == 400

    data = resp.json()
    assert "detail" in data
