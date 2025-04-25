#check whether the word is number /char/lower/upper/special char
char=input("enter any value :")
if len(char)!=1:
    print(" 'warn' enter single digit")
else:
    if char.isdigit():
        print("it is  digit/number")
    elif char.lower():
         print("character is in lower case")  
    elif char.upper():
        print("character is in upper case")
    else:
        print("character is special case")
    
    
              