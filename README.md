# mos-cli

MOS command-line interface.

## Installation

```
pip install mos-cli
```

## Documentation

Click here to view the documentation:

[![Documentation](https://github.com/Fuinn/mos-cli/actions/workflows/documentation.yml/badge.svg?branch=master)](https://Fuinn.github.io/mos-cli)

Or, use commands of the following form from the terminal:

```
mosctl --help
mosctl SUBCOMMAND1 ... SUBCOMMANDN --help
```

## Examples

### Get user token
```
mosctl --url 'http://localhost:8000/api' user get-token USERNAME PASSWORD
```

### Get model status
```
mosctl --url 'http://localhost:8000/api' --token TOKEN model --name 'MODEL NAME' get-status
```
