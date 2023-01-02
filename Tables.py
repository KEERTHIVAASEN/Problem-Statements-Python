# Declare a 2D array with some initial values
table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Print the entire table
for row in table:
    print(row)

# Access and print an element of the table by its indices
print(table[1][2])

# Modify an element of the table by its indices
table[1][2] = 10

# Print the modified table
for row in table:
    print(row)
