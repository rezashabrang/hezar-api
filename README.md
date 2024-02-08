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

<b>Inference API Wrapper for [Hezar](https://github.com/hezarai/hezar).</b>

</div>

## Installation

- You need [Docker](https://docs.docker.com/engine/install/)and [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine.
- Clone the project.

```bash
git clone git@github.com:rezashabrang/hezar-api.git
```

- Build the image.

```bash
docker compose -f docker-compose-dev.yml build
```

- Run the image

```bash
docker compose -f docker-compose-dev.yml up
```

In the `.env.dev` file, change `MODEL_NAME` accordingly. Currently only `NLP` domain is supported.

- Go to [localhost:8080/docs](localhost:8080/docs)
