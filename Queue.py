# Declare an empty queue
queue = []

# Enqueue three elements onto the queue
queue.append(1)
queue.append(2)
queue.append(3)

# Print the queue
print(queue)

# Dequeue an element from the queue
first_element = queue.pop(0)
print("Dequeued element:", first_element)

# Print the queue again
print(queue)

# Enqueue two more elements onto the queue
queue.append(4)
queue.append(5)

# Print the queue
print(queue)

# Dequeue all elements from the queue
while queue:
    first_element = queue.pop(0)
    print("Dequeued element:", first_element)

# Print the queue (should be empty)
print(queue)
