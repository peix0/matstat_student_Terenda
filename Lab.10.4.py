import numpy as np
import sys

sys.set_int_max_str_digits(20000)

array1 = np.array([10, 20, 5, 2])
array2 = np.array([2, 5, 10, -3])

print(f"Array 1: {array1}")
print(f"Array 2: {array2}\n")

print("--- Arithmetic Operations (Element-wise) ---")
print(f"Arrays Sum:      {array1 + array2}")
print(f"Arrays Difference:   {array1 - array2}")
print(f"Arrays Multiplication:  {array1 * array2}")
print(f"Arrays Division:   {array1 / array2}")
print("-" * 40 + "\n")

print("--- Concatenation and Aggregation ---")
combined_array = np.concatenate((array1, array2), axis=0)
print(f"Combined Array: {combined_array}\n")

max_element = np.max(combined_array)
min_element = np.min(combined_array)
sum_elements = np.sum(combined_array)
product_elements = np.prod(combined_array)

print(f"Maximum Element:  {max_element}")
print(f"Minimum Element:   {min_element}")
print(f"Sum of all Elements:   {sum_elements}")
print(f"Product of all Elements: {product_elements}")

# Код успішно виконує всі поставлені завдання за допомогою бібліотеки **NumPy**
#  включаючи поелементні арифметичні операції, об'єднання масивів
# та знаходження ключових статистичних показників (мінімум, максимум, сума, добуток)
