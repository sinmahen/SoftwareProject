# Edited by Katie reeves

import json
import os
import time
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

FIXTURE_PATH = os.path.join("tests", "fixtures", "multiply_cases.json")

def load_cases():
    with open(FIXTURE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# Smoke Test
def test_multiply_smoke_endpoint():
    resp = client.get("/multiply", params = {"a": 2, "b": 128})
    assert resp.status_code == 200

    data = resp.json()
    assert data["operation"] == "multiply"
    assert "result" in data

# Functional Test
@pytest.mark.parametrize("case", load_cases()["valid_cases"])
def test_multiply_functional_simple_multiplication(case):
    resp = client.get("/multiply", params={"a": case["a"], "b": case["b"]})
    assert resp.status_code == 200

    data = resp.json()
    assert data["operation"] == "multiply"
    assert data["result"] == case["expected"]

# Non-Functional Test:
def test_multiply_nonfunctional_response_time():
    start = time.perf_counter()
    resp = client.get("/multiply", params = {"a": 2, "b": 128})
    end = time.perf_counter()

    assert resp.status_code == 200

    elapsed_ms = (end - start) * 1000
    assert elapsed_ms < 200

# Functional Test
@pytest.mark.parametrize("case", load_cases()["zero_multiplication_cases"])
def test_multiply_functional_divide_by_zero(case):
    resp = client.get("/multiply", params = {"a": case["a"], "b": case["b"]})
    assert resp.status_code == 400

    data = resp.json()
    assert "detail" in data
