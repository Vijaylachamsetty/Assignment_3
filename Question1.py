#Write a Python function to sum all the numbers in a list.
def createlist():
    lenof=int(input("enter the size of list:"))
    l=()
    sum=0
    for i in range(lenof):
        value=int(input("enter the values in the list:"))
        l=l+(value,)
        sum=sum+value
    print(l)
    print("sum of elements in the list:",sum)
createlist()

#saSample List : (8, 2, 3, 0, 7)
#Expected Output : 20
            