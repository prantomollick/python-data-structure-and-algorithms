#size of matrix
M = 3
N = 3

mat = [[12, 23, 34],
          [45, 56, 67], 
          [78, 89, 91]]
 

def rotateMatrix(k):
    global M, N, mat
    
    #temporary array of size M
    temp = [0] * M
       
    #with the size of matrix
    k = k % M

    
    for i in range(N):
        
        #copy first m-k elements to temporary array
        for t in range(0, M - k):
            temp[t] = mat[i][t]
        
        #copy the elements from k to end to starting
        for j in range(M-k, M):
            mat[i][j-M+k] = mat[i][j]
            
        #copy ements from temporary array to end
        for j in range(k, M):
            mat[i][j] = temp[j-k]
            


def displayMatrix():
    global M, N, mat
    for i in range(0, N):
        for j in range(0, M):
            print("{} ".format(mat[i][j]), end = "")
        
        print()
        


# Driver code
k = 2
 
# rotate matrix by k
rotateMatrix(k)
 
# display rotated matrix
displayMatrix()