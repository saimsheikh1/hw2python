def document_analyzer():
    #fileName = open('document.txt', 'r')
    #Lines = fileName.readLines()
    #word = fileName.read()
    
 #   file = open('document.txt', 'r', encoding = 'utf-8')
  #  text = file.read()
    
   
    d =  { }    # initialize varibale for dictionary
    with open('document.txt','r', encoding = 'utf-8') as file:         # how to for sure read file
        for line in file:       # for every line in file
                        #print lines
            for word in line.split():       # line.split seperates by white space the words
                 word=word.lower()          # word.lower() only counting lowercase, so we turned all uppercase to lower case
                 if word.isalnum():         
                     d[word]= d.get(word,0)+1
               
    list = []
    for w in sorted(d, key = lambda key: (-d[key],key)):   
        list.append(w)
        #print(w,d[w])
    print("\r")
    for i in range (5):
        
       print(list[i], ": ", d[list[i]]  )
       #  print(":"  )
       # print(d[list[i]] )



      
    #d= dict(sorted(d.items(), key =lambda t: t[1]))
    #print(d)
document_analyzer()

 
