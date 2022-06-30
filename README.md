# mos-cli

MOS command-line interface.

## Installation

```
pip install mos-cli
```

## Documentation

```
mosctl --help
mosctl SUBCOMMAND --help
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
