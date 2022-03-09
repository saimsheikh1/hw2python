def sort(l):      #type list parameter
    if not isinstance(l, list): 
        #isinstance(object, classinfo)
       print("Not list")
       return []
        
    #variable initalization for while loop below   
    i=0
    j=0
    n= len(l)
    #bubble sort 
    while i < n:
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
print(*sort(a))
print(*sort(b))
print(*sort(c))