def reverseStr(str):
    n = len(str)
    
    i, j = 0, n - 1
    

    #swap character starting from 
    #two corners
    #i is the left pointer and j is the right pointer
    
    while i < j:
        str[i], str[j] = str[j], str[i]
        
        i += 1
        j -= 1



if __name__ == "__main__":
    str = "Pranto Mollick"
 
    # converting string to list
    # because strings do not support
    # item assignment
    str = list(str)
    reverseStr(str)
 
    # converting list to string
    str = ''.join(str)
 
    print(str)