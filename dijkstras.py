# Write a program that finds the shortest path from a source 
# vertex (0) to all other vertices. Following is a sample 
# input and output files.
# Reference : https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/

# Sample Input:
# 8
# 15
# 4 5 0.35
# 5 4 0.35
# 4 7 0.37
# 5 7 0.28
# 7 5 0.28
# 5 1 0.32
# 0 4 0.38
# 0 2 0.26
# 7 3 0.39
# 1 3 0.29
# 2 7 0.34
# 6 2 0.40
# 3 6 0.52
# 6 0 0.58
# 6 4 0.93

# Sample Output:
#  0 to 0 (0.00)  
#  0 to 1 (1.05)  0->4  0.38   4->5  0.35   5->1  0.32
#  0 to 2 (0.26)  0->2  0.26
#  0 to 3 (0.99)  0->2  0.26   2->7  0.34   7->3  0.39
#  0 to 4 (0.38)  0->4  0.38
#  0 to 5 (0.73)  0->4  0.38   4->5  0.35
#  0 to 6 (1.51)  0->2  0.26   2->7  0.34   7->3  0.39   3->6  0.52
#  0 to 7 (0.60)  0->2  0.26   2->7  0.34

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def insert(root,key):
    if key is None:
        pass
    elif root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        if root.val < key:
            root.right = insert(root.right, key)
        elif root.val >= key:
            root.left = insert(root.left,key)
    return root
def search(root,key):
    flag = True
    if root is None:
        return False
    elif root.val == key:
        return True
    elif root.val < key:
        return search(root.right,key)
    else:
        return search(root.left,key)
def delete(root,data):
    # if root is None:
    #     print("tree is empty")
    #     return
    if data < root.val:
        if root.left:
            root.left = delete(root.left,data)
        else:
            print(f"{data} is not available")
    elif data > root.val:
        if root.right:
            root.right = delete(root.right,data)
        else:
            print(f"{data} is not available")
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        if root.right is None:
            temp = root.right
            root = None
            return temp
        node = root.right
        while node.left:
            node = node.left
        root.val = node.val
        root.right = delete(root.right,node.val)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
 
r = Node(50)
delete(r,90)
r = insert(r, 30)
# print("for 30 root is",r)
r = insert(r, 20)
# print("for 20 root is",r.val)
r = insert(r, 40)
# print("for 40 root is",r.val)
r = insert(r, 70)
# print("for 70 root is",r.val)
r = insert(r, 90)
 
delete(r,70)
delete(r,20)
delete(r,30)
delete(r,40)
delete(r,50)
print("root",r.val)
# print("for 60 root is",r.val)
# r = insert(r, 50)
# print("for 50 root is",r.val)
# r = insert(r, 50)
# print("for 50 root is",r.val)
# r = insert(r,2530)
# print("for 230 root is",r.val)
 
 
# # r=Node(7)
# # r = insert(r,24)
# # print(r.val)
# print(search(r,2530))
 
inorder(r)


# Pleae go through the module resources which you can find in the week - 3 Day - 1