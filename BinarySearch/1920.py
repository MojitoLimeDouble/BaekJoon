import sys
input = sys.stdin.readline

# 이분탐색
def binary_search(i, A, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if i == A[mid]:
        return 1
    elif i < A[mid]:
        return binary_search(i, A, start, mid-1)
    else:
        return binary_search(i, A, mid+1, end)

N = input()
A = sorted(map(int, input().split()))
M = input()
B = list(map(int, input().split()))

for i in B:
    print(binary_search(i, A, 0, len(A)-1))
