# Sumit Sangave
#2. Write a program that takes a list of integers called numbers and
# replaces each element greater than 10 with a '*'. Print the new version of numbers

list=[50,20,1,5,45,2]
NewList=[]
for i in list:
    if(i>10):
        NewList.append("*")
    else:
        NewList.append(i)
print(NewList)