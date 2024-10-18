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
to
save and load objects in formats like JSON. This feature allows users to easily store the state of financial
instruments, share data between systems, or integrate with other applications.

## Installation

Install `finstruments` using `pip`:

```bash
pip install finstruments
```

## Usage Examples

Below are some examples demonstrating how to use the library for different financial tasks.

### Example 1: Calculating Business Days Between Two Dates

```python
from finstruments.common.date import create_dates_between
from datetime import date

# Define start and end dates
start_date = date(2024, 1, 1)
end_date = date(2024, 1, 31)

# Get business days between the two dates
business_days = create_dates_between(start=start_date, end=end_date, frequency="B")
print("Business Days:", business_days)
```

### Example 2: Option Payoff Calculation

```python
from finstruments.instrument.common.option import OptionType, calculate_payoff

# Define option parameters
strike_price = 100
market_price = 105
option_type = OptionType.CALL

# Calculate payoff for a call option
payoff = calculate_payoff(market_price, strike_price, option_type)
print("Option Payoff:", payoff)
```

### Example 3: Creating a Forward Contract

```python
from finstruments.instrument.forward import ForwardContract
from datetime import date

# Create a forward contract
contract = ForwardContract(
    underlying_asset="AAPL",
    notional_amount=100000,
    start_date=date(2024, 1, 1),
    end_date=date(2025, 1, 1),
    fixed_rate=0.05
)

# Calculate forward price
forward_price = contract.calculate_forward_price()
print("Forward Price:", forward_price)
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
   git clone https://github.com/yourusername/finstruments.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the tests to ensure everything is set up correctly:
   ```bash
   pytest
   ```

## Help and Support

For help or feedback, please reach out via email at [kyle@spotlight.dev](mailto:kyle@spotlight.dev).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
