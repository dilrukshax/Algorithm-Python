#quicksort(A, p, r):
#    if p < r
#        q = partition(A, p, r)
#        quicksort(A, p, q - 1)
#        quicksort(A, q + 1, r)
#
#partition(A, p, r):
#    i = p - 1   // Initialize the index of smaller element
#    x = A[r]    // Choose the pivot element (usually the last element)
#    for j = p to r:
#        if A[j] <= x:
#            i = i + 1   // Increment index of smaller element
#            swap A[i] with A[j]  // Swap current element with element at smaller index
#    swap A[i + 1] with A[r]   // Swap pivot element with element at smaller index + 1
#    return i + 1   // Return the partition point


A = []

n = int(input("Eneter number size: "))

print("enter number:")
for i in range(0,n):
    elimant = int(input())
    A.append(elimant)


print(A)
    

def partition(A, p,r):
    i = p-1   # p fist index
    x = A[r]  # r last index (pivot)
    for j in range(p,r):
        if A[j] <= x:
            i = i + 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i +1

def quicksort(A, p, r ):
    if p < r:
        q = partition(A, p,r)
        quicksort(A, p,q-1)
        quicksort(A,q+1,r)



quicksort(A, 0,n-1)
print(A)

# Adjusted for descending order

def partition(A, p,r):
    i = p-1   # p fist index
    x = A[r]  # r last index (pivot)
    for j in range(p,r):
        if A[j] >= x: # Adjusted for descending order
            i = i + 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i +1

def quicksort(A, p, r ):
    if p < r:
        q = partition(A, p,r)
        quicksort(A, p,q-1)
        quicksort(A,q+1,r)



quicksort(A, 0,n-1)
print(A)
        
