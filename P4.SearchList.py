#Sumit Sangave
# 4.Write a function called search_list that takes a list and a search term as parameters.


# List=["Apple","Orange","Mango","Strwabery"]
# def Search_List():
#     for i in List:
        
# # print(dir(List))
# # 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

def Search_List(List,Search):
    index=0
    for i in List:
        if(i.upper() == Search.upper()):
            return index
        index=index+1
    return -1

names=input("Enter the names :  ")
List=names.split()
Search=input("Enter the name to be searched : ")
Result= Search_List(List,Search)
print(Result)