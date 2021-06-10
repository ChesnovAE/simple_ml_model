# simple_ml_model
[![Build Status](http://194.67.111.68:8081/job/test_folder/job/test_multibranch/job/master/badge/icon)](http://194.67.111.68:8081/job/test_folder/job/test_multibranch/job/master/)


This is the abstract ml project for testing [MLops pipeline](https://github.com/ChesnovAE/MLops_setup)

## Prerequisites

- conda
- docker

## Installation

```bash
pip3 install -r requirements.txt
```

## Usage

```bash
python3 app.py -h
```

## Usage via docker

```bash
docker build -t simple_ml:latest .
```

```bash
docker run simple_ml -h
```
