from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.exponential(scale=100, size=1000), kind="kde")

plt.show()
