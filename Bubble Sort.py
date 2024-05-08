#BubbleSort(A):
#1. n = length(A)
#2. for i = 1 to n - 1
#3.     for j = 1 to n - i
#4.         if A[j] < A[j - 1]
#5.             swap A[j] with A[j - 1]



arr = []

n = int(input("Enter the size: "))

print("enter number:")
for i in range(0,n):
    eliment = int(input())
    arr.append(eliment)

print(arr)


def bubblesort(A):
    n = len(A)
    for i in range(1,n):
        for j in range(1,n-i+1):
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]


bubblesort(arr)
print("sorted array")
print(arr)
