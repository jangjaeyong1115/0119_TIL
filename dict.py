members = [
    'jay','john'
]

count = {}

for member in members:

    count[member] = count.get(member,0) + 1

count_items = count.items()
print(count_items)

from collections import Counter
new_count_items = Counter(members)
print(new_count_items)