# rest_app_template


## Getting started
Проект предназначен для ознакомления с принципами разработки REST-приложений с покрытием юнит и функциональных тестов.


## How to run app locally?

```
git clone
cd rest_app_template
pip install poetry && poetry install
python main.py
```

## Hot to run unit-tests?
```
pytest -v tests/unit

OR

poetry run pytest -v tests/unit
```

## How to build local docker image?
```
make build
```

## How to run functional tests?
```
cd tests/functional && chmod +x run.local.sh && ./run.local.sh
cd -
```
