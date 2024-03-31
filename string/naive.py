def search(pat, text):
    M = len(pat)
    N = len(text)
    

    #A loop to slide pat[] one by one
    for i in range(N - M + 1):
        j = 0
        
        # For current index i check for pattern match
        while(j < M):
            if(text[i + j] != pat[j]):
                break
            j += 1
            
        if (j == M):
            print("Pattern found at index", i)
            


#Driver's Code
if __name__ == '__main__'            :
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    
    #function call
    search(pat, txt)