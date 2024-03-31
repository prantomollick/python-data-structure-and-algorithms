#python program to reverse a string using stack


def reverseByStack(str):
    
    #using as stack
    
    stack = []
    

    for i in range(len(str)):
        stack.append(str[i])
        

    for i in range(len(str)):
        str[i] = stack.pop()
        


if __name__ == '__main__':
    str = "pranto"
    
    str = list(str)
    reverseByStack(str)
    

    str= ''.join(str)
    
    print(str)