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

# Assuming time for each code is in the second, third, and fourth columns
code1_time = df[var_names[1]].values.tolist()
code2_time = df[var_names[2]].values.tolist()
code3_time = df[var_names[3]].values.tolist()

# Calculate MFLOP/s for each code
mflops_code1 = [problem_sizes[i] / code1_time[i] / 1e6 for i in range(len(problem_sizes))]
mflops_code2 = [problem_sizes[i] / code2_time[i] / 1e6 for i in range(len(problem_sizes))]
mflops_code3 = [problem_sizes[i] / code3_time[i] / 1e6 for i in range(len(problem_sizes))]

plt.figure()

plt.title("Problem Size vs. MFLOP/s for 3 Codes")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)

# Plotting MFLOP/s for each code
plt.plot(mflops_code1, "r-o", label=var_names[1])
plt.plot(mflops_code2, "b-x", label=var_names[2])
plt.plot(mflops_code3, "g-^", label=var_names[3])

plt.xlabel("Problem Sizes")
plt.ylabel("MFLOP/s")

plt.legend(loc="best")

plt.grid(axis='both')

# Save the figure before trying to show the plot
plt.savefig(plot_fname, dpi=300)

plt.show()
