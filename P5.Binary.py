#Sumit Sangave
# 5.Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and 
# then check whether they are divisible by 5 or not. The numbers that are divisible by 5 
# are to be printed in a comma separated sequence.

n = input("Enter the Binary nubersnumbers separated by commas: ").split(",")
for i in n:
    if int(i) % 5 == 0:  
        print(i)
