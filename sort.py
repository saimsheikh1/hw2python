def sort_list(l):      #type list parameter
    if not isinstance(l, list): 
        #isinstance(object, classinfo)
       print("Not list")
       return []
        
    #variable initalization for while loop below   
    i=0
    
    n= len(l)
    #bubble sort 
    while i < n:
      j=0
      while j < (n-i-1):
            if l[j]>l[j+1]:     # if left greater than right 
                l[j], l[j+1] = l[j+1], l[j] #switch
            j+=1
      i+=1
        
    return l

#testing
a=[1,3,2,7]
b=[3,2,4,89]
c= 10
d=["A" ,"E" ,"G","B","H"]
e=[15, 377, 386, 612, 474, 267, 129, 17, 252, 999] 


print(*sort_list(a))
print(*sort_list(b))
print(*sort_list(c))
print(*sort_list(d))
print(*sort_list(e))

