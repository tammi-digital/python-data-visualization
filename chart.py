import matplotlib.pyplot as plt
import csv

days = []
sales = []

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        days.append(row["day"])
        sales.append(int(row["sales"]))

plt.bar(days, sales, color='skyblue')
plt.title("Sales per Day")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.show()
