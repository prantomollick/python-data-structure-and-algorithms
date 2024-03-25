arr = [ [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ], [ 9, 10, 11, 12] ] 

for i in range(0, 3):
    for j in range(0, 4):
        print(arr[i][j], end=' ')
    print("")
    


#search in a matrix

def searchInMatrix(arr, x):
    for i in range(0, 4):
        for j in range(0, 5):
            if(arr[i][j] == x):
                return 1
    return


x = 8
arr = [[0, 6, 8, 9, 11], 
       [20, 22, 28, 29, 31], 
       [36, 38, 50, 61, 63], 
       [64, 66, 100, 122, 128]] 



if(searchInMatrix(arr, x)):
    print("Yes")
else:
    print("No")