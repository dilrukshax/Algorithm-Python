
#SELECTION-SORT(A) 
#1. n = A.length 
#2. for j = 1 to n #pseudo code 1 in python 0  
#3.      smallest = j
#4.      for i = j + 1 to n           
#5.          if A[i ] < A[smallest]                
#6.              smallest = i                     
#7.          exchange A[ j ] with A[smallest]            



A = []

n = int(input("enter size : "))
print("enter number")
for i in range(n):
    elimant = int(input())
    A.append(elimant)

print(A)


def selectionsort(A):
    n = len(A)
    for j in range(0,n):
        smallest = j
        for i in range (j+1,n):
            if A[i] < A [smallest]:
                smallest= i
        A[j],A[smallest] = A[smallest],A[j]

selectionsort(A)
print("sorted array")
print(A)
