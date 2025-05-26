from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.logistic(size=1000)
sns.displot(x, kind="kde")
plt.show()
