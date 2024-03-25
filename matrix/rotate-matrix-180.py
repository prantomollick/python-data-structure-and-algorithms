#python program for left rotation of matrix by 180

R = 4
C = 4


#function to rotate the matrix by 180 degree
def reverseColumns(mat):
    for i in range(C):
        for j in range(int(C / 2)):
            temp = mat[j][i]
            mat[j][i] = mat[C - 1 - j][i]
            mat[C - 1 - j][i] = temp



#Function for transpose of matrix
def transpose(mat):
    for i in range(R):
        for j in range(i, C):
            temp = mat[j][i]
            mat[j][i] = mat[i][j]
            mat[i][j] = temp
            
            
    


# function to anticlockwise rotate matrix
#by 180 degree

def rotate180(mat):
    transpose(mat)
    reverseColumns(mat)
    transpose(arr)
    reverseColumns(arr)



# function for display the matrix
def printMatrix(mat):
    for i in range(R):
        for j in range(C):
            print(mat[i][j], end="\t")
        print()

            
arr = [[1, 2, 3, 4 ],  
    [ 5, 6, 7, 8 ],  
    [ 9, 10, 11, 12 ],  
    [ 13, 14, 15, 16 ]] 

rotate180(arr)
printMatrix(arr)