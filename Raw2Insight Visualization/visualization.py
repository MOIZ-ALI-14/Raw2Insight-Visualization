import matplotlib.pyplot as plt
import pandas as pd

# Pandas is used to load and handle the café sales data in a DataFrame.
# Matplotlib is used to create and customize the different visualizations.
cafe_sales_data = pd.read_csv("data/clean_cafe_sales.csv")
print(cafe_sales_data.head())  # checking whether data is loaded successfully or not

# ---------------- Line Chart ----------------

# We create a separate Figure and Axes for the line chart.
# Using the Object-Oriented API makes it easier to control each chart separately.
fig, line_chart = plt.subplots(figsize=(8, 5))

# Checking the column names and data types to understand the structure of our data.
print(cafe_sales_data.columns)
print(cafe_sales_data.dtypes)

# Transaction Date is initially read as text, so we convert it into datetime format.
# This allows us to work properly with months, days, years, and other date operations.
cafe_sales_data["Transaction Date"] = pd.to_datetime(
    cafe_sales_data["Transaction Date"]
)
print(cafe_sales_data.dtypes)

# We group the transactions by month and calculate the total sales for each month.
# The month number is used so that we can show the sales trend from January to December.
monthly_sales = cafe_sales_data.groupby(cafe_sales_data["Transaction Date"].dt.month)[
    "Total Spent"
].sum()

# Plotting the monthly sales values as a line chart.
# The month numbers are used on X-axis and the monthly sales are used on Y-axis.
line_chart.plot(
    monthly_sales.index,
    monthly_sales.values,
    color="royalblue",
    marker="o",
    markerfacecolor="white",
    markeredgecolor="royalblue",
    markeredgewidth=2,
    linewidth=2,
    markersize=6,
    label="Monthly Revenue",
)

# Adding labels and title to make the chart easier to understand.
line_chart.set_xlabel("Months", size=13)
line_chart.set_ylabel("Total Sales ($)", size=13)
line_chart.set_title("Monthly Sales Revenue Throughout 2023", size=15)

# Adding a dotted grid to make the sales values easier to read.
line_chart.grid(linestyle=":", linewidth="2", alpha=0.7)

# Replacing month numbers with actual month names on the X-axis.
line_chart.set_xticks(range(1, 13))
line_chart.set_xticklabels(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
)

# Setting readable sales values on the Y-axis.
line_chart.set_yticks(range(6000, 12001, 1000))
line_chart.set_yticklabels(["$6k", "$7k", "$8k", "$9k", "$10k", "$11k", "$12k"])

# Automatically adjusting the spacing between the chart elements.
fig.tight_layout()

# Saving the line chart as a high-resolution PNG image.
fig.savefig("outputs/monthly_sales.png", dpi=300, bbox_inches="tight")


# ---------------- Bar Chart ----------------

# Creating a separate Figure and Axes for the bar chart.
fig, bar_chart = plt.subplots(figsize=(8, 5))

# We group the data by Item because we want to compare the sales of each product.
# Then we select Total Spent and sum all transactions belonging to each product.
sales_by_product = cafe_sales_data.groupby("Item")["Total Spent"].sum()
print(sales_by_product)

# Creating bars where products are on the X-axis and total sales are on the Y-axis.
bar_chart.bar(
    sales_by_product.index,
    sales_by_product.values,
    color="green",
    width=0.5,
    edgecolor="black",
    alpha=0.5,
    label="Total Sales",
)

# Adding labels and title to explain what the bar chart represents.
bar_chart.set_xlabel("Products", size=13)
bar_chart.set_ylabel("Total Sales ($)", size=13)
bar_chart.set_title("Sales by Product", size=15)

# Showing the name of the data represented by the bars.
bar_chart.legend()

# Setting readable values for the Y-axis.
bar_chart.set_yticks(range(0, 20001, 2500))
bar_chart.set_yticklabels(
    ["0", "$2.5k", "$5k", "$7.5k", "$10k", "$12.5k", "$15k", "$17.5k", "$20k"]
)

# Adjusting the spacing before saving the figure.
fig.tight_layout()

# Saving the bar chart separately as a high-resolution PNG image.
fig.savefig("outputs/sales_by_product.png", dpi=300, bbox_inches="tight")


# ---------------- Pie Chart ----------------

# Creating a separate Figure and Axes for the pie chart.
fig, pie_chart = plt.subplots(figsize=(8, 5))

# Counting how many transactions were made using each payment method.
# value_counts() is suitable here because we want the share of each payment category.
payment_methods = cafe_sales_data["Payment Method"].value_counts()
print(payment_methods)

# Creating a pie chart to show how transactions are divided among payment methods.
pie_chart.pie(
    payment_methods.values,
    labels=payment_methods.index,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops={"edgecolor": "black", "linewidth": 1},
    colors=["royalblue", "mediumseagreen", "darkorange"],
    textprops={"fontsize": 11},
    pctdistance=0.6,
    labeldistance=1.1,
)

# Adding a title to explain what the pie chart represents.
pie_chart.set_title("Payment Method Distribution", size=15)

# Adjusting the spacing so the chart fits properly.
fig.tight_layout()

# Saving the pie chart separately as a high-resolution PNG image.
fig.savefig("outputs/payment_method_distribution.png", dpi=300, bbox_inches="tight")


# ---------------- Histogram ----------------

# Creating a separate Figure and Axes for the histogram.
fig, histogram = plt.subplots(figsize=(8, 5))

# We only need the Total Spent column because the histogram shows
# how transaction spending values are distributed across different ranges.
transaction_spending = cafe_sales_data["Total Spent"]

# Creating the histogram using the transaction spending values.
# bins=6 divides the spending values into six numerical ranges.
histogram.hist(
    transaction_spending,
    bins=6,
    color="royalblue",
    edgecolor="black",
    linewidth=1.2,
    alpha=0.7,
    label="Transaction Spending",
)

# Adding labels and title to explain the distribution.
histogram.set_xlabel("Transaction Amount ($)", size=13)
histogram.set_ylabel("Number of Transactions", size=13)
histogram.set_title("Customer Spending Distribution", size=15)

# A Y-axis grid makes it easier to compare the number of transactions in each bin.
histogram.grid(
    axis="y",
    linestyle=":",
    linewidth=1.2,
    alpha=0.7,
)

# Setting readable spending values on the X-axis.
histogram.set_xticks(range(0, 26, 5))
histogram.set_xticklabels(["0", "$5", "$10", "$15", "$20", "$25"])

# Showing the name of the data represented by the histogram.
histogram.legend()

# Adjusting the spacing before saving the figure.
fig.tight_layout()

# Saving the histogram separately as a high-resolution PNG image.
fig.savefig(
    "outputs/customer_spending_distribution.png",
    dpi=300,
    bbox_inches="tight",
)


# ---------------- Scatter Plot ----------------

# Creating a separate Figure and Axes for the scatter plot.
fig, scatter_plot = plt.subplots(figsize=(8, 5))

# Selecting Quantity and Total Spent because we want to see
# whether the transaction quantity has a relationship with transaction value.
quantity = cafe_sales_data["Quantity"]
transaction_spending = cafe_sales_data["Total Spent"]

# Creating a scatter plot where each point represents one transaction.
scatter_plot.scatter(
    quantity,
    transaction_spending,
    color="royalblue",
    edgecolor="black",
    linewidth=0.8,
    alpha=0.6,
    s=50,
    label="Transactions",
)

# Adding labels and title to explain the relationship being shown.
scatter_plot.set_xlabel("Quantity", size=13)
scatter_plot.set_ylabel("Transaction Value ($)", size=13)
scatter_plot.set_title("Quantity vs Transaction Value", size=15)

# Adding a grid to make the positions of individual points easier to read.
scatter_plot.grid(
    axis="both",
    linestyle=":",
    linewidth=1.2,
    alpha=0.7,
)

# Setting the possible quantity values on the X-axis.
scatter_plot.set_xticks(range(1, 6, 1))
scatter_plot.set_xticklabels(["1", "2", "3", "4", "5"])

# Setting readable transaction values on the Y-axis.
scatter_plot.set_yticks(range(0, 26, 5))
scatter_plot.set_yticklabels(["0", "$5", "$10", "$15", "$20", "$25"])

# Showing the name of the data represented by the points.
scatter_plot.legend()

# Adjusting the spacing before saving the figure.
fig.tight_layout()

# Saving the scatter plot separately as a high-resolution PNG image.
fig.savefig(
    "outputs/quantity_vs_transaction_value.png",
    dpi=300,
    bbox_inches="tight",
)
