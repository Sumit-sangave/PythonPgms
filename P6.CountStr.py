#Sumit Sangvae.
# 6. Write a program that accepts a sentence and calculate the number of letters and digits.

Statement="Hi I am Sam 2631"
letters=0
digits=0
for i in Statement:
    if(i.isalpha()):
        letters+=1
    elif(i.isnumeric()):
        digits+=1

print("Count of letters : ",letters)
print("Count if digits : ",digits)