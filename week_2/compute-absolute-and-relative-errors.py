# True value and approximate value
true_value = 3.14159265
approx_value = 3.14

# Calculate Absolute Error
absolute_error = abs(true_value - approx_value)

# Calculate Relative Error
relative_error = absolute_error / abs(true_value)

# Print Results
print("Absolute Error:", absolute_error)
print("Relative Error:", relative_error)
print("Relative Error (%):", relative_error * 100)
