import random
import numpy as np
from matplotlib import pyplot as plt

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y)

# x_mark = np.arange(10, 13, 0.25)
plt.xticks(x)
plt.yticks(y)
plt.savefig("./test2.png")
