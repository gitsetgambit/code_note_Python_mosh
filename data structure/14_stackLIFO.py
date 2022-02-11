# declaring a list
browsing_session = []
# adding element in the list with append method
browsing_session.append(4)
browsing_session.append(2)
browsing_session.append(6)
browsing_session.append(46)
# popping the element and storing the list in 'lifo' variable
Lifo = browsing_session.pop()
# printing the popped element
print(Lifo)
# printing the whole list after element popped
print(browsing_session)
# printing redirect and last element in the list after the popping
print("redirect", browsing_session[-1])
