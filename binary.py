def check(string) : 
  
  
    p = set(string) 
    s = {'0', '1'} 
    if s == p or p == {'0'} or p == {'1'}: 
        print("Yes") 
    else : 
        print("No") 
  
  
          
# driver code 
if __name__ == "__main__" : 
  
    string = input("Enter a string to check if its binary: - ")
  
    check(string) 