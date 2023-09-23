#Write a Python function that accepts a string and calculate the number of
#upper case letters and lower case letters.
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
def lowerupper():
    char=input("enter a new charcter:")
    upper,lower=0,0
    for i in char:
        if i.isupper():
            upper=upper+1
        else:
            lower=lower+1
    print("No. of Upper case characters :",upper)
    print("No. of lower case characters :",lower)
lowerupper()
        
        

