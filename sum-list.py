#Write a Python program to sum all the items in a list.

def sum_list(items):
    sum = 0
    for x in items:
        sum = sum + x
    return sum
print(sum_list([10,20,80]))