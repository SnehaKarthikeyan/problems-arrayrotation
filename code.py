Coding:

def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr
n=int(input())
arr = list(input().split())
d=int(input())
b=rotateArray(arr, n, d)
for i in range(0,n-1):
    print(b[i],end=" ")
print(b[n-1])
