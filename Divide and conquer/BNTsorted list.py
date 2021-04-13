from sys import stdin

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def Balance_Tree(root, arr, start, end):
    if start > end:
        return None
    mid = start + (end - start)//2
    left = Balance_Tree(root, arr, start, mid - 1)
    root = Node(arr[mid])
    right = Balance_Tree(root, arr, mid + 1, end)
    root.left = left
    root.right = right
    return root
    
def Post_Order(root):
    if root:
        Post_Order(root.left)
        Post_Order(root.right)
        print(root.val)

#initilize array:
arr = []

while True:
    try: #While not EOF
        arr.append(int(stdin.readline()))
    except:
        break #if EOF
#root of balance tree is the middle value of sorted array
mid =  len(arr)//2
root = Node(arr[mid])
#print LRN (Post-Order)
Post_Order(Balance_Tree(root,arr,0,len(arr)-1))