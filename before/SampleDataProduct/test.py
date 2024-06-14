import datetime
from sample_data_product.extract import extract_people_data, extract_orders_data, extract_dishes_data
from sample_data_product.transform import aggregate_orders, filter_dishes_by_spice
from sample_data_product.load import save_dataframe_to_delta
people = extract_people_data(datetime.date(1980, 1, 1), datetime.date(2000, 1, 1), 100) 
print(people)
dishes = extract_dishes_data(100)
print(dishes)
orders = extract_orders_data(people, dishes, datetime.date(2020, 1, 1), datetime.date(2020, 1, 31), 100)
print(orders)
aggregation = aggregate_orders(orders)
print(aggregation)
save_dataframe_to_delta(aggregation, 'aggregated_orders')
print(dishes.select('spices').head())

filtered_spices = filter_dishes_by_spice(dishes, 'Saffron')
print(filtered_spices)