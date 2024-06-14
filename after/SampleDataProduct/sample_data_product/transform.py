import polars as pl
from polars import col


def aggregate_orders(orders: pl.DataFrame) -> pl.DataFrame:
    """Aggregate orders by dish.

    :param orders: Orders DataFrame.
    :return: DataFrame with aggregated orders.
    """
    return orders.group_by("dish").sum().drop("person", "datetime")


def filter_dishes_by_spice(dishes: pl.DataFrame, spice: str) -> pl.DataFrame:
    """Filter dishes by spice.

    :param dishes: Dishes DataFrame.
    :param spice: Spice to filter by.
    :return: DataFrame with filtered dishes.
    """
    return dishes.filter(col("spices").list.contains(spice))
