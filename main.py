import numpy as np
import matplotlib.pyplot as plt
from operationclass import IntArray  # Make sure this class is correct

# ------------------------
# Productivity Functions
# ------------------------
def productivity_of_company(order, data_frame):
    """Calculates total products made by a company (row in data_frame)."""
    return np.sum(data_frame[order])

def max_productivity(data_frame):
    best_company = 1
    max_products = 0

    for i, row in enumerate(data_frame):
        total = productivity_of_company(i, data_frame)
        if total > max_products:
            max_products = total
            best_company = i + 1

    print(f"The best company is company {best_company} with {max_products} products made.")

def min_productivity(data_frame):
    worst_company = 1
    min_products = productivity_of_company(0, data_frame)

    for i, row in enumerate(data_frame):
        total = productivity_of_company(i, data_frame)
        if total < min_products:
            min_products = total
            worst_company = i + 1

    print(f"The worst company is company {worst_company} with {min_products} products made.")

def mean_products(data_frame):
    """Calculates per-company and overall average products per employee."""
    total_sum = 0
    total_employees = 0

    for i, row in enumerate(data_frame):
        average = np.mean(row)
        print(f"On average, one employee from company {i+1} produced {average:.2f} products.")
        total_sum += np.sum(row)
        total_employees += len(row)

    total_mean = total_sum / total_employees
    print(f"Total average products per employee across all companies: {total_mean:.2f}")

# ------------------------
# File Handling
# ------------------------
def file_handling(filename="company.txt"):
    """Reads company.txt and returns a numpy array of integers."""
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            values = line.strip().split(',')
            int_values = [int(val) for val in values]
            lines.append(int_values)

    data_frame = np.array([np.array(row) for row in lines], dtype=object)
    return data_frame

# ------------------------
# Main
# ------------------------
def main():
    data_frame = file_handling()
    print("Data frame:")
    print(data_frame)

    # Example usage of IntArray class for the first company
    first_branch = IntArray(data_frame[0])
    first_branch.display()
    first_branch.salary(10)
    first_branch.show_data()

    # Productivity stats
    max_productivity(data_frame)
    min_productivity(data_frame)
    mean_products(data_frame)

if __name__ == "__main__":
    main()
