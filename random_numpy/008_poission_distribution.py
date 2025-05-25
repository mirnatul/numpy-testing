from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.poisson(lam=2, size=1000)
sns.displot(x)

plt.show()
