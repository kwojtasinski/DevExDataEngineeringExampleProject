from polars import col


def aggregate_orders(orders):
    return orders.groupby('dish').sum()

def filter_dishes_by_spice(dishes, spice):
    return dishes.filter(col('spices').contains(spice))