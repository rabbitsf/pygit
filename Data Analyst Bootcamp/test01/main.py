from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [15, 13, 14, 5, 17, 20, 25, 26, 26, 24, 22, 18]

# Define figure size
fig = plt.figure(figsize=(20, 8), dpi=80)

# Plot
plt.plot(x, y)

#scale setup. Parameter inside could be a list
plt.xticks(x)
plt.yticks(range(1, 30))

# Save the plot to local computer
plt.savefig("./test.png")

# Show the plot if needed
# plt.show()