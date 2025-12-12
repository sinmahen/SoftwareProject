from fastapi import FastAPI, HTTPException
from calculator import add, subtract, multiply, divide

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/add")
def add_endpoint(a: float, b: float):
    result = add(a, b)
    return {
        "operation": "add",
        "a": a,
        "b": b,
        "result": result
    }

@app.get("/subtract")
def subtract_endpoint(a: float, b: float):
    result = subtract(a, b)
    return {
        "operation": "subtract",
        "a": a,
        "b": b,
        "result": result
    }

@app.get("/multiply")
def multiply_endpoint(a: float, b: float):
    result = multiply(a, b)
    return {
        "operation": "multiply",
        "a": a,
        "b": b,
        "result": result
    }

@app.get("/divide")
def divide_endpoint(a: float, b: float):
    try:
        result = divide(a, b)
        return {
            "operation": "divide",
            "a": a,
            "b": b,
            "result": result
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
