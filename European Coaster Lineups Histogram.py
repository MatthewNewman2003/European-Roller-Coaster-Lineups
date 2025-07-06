import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("European Coaster Lineups.csv")

sns.histplot(x = "Park", y="Rating out of 10", data = df)

plt.show()
