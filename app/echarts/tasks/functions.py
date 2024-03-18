from datetime import datetime, timedelta
import random


def generate_data():

    # Setting the base date and one day in seconds
    base_date = datetime(1988, 10, 3)
    one_day = timedelta(days=1)

    # Generating the data
    data = []
    for i in range(20000):
        if i == 0:
            # For the first item, randomize the second value
            data_point = [base_date.timestamp() * 1000, random.random() * 300]
        else:
            # For subsequent items, base the second value on the previous one
            data_point = [
                (base_date + i*one_day).timestamp() * 1000,
                round((random.random() - 0.5) * 20 + data[i-1][1])
            ]
        data.append(data_point)

    return data
