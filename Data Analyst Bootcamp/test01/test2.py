import random
from matplotlib import pyplot as plt

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y)

x_scale = []
for i in range(0, 120, 4):
    x_scale.append(i/)

print(x_scale)

plt.xticks(x_scale)
plt.yticks(y)
plt.savefig("./test2.png")
