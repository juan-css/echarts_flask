from datetime import datetime, timedelta
import numpy as np
# import random


# def generate_data():

#     # Setting the base date and one day in seconds
#     base_date = datetime(1988, 10, 3)
#     one_day = timedelta(days=1)

#     # Generating the data
#     data = []
#     for i in range(20000):
#         if i == 0:
#             # For the first item, randomize the second value
#             data_point = [base_date.timestamp() * 1000, random.random() * 300]
#         else:
#             # For subsequent items, base the second value on the previous one
#             data_point = [
#                 (base_date + i*one_day).timestamp() * 1000,
#                 round((random.random() - 0.5) * 20 + data[i-1][1])
#             ]
#         data.append(data_point)

#     return data


def generate_data():

    # Re-initialize after reset
    base_date = datetime(1988, 10, 3)
    one_day = timedelta(days=1)

    # Generate line plot data
    line_data = []
    for i in range(365):  # Using 365 data points, one for each day of a year
        date = (base_date + i*one_day).timestamp() * 1000  # Timestamp in milliseconds
        value = round((np.random.random() - 0.5) * 20 + 100)  # Random value around 100
        line_data.append([date, value])

    # Generate heatmap data
    heatmap_data = []
    for i, item in enumerate(line_data):
        day_value = item[1]  # Same value as the line plot for simplicity
        for hour in range(24):  # 24 data points per day for hourly values
            heatmap_value = day_value + round((np.random.random() - 0.5) * 5)
            heatmap_data.append([i, hour, heatmap_value if heatmap_value > 0 else 0])  # Ensure values are non-negative

    return line_data, heatmap_data
