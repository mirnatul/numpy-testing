from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


x = random.normal(size=(2, 3))
# print(x)

# Center 5 and spread +- 10 in (2x3) matrix
y = random.normal(loc=30, scale=1, size=(100))

print(y)

sns.displot(y)
sns.displot(y, kind="kde")
plt.show()
