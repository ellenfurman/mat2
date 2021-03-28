
def revword(word):
    w=""
    length=len(word)-1
    i=length
    while i >= 0 :
        w= w + word[i].lower()
        i=i-1
    return w
    
def countword():
    counter=1
    myfile = open("c:/users/ellen/programspy/matala2/text.txt", "r")
    #read first line without /n
    word = myfile.readline()
    word = word[0:len(word)-1]
    
    Lines = myfile.readlines()
    for line in Lines:
        for w in line.split():
            w = revword(w)
            if(w == word):
                counter = counter+1
    
    myfile.close()    
    return counter
        

    

