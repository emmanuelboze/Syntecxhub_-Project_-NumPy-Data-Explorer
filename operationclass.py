import numpy as np
import matplotlib.pyplot as plt
class IntArray:
    def __init__(self, int_array):
        if not isinstance(int_array, np.ndarray) or int_array.dtype != int:
            raise ValueError("Input must be a NUMPY array of integers")
        self.int_array = int_array

    def display(self):
        print(self.int_array)

    def salary(self, money_per_product):
        """
        Calculate salary based on number of products and money per product.
        money_per_product: int or float
        """
        array_shape = self.int_array.shape
        money_array = np.full(array_shape, money_per_product)
        salaries = self.int_array * money_array
        print(f"People made {self.int_array} products and their salaries are {salaries}")
    def show_data(self):
        x=np.arange(len(self.int_array))
        plt.plot(x, self.int_array, marker='o')  # Circle marker
        plt.title("productivity of the employees")
        plt.xlabel("rank of employee")
        plt.ylabel("products/month")
        plt.xticks(x)
        plt.grid()
        plt.show()