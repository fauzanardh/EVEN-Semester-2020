import pandas as pd
import matplotlib.pyplot as plt

# Reading csv data
df = pd.read_csv("dataset/automobile.csv")

# Replacing NaN to 0
df.fillna(0, inplace=True)

# Grouping by company
company = df.groupby("company")

# Getting the average price of every company
prices = company.price
averages = prices.sum()/prices.count()

# Changing the plot size to make it more readable
plt.figure(figsize=(8.0, 4.0))

# Sorting and plotting the averages
ax = averages.sort_values().plot(marker="o")


# Rotating the ticks
plt.xticks(rotation=45)

# Showing the plot
plt.show()
