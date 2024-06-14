import polars as pl

from sample_data_product.extract import extract_dishes_data
from sample_data_product.load import load_dataframe_to_delta


def test_load_dishes_data_to_delta(tmpdir) -> None:  # noqa: ANN001
    """Test load dishes data to Delta Lake."""
    num_rows = 10000
    dishes = extract_dishes_data(limit=num_rows)
    path = f"{tmpdir}/dishes"
    load_dataframe_to_delta(df=dishes, path=path, mode="overwrite")
    assert dishes.equals(pl.read_delta(path))
