import random
import mimesis

import polars as pl

def extract_people_data(start_date, end_date, limit):
    person = mimesis.Person()
    people = []
    for idx in range(100):
        people.append({'name': person.full_name(),'birthdate': person.birthdate(min_year=1960, max_year=2000),'email': person.email(),'phone': person.telephone(),})
    return pl.DataFrame(people)

def extract_dishes_data(limit):
    product = mimesis.Food()
    products = []
    for idx in range(100):
        products.append({
            'name': product.dish(),
            "vegetables": [product.vegetable() for idx in range(3)],
            "fruits": [product.fruit() for idx in range(3)],
            "spices": [product.spices() for idx in range(3)]
        })
    return pl.DataFrame(products)

def extract_orders_data(people, products, start_date, end_date, limit):
    orders = []
    for idx in range(100):
        random_person = people.sample(n=1)
        random_dish = products.sample(n=1)
        orders.append({
            'person': random_person.get_column("name")[0],
            'dish': random_dish.get_column("name")[0],
            'datetime': mimesis.Datetime().datetime(start=start_date.year, end=end_date.year),
            'quantity': random.randint(1, 5),
        })
    return pl.DataFrame(orders)


