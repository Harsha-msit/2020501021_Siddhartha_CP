# removeRowAndCol (non-destructive and destructive)
# Here we will write removeRowAndCol(row, col), 
# Do not use copy.deepcopy and directly construct 
# the modified 2d list.

# The function takes a rectangular list L and two ints, 
# row and col. the goal is to obtain a version of the list 
# that has the given row and given column removed. 
# You may assume that row and col are both legal values 
# (that is, they are non-negative integers that are smaller 
# than the largest row and column, respectively). For example, 
# the list shown to the left would lead to the result shown on 
# the right when called with row 1 and column 2.

# list
# [ [ 2, 3, 4, 5],
#   [ 8, 7, 6, 5],
#   [ 0, 1, 2, 3] ]

# result
# [ [ 2, 3, 5],
#   [ 0, 1, 3] ]

def removeRowAndCol(L, row, col):
    # Your code goes here...
    l=[]
    out=[]
    for i in range(len(L)):
        if(i!=row):
            l.append(L[i])
    for i in range(len(l)):
        la=[]
        for j in range(len(l[0])):
            if(j!=col):
                la.append(l[i][j])
        out.append(la)
    return out

# Write your own test cases.
L=[[2, 3, 4, 5],[8, 7, 6, 5],[0, 1, 2, 3]]
K=[[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16],[17, 18, 19, 20]]
# print(removeRowAndCol(K,3,3))

assert(removeRowAndCol(L,1,2) == [[2,3,5],[0,1,3]])
assert(removeRowAndCol(K,3,3) == [[1, 2, 3],[5, 6, 7],[9, 10, 11],[17, 18, 19]])
print("pass")