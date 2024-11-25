# Sumit Sangave
#3. Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. 

n=int(input("Enter the number : "))
temp=n
sum=0
for i in range(0,4):
    sum=sum+n
    n=(n*10)+temp
print(sum)