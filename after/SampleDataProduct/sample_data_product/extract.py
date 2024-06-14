import random
from datetime import datetime

import mimesis
import polars as pl


def extract_people_data(
    start_date: datetime.date,
    end_date: datetime.date,
    limit: int,
) -> pl.DataFrame:
    """Extract people data.

    :param start_date: Start date for birthdate.
    :param end_date: End date for birthdate.
    :param limit: Number of people to generate.
    :return: DataFrame with people data.
    """
    person = mimesis.Person()
    people = [
        {
            "name": person.full_name(),
            "birthdate": person.birthdate(
                min_year=start_date.year,
                max_year=end_date.year,
            ),
            "email": person.email(),
            "phone": person.telephone(),
        }
        for _ in range(limit)
    ]

    return pl.DataFrame(people)


def extract_dishes_data(limit: int) -> pl.DataFrame:
    """Extract dishes data.

    :param limit: Number of dishes to generate.
    :return: DataFrame with dishes data.
    """
    food = mimesis.Food()
    dishes = []
    for _ in range(100):
        dishes = [
            {
                "name": food.dish(),
                "vegetables": [food.vegetable() for _ in range(3)],
                "fruits": [food.fruit() for _ in range(3)],
                "spices": [food.spices() for _ in range(3)],
            }
            for _ in range(limit)
        ]
    return pl.DataFrame(dishes)


def extract_orders_data(
    people: pl.DataFrame,
    dishes: pl.DataFrame,
    start_date: datetime.date,
    end_date: datetime.date,
    limit: int,
) -> pl.DataFrame:
    """Extract orders data.

    :param people: DataFrame with people data.
    :param dishes: DataFrame with dishes data.
    :param start_date: Start date for order datetime.
    :param end_date: End date for order datetime.
    :param limit: Number of orders to generate.
    :return: DataFrame with orders data.
    """
    orders = [
        {
            "person": people.sample(n=1).get_column("name")[0],
            "dish": dishes.sample(n=1).get_column("name")[0],
            "datetime": mimesis.Datetime().datetime(
                start=start_date.year,
                end=end_date.year,
            ),
            "quantity": random.randint(1, 5),
        }
        for _ in range(limit)
    ]
    return pl.DataFrame(orders)
