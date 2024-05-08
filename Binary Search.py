#binary_search(A, min_index, max_index, key):
#1. if max_index < min_index:
#2.     return False    // Key not found
#3. else:
#4.     mid = (min_index + max_index) // 2   // Calculate the middle index
#5.     if A[mid] > key:
#6.         return binary_search(A, min_index, mid - 1, key)    // Search in the left half
#7.     else if A[mid] < key:
#8.         return binary_search(A, mid + 1, max_index, key)    // Search in the right half
#9.     else:
#10.        return mid    // Key found at index mid




A = []

n = int(input("enter size : "))
print("enter number")
for i in range(n):
    elimant = int(input())
    A.append(elimant)

print(A)

def binarysearch(A, min,max,key):
    if max < min:
        return False
    else:
        mid = (min+max)//2 #get extarct value
        if A[mid] > key:
            return binarysearch(A,min,mid-1,key)
        elif A[mid] < key:
            return binarysearch(A,mid+1,max,key)
        else:
            return mid

answer = binarysearch(A, 0,len(A)-1,20)
print ("the key found at index ", answer + 1)
