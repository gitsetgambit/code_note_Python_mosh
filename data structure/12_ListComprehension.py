items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
    ("product4", 17),
    ("product5", 3),
    ("product6", 40),
]

# mapped = list(map(lambda item: item[1], items))
# map 'comprehension' here its cleaner and better
mapped = [item[1] for item in items]
print(mapped)

# filtered = list(filter(lambda item: item[1] >= 10, items))
# filter 'comprehension' here its cleaner and better
filtered = [item for item in items if item[1] >= 10]
print(filtered)
