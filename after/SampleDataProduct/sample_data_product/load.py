import polars as pl


def load_dataframe_to_delta(df: pl.DataFrame, path: str, mode: str) -> None:
    """Save DataFrame to Delta Lake.

    :param df: DataFrame to save.
    :param path: Path to save DataFrame.
    :param mode: Mode to save DataFrame.
    """
    df.write_delta(target=path, mode=mode)
