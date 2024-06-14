import datetime

from sample_data_product.extract import (
    extract_dishes_data,
    extract_orders_data,
    extract_people_data,
)


def test_extract_people_data() -> None:
    """Test extract_people_data function."""
    num_rows = 10
    start_date = datetime.date(1950, 1, 1)
    end_date = datetime.date(2000, 1, 1)
    people = extract_people_data(
        start_date=start_date,
        end_date=end_date,
        limit=num_rows,
    )
    assert len(people) == num_rows
    assert people.columns == ["name", "birthdate", "email", "phone"]


def test_extract_dishes_data() -> None:
    """Test extract_dishes_data function."""
    num_rows = 10
    dishes = extract_dishes_data(limit=num_rows)
    assert len(dishes) == num_rows
    assert dishes.columns == ["name", "vegetables", "fruits", "spices"]


def test_extract_orders_data() -> None:
    """Test extract_orders_data function."""
    num_rows = 10
    start_date = datetime.date(1960, 1, 1)
    end_date = datetime.date(2000, 1, 10)
    people = extract_people_data(
        start_date=start_date,
        end_date=end_date,
        limit=num_rows,
    )
    dishes = extract_dishes_data(limit=num_rows)
    orders = extract_orders_data(
        people=people,
        dishes=dishes,
        start_date=start_date,
        end_date=end_date,
        limit=num_rows,
    )
    assert len(orders) == num_rows
    assert orders.columns == ["person", "dish", "datetime", "quantity"]
