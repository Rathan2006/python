import numpy as np

def format_array_elements(arr):
    formatted_arr = []
    for element in arr:
        element = str(element)
        formatted_element = element.center(15, "_")
        formatted_arr.append(formatted_element)
        formatted_element = element.ljust(15, "_")
        formatted_arr.append(formatted_element)
        formatted_element = element.rjust(15, "_")
        formatted_arr.append(formatted_element)
    return np.array(formatted_arr)

user_input = input("Enter elements of the array separated by commas: ")
data = np.array(user_input.split(","))
try:
    formatted_array = format_array_elements(data)
    print(formatted_array)
except ValueError as e:
    print(e)
