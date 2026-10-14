# Tuple of temperatures for Saturday and Sunday (3 times each)
# Saturday (Morning, Afternoon, Evening), Sunday (Morning, Afternoon, Evening)
temperatures = (22, 31, 26, 21, 33, 27)

# Display each temperature using a for loop
print("Temperatures recorded:")
for temp in temperatures:
    print(temp)

# Find highest and lowest
highest_temp = max(temperatures)
lowest_temp = min(temperatures)

print("Highest Temperature:", highest_temp)
print("Lowest Temperature:", lowest_temp)