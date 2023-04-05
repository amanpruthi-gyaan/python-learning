# Convert a dictionary to a list :
#dict = {"0":"zero" , "1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}

x =input ("Enter the desired number\n")
dict = {
    "0":"zero" ,
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine"
}
list =[]

for i in x:
    list.append(dict[i])
    
print(list)