# py-tabulator

Shiny bindings for tabulator JS

## Installation

```bash
pip install git+https://github.com/eodaGmbH/py-tabulator
```

## Getting started

Shiny Express:

```python
import pandas as pd
from shiny import render
from shiny.express import input, ui
from tabylator import render_tabular


@render.code
async def txt():
    print(input.tabylator_row())
    return input.tabylator_row()["Name"]


@render_tabular
def tabylator():
    return pd.read_csv(
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )
```

```bash
shiny run docs/examples/getting_started/shiny_express.py
```