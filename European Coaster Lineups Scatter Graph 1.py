import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

DataFrame = pd.read_csv("European Coaster Lineups.csv")

plt.scatter(DataFrame["Scoreable Coaster Quantity"], DataFrame["Rating out of 10"])

plt.xlabel("Scoreable Coaster Quantity")
plt.ylabel("Rating out of 10");

plt.show()
