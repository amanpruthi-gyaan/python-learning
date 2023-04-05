"""
Write a Python program to reverse the order of the items in the array. Go to the editor
Sample Output
Original array: array('i', [1, 3, 5, 3, 7, 1, 9, 3])
Reverse the order of the items:
array('i', [3, 9, 1, 7, 3, 5, 3, 1])
"""


import array as arr

a = arr.array("i", [1, 2, 3, 4, 5])
print("The array: ", a)
l = len(a)

for i in range(l // 2):
#swapping the elements
    a[i], a[l - i - 1] = a[l - i - 1], a[i]

print("The reversed array: ", a)