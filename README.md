# Finstruments: Financial Instruments

`finstruments` is a Python library designed for modeling financial instruments. It comes with the core financial
instruments, such as forwards and options, out of the box, as well as position, trade, and portfolio models.
`finstruments` comes with the basic building blocks, making it easy to extend and build new instruments for any asset
class. These building blocks also provide the functionality to serialize and deserialize to and from JSON, enabling the
ability to store a serialized format in a document database. This library is ideal for quantitative researchers,
traders, and developers who need a streamlined way to build and interact with financial instruments.

## Key Features

- Support for various financial instruments, including options, forwards, and custom instrument extensions.
- Functions for date handling, business day calculations, and other financial operations.
- Serialization and deserialization capabilities for easy conversion between data formats.
- Automatically handles complex calculations like option payoffs and date conventions.
- Lightweight and dependency-minimized where possible.

## Serialization and Deserialization

`finstruments` includes built-in support for serialization and deserialization of financial instruments, making it easy
to save and load objects in formats like JSON. This feature allows users to easily store the state of financial
instruments, share data between systems, or integrate with other applications.

## Installation

Install `finstruments` using `pip`:

```bash
pip install finstruments
```

## Usage

An equity option requires a `BaseEquity` instrument object (e.g. `CommonStock`) as input for the underlying field. The
payoff (`VanillaPayoff`, `DigitalPayoff`) and exercise_type (`EuropeanExerciseStyle`, `AmericanExerciseStyle`,
`BermudanExerciseStyle`) fields need to be populated with objects as well.

```python
from datetime import date

from finstruments.common.enum import Currency
from finstruments.instrument.common.cut import NysePMCut
from finstruments.instrument.common.exercise_style import AmericanExerciseStyle
from finstruments.instrument.common.option.enum import OptionType
from finstruments.instrument.common.option.payoff import VanillaPayoff
from finstruments.instrument.equity import EquityOption, CommonStock

equity_option = EquityOption(
    underlying=CommonStock(ticker='AAPL'),
    payoff=VanillaPayoff(
        option_type=OptionType.PUT,
        strike_price=100
    ),
    exercise_type=AmericanExerciseStyle(
        minimum_exercise_date=date(2022, 1, 3),
        expiration_date=date(2025, 1, 3),
        cut=NysePMCut()
    ),
    denomination_currency=Currency.USD,
    contract_size=100
)
```

## Linting and Code Formatting

This project uses [black](https://github.com/psf/black) for code linting and auto-formatting. If the CI pipeline fails
at the linting stage, you can auto-format the code by running:

```bash
# Install black if not already installed
pip install black

# Auto-format code
black ./finstruments
```

## Documentation

We use [pdoc3](https://pdoc3.github.io/pdoc/) to automatically generate documentation. All Python code must follow
the [Google docstring format](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) for
compatibility with `pdoc3`.

### Generating HTML Documentation

To generate the documentation in HTML format, run:

```bash
pdoc3 --html ./finstruments/ --output-dir ./docs/generated --force
```

### Generating Markdown Documentation

To generate the documentation in Markdown format, run:

```bash
pdoc3 ./finstruments/ --template-dir ./docs/templates --output-dir ./docs/md --force --config='docformat="google"'
```

## Contributing

We welcome contributions! If you have suggestions, find bugs, or want to add features, feel free to open an issue or
submit a pull request.

### Setting Up a Development Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/kyleloomis/finstruments.git
   ```

2. Install dependencies:
   ```bash
   pip install .
   ```

3. Run the tests to ensure everything is set up correctly:
   ```bash
   pytest
   ```

## Help and Support

For help or feedback, please reach out via email at [kyle@spotlight.dev](mailto:kyle@spotlight.dev).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
