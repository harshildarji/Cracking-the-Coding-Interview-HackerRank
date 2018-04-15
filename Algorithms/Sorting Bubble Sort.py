# Sorting: Bubble Sort
# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
count = 0
for i in range(n):
    for j in range(i+1, n):
        if a[i] > a[j]: a[i], a[j] = a[j], a[i]; count += 1
print('Array is sorted in %d swaps.\nFirst Element: %d\nLast Element: %d' % (count, a[0], a[n-1]))
