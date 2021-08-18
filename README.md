# Setup

`pipenv install`

# Running the flow

- `pipenv run python -m mypackage.myflow` works
- `pipenv run prefect run -m mypackage.myflow` raises `No module named 'mypackage'`