# Arrays: Left Rotation
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

n, m = map(int, input().split())
a = list(map(int, input().split()))[:n]
print(*a[m:]+a[:m])
