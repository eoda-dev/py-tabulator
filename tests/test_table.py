import pytest
from pandas import DataFrame
from pydantic import BaseModel
from pytabulator import Tabulator
from pytabulator._table_options_dc import TableOptionsDC as TableOptionsDC

# from pytabulator import TableOptions as TableOptionsPydantic
from pytabulator._table_options_pydantic import TableOptionsPydantic


@pytest.fixture
def df() -> DataFrame:
    data = [["Hans", "22"], ["Peter", [23]]]
    return DataFrame(data, columns=["Name", "Age"])


def test_table_dc(df: DataFrame) -> None:
    # Prepare
    table_options = TableOptionsDC(selectable_rows=3)

    # Act
    table = Tabulator(df, table_options=table_options)
    table_dict = table.to_dict()
    print(table_dict)

    # Assert
    assert list(table_dict.keys()) == ["schema", "data", "options"]
    assert isinstance(table_dict["options"], dict)
    # assert hasattr(table.table_options, "__dataclass_fields__")


def test_table_pydantic(df: DataFrame) -> None:
    # Prepare
    table_options = TableOptionsPydantic(selectable_rows=3)

    # Act
    table = Tabulator(df, table_options=table_options)
    table_dict = table.to_dict()
    print(table_dict)

    # assert isinstance(table.table_options, BaseModel)
    # print("pydantic", type(table.table_options))
    assert list(table_dict.keys()) == ["schema", "data", "options"]
    assert isinstance(table_dict["options"], dict)
