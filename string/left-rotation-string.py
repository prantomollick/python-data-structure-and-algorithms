
def leftRotationString(str, r_times):
    
    temp = []
    
    for i in range(r_times, len(str)):
        temp.append(str[i])
        
    for i in range(r_times):
        temp.append(str[i])
        
    return temp




if __name__=="__main__":
    str = "GeeksforGeeks"
    str = list(str)

    
    
    str = ''.join(leftRotationString(str, 2))
    print(str)
    



def leftRotate(str1, n):
    #extended string
    temp = str1 + str1
    l = len(str1)
    
    return temp[n : l + n]

      
def rightRotate(str1, n):
    return leftRotate(str1, len(str1) - n)


if __name__=="__main__":
    str = "GeeksforGeeks"
    
    print(leftRotate(str, 2))
    print(rightRotate(str, 2))
    
