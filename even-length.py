def printWords(s): 
        
    s = s.split(' ')
    for word in s:
        if len(word)%2==0: 
            print(word)  
  
  
# Driver Code  
s = input("Enter a line of text: - ")
printWords(s)  
