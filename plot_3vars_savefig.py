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

# Assuming MFLOP/s metrics are in the second, third, and fourth columns
mflops_code1 = df[var_names[1]].values.tolist()
mflops_code2 = df[var_names[2]].values.tolist()
mflops_code3 = df[var_names[3]].values.tolist()

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
