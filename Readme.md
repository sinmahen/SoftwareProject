# Calculator

This program lets you add, subtract, multiply, and devide.

# How to install?

## How to clone the repo?
Use ```git clone https://github.com/sinmahen/SoftwareProject/tree/main```

# how to build and run?
Navigate to the SoftwareProject directory in your terminal, then install the requirements.

## Windows/Linux
```pip install -r requirements.txt```

## macOS
```pip3 install -r requirements.txt --break-system-packages```

## Run the tests

### Windows
```py -m pytest```

### Linux
```python -m pytest```

### macOS
```python3 -m pytest```

# Dirs
```
.
└── SoftwareProject
    ├── .github
    │   └── workflows
    │       ├── ci.yml
    │       ├── production.yml
    │       └── staging.yml
    ├── calculator.py
    ├── docker-compose.yml
    ├── Dockerfile
    ├── docs
    │   ├── CODE_REVIEW_TEMPLATE.md
    │   └── ISSUE_TEMPLATE.md
    ├── main.py
    ├── requirements.txt
    └── tests
        ├── fixtures
        │   ├── add_cases.json
        │   ├── divide_cases.json
        │   ├── multiply_cases.json
        │   └── subtract_cases.json
        ├── test_add.py
        ├── test_divide.py
        ├── test_multiply.py
        └── test_subtract.py
```