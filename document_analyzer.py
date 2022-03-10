
def document_analyzer():
    #fileName = open('document.txt', 'r')
    #Lines = fileName.readLines()
    #word = fileName.read()
    
    file = open('document.txt', 'r', encoding = 'utf-8')
    text = file.read()

   
    d =  { }
    with open('document.txt','r', encoding = 'utf-8') as file:
        for line in file:
            print(line)
            for word in line.split():
                    d[word]= d.get(word,0)+1
    list = []
    for w in sorted(d, key = d.get, reverse = True):   
        list.append(w)
        #print(w,d[w])
    for i in range (5):
        print(list[i], ": ", d[list[i]]  )
       #  print(":"  )
       # print(d[list[i]] )



      
    #d= dict(sorted(d.items(), key =lambda t: t[1]))
    #print(d)
   
document_analyzer()



 