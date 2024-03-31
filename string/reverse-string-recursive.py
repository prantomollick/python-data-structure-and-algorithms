#recursive python program to reverse a string
def recursiveReverse(str, i = 0):
    n = len(str)
    
    if i == n //  2:
        return
    
    #swap the i and n-i-1 character
    str[i], str[n-i-1] = str[n-i-1], str[i]
    
    return recursiveReverse(str, i + 1)

if __name__ == '__main__':
    str = "Pranto Mollick"
    
    str = list(str)
    recursiveReverse(str)
    
    str = ''.join(str)
    print(str)