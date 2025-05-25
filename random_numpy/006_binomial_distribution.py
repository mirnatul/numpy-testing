from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# total (n=10)
# number near (n*0.5 = 5)
x = random.binomial(n=10, p=0.5, size=1000)
print(x)

sns.displot(x)
plt.show()
