list1=list(input("enter a string ="))
n=len(list1)
if(n>=3):
   temp = list1[0]
   for i in range(1, n):
     list1[i - 1] = list1[i]
   list1[n-1] = temp
else :
    #reverse string
    temp=list1[0]
    list1[0]=list1[1]
    list1[1]=temp
list1=''.join(list1)
print(list1)
