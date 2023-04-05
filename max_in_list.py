#Write a Python program to get the largest number from a list.

def max_num_in_list( l ):
    max = l[ 0 ]
    for i in l:
        if i > max:
            max = i
    return max
print(max_num_in_list([50, 20, 78, 40]))