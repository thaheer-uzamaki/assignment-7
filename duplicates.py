from collections import OrderedDict 

def removeDupWithoutOrder(str): 
   
   
    return "".join(set(str)) 
  
def removeDupWithOrder(str): 
    return "".join(OrderedDict.fromkeys(str))  
  
# Driver program 
if __name__ == "__main__": 
    str = input("Enter a line of text: - ")
    print ("Without Order = ",removeDupWithoutOrder(str) )
    print ("With Order = ",removeDupWithOrder(str) )