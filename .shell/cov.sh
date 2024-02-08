#!/bin/bash
find . -name 'coverage.txt' -delete
poetry run pytest --cov-report term --cov hezar_api tests/ >>.logs/coverage.txt
