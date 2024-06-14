import datetime

from sample_data_product.extract import (
    extract_dishes_data,
    extract_orders_data,
    extract_people_data,
)
from sample_data_product.transform import aggregate_orders, filter_dishes_by_spice


def test_filter_dishes_by_spice() -> None:
    """Test filter_dishes_by_spice function."""
    num_rows = 10000
    spice = "Salt"
    dishes = extract_dishes_data(limit=num_rows)
    filtered_dishes = filter_dishes_by_spice(dishes=dishes, spice=spice)
    assert len(filtered_dishes) <= num_rows
    assert filtered_dishes.columns == ["name", "vegetables", "fruits", "spices"]
    assert all(spice in spices for spices in filtered_dishes["spices"].to_list())


def test_aggregate_orders() -> None:
    """Test aggregate_orders function."""
    orders = extract_orders_data(
        people=extract_people_data(
            start_date=datetime.date(1960, 1, 1),
            end_date=datetime.date(2000, 1, 1),
            limit=10,
        ),
        dishes=extract_dishes_data(limit=10),
        start_date=datetime.date(1960, 1, 1),
        end_date=datetime.date(2000, 1, 1),
        limit=10,
    )
    aggregated_orders = aggregate_orders(orders)
    assert len(aggregated_orders) <= len(orders)
    assert aggregated_orders.columns == ["dish", "quantity"]
