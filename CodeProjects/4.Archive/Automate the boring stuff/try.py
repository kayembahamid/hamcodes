# Define the range and step size
start = 1
end = 34
step = 4

# Create a formatted string without brackets
formatted_string = ','.join([f'{i}-{i + step - 1}' for i in range(start, end + 1, step)])

# Print the formatted string
print(formatted_string)


