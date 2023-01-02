# Declare an empty stack
stack = []

# Push three elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

# Print the stack
print(stack)

# Pop an element from the stack
top_element = stack.pop()
print("Popped element:", top_element)

# Print the stack again
print(stack)

# Push two more elements onto the stack
stack.append(4)
stack.append(5)

# Print the stack
print(stack)

# Pop all elements from the stack
while stack:
    top_element = stack.pop()
    print("Popped element:", top_element)

# Print the stack (should be empty)
print(stack)
