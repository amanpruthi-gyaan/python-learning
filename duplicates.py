# Write a Python program to remove duplicates from a list.

list = [5,28,92,69,13,87,60,32,90,82,7]

duplicate_items = set()
uniq_items = []
for i in list:
    if i not in duplicate_items:
        uniq_items.append(i)
        duplicate_items.add(i)

print(duplicate_items)