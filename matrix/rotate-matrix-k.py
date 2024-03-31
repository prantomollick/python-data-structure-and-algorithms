"""
Certainly! Let's break down the process of rotating a matrix to the right by **K** times step by step:

1. **Consider Each Row as an Array**:
   - Treat each row of the matrix as an array.
   - We will perform an array rotation on each row.

2. **Array Rotation**:
   - To rotate an array to the right by **K** positions, follow these steps:
     1. **Copy the Last K Elements** into a temporary array.
     2. **Shift** the first **(N - K)** elements from the beginning by **K** positions to the right.
     3. **Copy** the elements from the temporary array back into the main array.


   - **Output**:
     ```
     23 34 12
     56 67 45
     89 91 78
     ```

5. **Time Complexity**: O(N*M)
6. **Auxiliary Space**: O(M)

Remember that this approach treats each row as an array, making it straightforward to rotate the entire matrix to the right by **K** positions. Feel free to adapt this logic to other programming languages as needed! 🚀



Certainly! Let's break down the process of shifting the first **(N - K)** elements from the beginning of an array by **K** positions to the right in a more linear way:

1. **Consider an Array**:
   - Imagine we have an array of elements.

2. **Array Elements**:
   - Let's say our array has **N** elements.
   - The elements are indexed from **0** to **N-1**.

3. **Shifting to the Right**:
   - We want to shift the first **(N - K)** elements to the right by **K** positions.
   - Here's how we can do it step by step:

     a. **Copy the Last K Elements**:
        - Take the last **K** elements from the array and store them in a temporary location.
        - These are the elements from indices **(N - K)** to **(N - 1)**.

     b. **Make Space for the Shifted Elements**:
        - Move the first **(N - K)** elements (from indices **0** to **(N - K - 1)**) to their new positions.
        - Each element will move **K** positions to the right.
        - The elements that were at indices **0** to **(K - 1)** will now be at indices **K** to **(2K - 1)**.

     c. **Copy Back the Temporarily Stored Elements**:
        - Finally, copy the elements from the temporary location back into the array.
        - These elements will now occupy indices **0** to **(K - 1)**.

4. **Example**:
   - Suppose we have an array: **[10, 20, 30, 40, 50, 60, 70]**
   - If we want to shift the first **4** elements to the right by **2** positions:
     - Copy the last **2** elements: **[60, 70]**
     - Shift the first **4** elements: **[10, 20, 60, 70, 50, 60, 70]**
     - Copy back the temporarily stored elements: **[60, 70, 60, 70, 50, 60, 70]**

5. **Resulting Array**:
   - The final array after the right shift: **[60, 70, 60, 70, 50, 60, 70]**

Remember that this process maintains the relative order of elements within the array while achieving the desired shift. Feel free to apply this concept to any array or matrix rotation problem! 🚀

################################################################################################################
code Explaination
################################################################################################################
Certainly! Let's break down the given Python program step by step to understand how it rotates a matrix to the right by **K** positions:

1. **Matrix Initialization**:
   - We start with a **3x3 matrix** (3 rows and 3 columns) named `mat`:
     ```
     mat = [[12, 23, 34],
            [45, 56, 67],
            [78, 89, 91]]
     ```

2. **Function Definition**:
   - The program defines a function called `rotateMatrix(k)` that takes an integer **K** as an argument.
   - The function will rotate the matrix to the right by **K** positions.

3. **Temporary Array**:
   - A temporary array named `temp` is created with a size equal to the number of columns in the matrix (which is **M = 3**).

4. **Adjust K**:
   - To handle cases where **K** is greater than the number of columns, the program calculates `k = k % M`.
   - This ensures that **K** is within a valid range (0 to **M-1**).

5. **Row-wise Rotation**:
   - The program iterates through each row of the matrix (3 rows in this case).

6. **Copying First (M - K) Elements to Temporary Array**:
   - For each row, it copies the first **(M - K)** elements (from indices **0** to **(M - K - 1)**) into the `temp` array.
   - These elements will be shifted to the right.

7. **Shifting Elements to the Right**:
   - Next, it shifts the remaining **K** elements (from indices **(M - K)** to **(M - 1)**) to the left.
   - The elements that were originally at indices **0** to **(K - 1)** will now be at indices **K** to **(2K - 1)**.

8. **Copying Back the Temporarily Stored Elements**:
   - Finally, it copies the elements from the `temp` array back into the matrix.
   - These elements will occupy indices **0** to **(K - 1)** in the rotated row.

9. **Example**:
   - If we call `rotateMatrix(2)`:
     - The first row will be rotated to **[23, 34, 12]**.
     - The second row will be rotated to **[56, 67, 45]**.
     - The third row will be rotated to **[89, 91, 78]**.

10. **Resulting Matrix**:
    - After the rotation, the updated matrix will be:
      ```
      [[23, 34, 12],
       [56, 67, 45],
       [89, 91, 78]]
      ```

This program demonstrates how to perform a right rotation on each row of a matrix. Feel free to adapt this logic to other programming languages or different matrix sizes! 🚀


"""


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