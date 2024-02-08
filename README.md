# hezar-api

<div align="center">

![Python Version](https://img.shields.io/badge/Python-3.11-yellow)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/rezashabrang/hezar-api/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/rezashabrang/hezar-api/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/rezashabrang/hezar-api/releases)
[![License](https://img.shields.io/badge/License-MIT-blue)](https://github.com/rezashabrang/hezar-api/blob/master/LICENSE)
![Coverage Report](assets/images/coverage.svg)

<b>Inference API Wrapper for Hezar.</b>

</div>

## Installation

- You need [Docker](https://docs.docker.com/engine/install/) installed on your machine.
- Login to [Github Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry).

```bash
docker login ghcr.io
```

- Pull the image

```bash
docker pull ghcr.io/rezashabrang/hezar-api
```

- Run the image

```bash
docker run -p 8080:80 \
    -e LOG_LEVEL=DEBUG \
    -e DOMAIN=NLP \
    -e MODEL_NAME=hezarai/bert-fa-sentiment-dksf \
    ghcr.io/rezashabrang/hezar-api

```

Change `MODEL_NAME` accordingly. Currently only `NLP` domain is supported.

- Go to [localhost:8080](localhost:8080)
