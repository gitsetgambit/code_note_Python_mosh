"""
'deque' is double ended queue where we can do operation 
from both front and back end 
here we are importing that 'deque' from 'collection' module
"""
from collections import deque
# declaring the deque in variable'queue'
queue = deque([])

# adding elements with 'append' method
queue.append(16)
queue.append(24)
queue.append(3)
queue.append(443)

# using 'popleft' will remove pop the element from left
queue.popleft()
queue.popleft()

# using 'pop' will remove pop the element from right
queue.pop()
queue.pop()

# printing the queue
print(queue)

# using not operator to find queue is empty or not
if not queue:
    # if empty print "empty"
    print("empty")
