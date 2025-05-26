from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.rayleigh(scale=2, size=1000), kind="kde")

plt.show()
