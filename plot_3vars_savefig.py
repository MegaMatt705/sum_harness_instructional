import pandas as pd
import matplotlib.pyplot as plt

plot_fname = "myplot.png"

fname = "sample_data_3vars.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

print("var names =", var_names)

# Assuming the % peak memory bandwidth utilized metric is in the second column
memory_bandwidth = df[var_names[1]].values.tolist()

plt.figure()

plt.title("Problem Size vs. % Peak Memory Bandwidth Utilized")

# Assuming the problem size is in the first column
problem_sizes = df[var_names[0]].values.tolist()

plt.plot(problem_sizes, memory_bandwidth, "r-o")

plt.xlabel("Problem Sizes")
plt.ylabel("% Peak Memory Bandwidth Utilized")

plt.grid(axis='both')

# Save the figure before trying to show the plot
plt.savefig(plot_fname, dpi=300)

plt.show()
