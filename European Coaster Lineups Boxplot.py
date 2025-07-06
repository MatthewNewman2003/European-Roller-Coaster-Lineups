import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("European Coaster Lineups.csv")

sns.boxplot(x=df["Park"], y=df["Rating out of 10"] )

plt.show()
