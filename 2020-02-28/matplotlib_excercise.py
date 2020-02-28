import pandas as pd
import matplotlib.pyplot as plt
import numpy.random

# Reading csv data
df = pd.read_csv("dataset/automobile.csv")

# Replacing NaN to 0
df.fillna(0, inplace=True)

# Initializing the plot
fig, axis = plt.subplots(nrows=3)
fig.set_size_inches((10, 15))

# Grouping data by company
company = df.groupby("company")

# Getting total cars for each company
cars_count = company.index.count()

# Plotting data
cars_count.plot(kind="bar", width=0.9, ax=axis[0],
                title="Number of cars produced by each car maker company")
df.price.plot(kind="hist", ax=axis[1], color="gold", edgecolor="black", bins=40,
              title="The Histogram of car prices")
df.plot(kind="scatter", ax=axis[2], color=numpy.random.RandomState(0).rand(61), x="length", y="wheel-base", cmap="hsv",
        title="Length vs wheel base")

# Rotating the ticks of the first subplot
plt.sca(axis[0])
plt.xticks(rotation=90)

# Showing the plot
plt.tight_layout()
plt.show()
