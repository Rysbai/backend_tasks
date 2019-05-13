import matplotlib.pyplot as plt

input_values = list(range(0, 360, 10))

y_values = [
    0.16, 0.37, 0.51, 0.62, 0.69, 0.73, 0.77, 0.78, 0.78, 0.77, 0.75, 0.73, 0.70, 0.65, 0.55, 0.43, 0.25, 0.05,
    0.39, 0.53, 0.63, 0.69, 0.73, 0.75, 0.77, 0.78, 0.78, 0.75, 0.73, 0.68, 0.60, 0.50, 0.37, 0.11, 0.03, 0.12
]

plt.plot(input_values, y_values, linewidth=5)

plt.show()
plt.savefig("optic_lab.png")