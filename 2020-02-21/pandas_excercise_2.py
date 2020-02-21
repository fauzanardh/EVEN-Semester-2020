import scipy as sp
import pandas as pd
from scipy import stats


df = pd.read_csv("dataset/automobile.csv")

# Print first and last five rows
print("\nFIRST AND LAST 5 ROWS")
print(df.head(5))
print(df.tail(5))

# Find the null values and fill it with zeroes
print("\nFIND AND FILL THE NULL")
df.fillna(0, inplace=True)
print(f"RESULT:\n{df}")

# Find the most expensive car company name
max_index = df.price.idxmax()
print("\nMOST EXPENSIVE CAR")
print(df.iloc[max_index].company)

# Print all Toyota cars details
toyota = df[df.company == "toyota"]
print("\nALL TOYOTA CARS")
print(toyota)

# Count total cars per company
company = df.groupby("company")
print("\nTOTAL CARS PER COMPANY")
print(company.index.count())

# Find each company’s highest price car
company = df.groupby("company")
print("\nHIGHEST CARS FOR EACH COMPANY")
print(company.price.max())

# Find the average mileage of each car making company
company = df.groupby("company")
mileage = company["average-mileage"]
print("\nAVERAGE MILEAGE OF EACH COMPANY")
print(mileage.sum()/mileage.count())

# Create a new variable which contains the last 20 rows of the original table
last20 = df.tail(20)
print("\nLAST 20 ROWS")
print(last20)
