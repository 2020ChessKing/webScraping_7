import pandas as pd, plotly.express as px

# Read CSV
df = pd.read_csv("filtered_stars.csv")
Names = df["Name"].to_list()
Radiuses = df["Radius"].to_list()
Masses = df["Mass"].to_list()
Distances = df["Distance"].to_list()

# Plotting
fig_1 = px.bar(df, x="Mass", y="Name", title="Star Name vs Mass")
fig_2 = px.bar(df, x="Radius", y="Name", title="Star Name vs Radius")
fig_3 = px.bar(df, x="Distance", y="Name", title="Star Name vs Distance")
fig_4 = px.bar(df, x="Gravity", y="Name", title="Star Name vs Gravity")

fig_1.show()
fig_2.show()
fig_3.show()
fig_4.show()

# Conclusion :
# Stars Mass and Radius are in strong positive correlation
# Stars Mass (or Radius) and Distance are in strong negative correlation
# Gravity is random and has no correlation