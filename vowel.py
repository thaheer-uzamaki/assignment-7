def vowel_count(str): 
      

    count = 0
    vowel = set("aeiouAEIOU") 
    for alphabet in str: 
        if alphabet in vowel: 
            count = count + 1
      
    print("No. of vowels :", count) 
      
# Driver code  
str = input("Enter a line of text: - ")
  
# Function Call 
vowel_count(str) 