import pandas as pd
import matplotlib.pyplot as plt

plot_fname = "myplot.png"

fname = "sample_data_3vars.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

print("var names =", var_names)

# Assuming the problem size is in the first column
problem_sizes = df[var_names[0]].values.tolist()

# Simulating % peak memory bandwidth utilized for each code
# This is a placeholder calculation; adjust based on actual data or calculations
memory_bandwidth_code1 = [problem_size * 0.1 for problem_size in problem_sizes]
memory_bandwidth_code2 = [problem_size * 0.2 for problem_size in problem_sizes]
memory_bandwidth_code3 = [problem_size * 0.3 for problem_size in problem_sizes]

plt.figure()

plt.title("Problem Size vs. % Peak Memory Bandwidth Utilized for 3 Codes")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)

# Plotting % peak memory bandwidth utilized for each code
plt.plot(memory_bandwidth_code1, "r-o", label=var_names[1])
plt.plot(memory_bandwidth_code2, "b-x", label=var_names[2])
plt.plot(memory_bandwidth_code3, "g-^", label=var_names[3])

plt.xlabel("Problem Sizes")
plt.ylabel("% Peak Memory Bandwidth Utilized")

plt.legend(loc="best")

plt.grid(axis='both')

# Save the figure before trying to show the plot
plt.savefig(plot_fname, dpi=300)

plt.show()
