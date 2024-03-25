#5. Find unique elements in a matrix

#The idea is to use hasing and traverse through all the elements of the matrix, if an element is present in the dictionary, then increment it's count




#element in matrix
def findUniqueElements(mat, n, m):
    maximum = 0; flag = 0
    
    for i in range(n):
        for j in range(m):
            if maximum < mat[i][j]:
                maximum = mat[i][j]
    
    uniqueElementDict = [0] * (maximum + 1)
    
    for i in range(n):
        for j in range(m):
            uniqueElementDict[(mat[i][j])] += 1
    
    
    for key in range(maximum + 1):
        if uniqueElementDict[key] == 1:
            print(key, end = ' ')
            flag = 1
    
    if(flag == 0):
        print("No unique Element in the matrix")
            
        
        
def findUniqueElements2(mat, r, c):
    
    #declare map for hashing
    mp = {}
    for i in range(r):
        for j in range(c):
            if mat[i][j] not in mp:
                mp[(mat[i][j])] = 1
            else: 
                mp[(mat[i][j])] += 1
    
    print(mp)

    flag = False
    
    #print unique element
    for p in mp:
        print(p)
        if mp[p] == 1:
            print(p, end=" ")
            flag = True
    
    if flag == False:
        print("No unique element in the matrix")
            
    






                    
                
                
# Driver Code 
mat = [[1, 2, 3, 20],  
       [5, 6, 20, 25], 
       [1, 3, 5, 6], 
       [6, 7, 8, 15]] 

n = 4
m = 4
findUniqueElements2(mat, n, m) 