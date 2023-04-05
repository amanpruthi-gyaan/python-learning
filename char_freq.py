#Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
#Sample String : 'rajasthan'
#Expected Result : {'r': 1, 'a': 3, 'j': 1, 's': 1, 't': 1, 'h': 1, 'n': 1}



def char_frequency(str):
    dict = {}
    for i in str:
        keys = dict.keys()
        if i in keys:
            dict[i] = dict[i]+1
        else:
            dict[i] = 1
    return dict
print(char_frequency('rajasthan'))