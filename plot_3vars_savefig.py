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


memory_latency_code1 = [problem_size * 0.01 for problem_size in problem_sizes]
memory_latency_code2 = [problem_size * 0.02 for problem_size in problem_sizes]
memory_latency_code3 = [problem_size * 0.03 for problem_size in problem_sizes]

plt.figure()

plt.title("Problem Size vs. Memory Latency for 3 Codes")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)

# Plotting memory latency for each code
plt.plot(memory_latency_code1, "r-o", label=var_names[1])
plt.plot(memory_latency_code2, "b-x", label=var_names[2])
plt.plot(memory_latency_code3, "g-^", label=var_names[3])

plt.xlabel("Problem Sizes")
plt.ylabel("Memory Latency")

plt.legend(loc="best")

plt.grid(axis='both')

# Save the figure before trying to show the plot
plt.savefig(plot_fname, dpi=300)

plt.show()
