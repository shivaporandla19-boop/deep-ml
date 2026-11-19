def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    pass
    res=[0]*len(a)
    if len(a[0])==len(b):
        for i in range(0,len(a)):
            for j in range(0,len(a[0])):
                res[i]+=(b[j]*a[i][j])
        return res
    else: 
        return -1