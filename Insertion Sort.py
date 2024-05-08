#InsertionSort(A):
#1. for j = 1 to length(A) - 1
#2.     key = A[j]
#3.     i = j - 1
#4.     while i >= 0 and key < A[i]
#5.         A[i + 1] = A[i]
#6.         i = i - 1
#7.     A[i + 1] = key



list = []

n = int (input("Eneter the numbers:  "))

print("Enter numbers")
for i in range(0,n):
    element = int (input())
    list.append(element)

print(list)

def insertionSort(arr):
    for j in range(1,len(arr)):
        key = arr[j]
        i = j-1
        while i>= 0 and key <arr[i]:
            arr[i+1] = arr[i]
            i=i-1
        arr[i+1]=key

insertionSort(list)
print ("Sorted array :")
#for i in range(len(list)):
#    print("%d" %list[i])
print(list)

print(sum(list))
