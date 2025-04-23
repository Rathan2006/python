import numpy as np

def format_array_elements(arr, alignment):
    formatted_arr = []
    for element in arr:
        element = str(element)
        if alignment == "center":
            formatted_element = element.center(15, "_")
        elif alignment == "left":
            formatted_element = element.ljust(15, "_")
        elif alignment == "right":
            formatted_element = element.rjust(15, "_")
        else:
            raise ValueError("Invalid alignment type.")
        formatted_arr.append(formatted_element)
    return np.array(formatted_arr)

user_input = input("Enter elements of the array separated by commas: ")
data = np.array(user_input.split(","))
alignment_type = input("Enter alignment type (center, left, right): ").strip().lower()
try:
    formatted_array = format_array_elements(data, alignment_type)
    print(formatted_array)
except ValueError as e:
    print(e)
