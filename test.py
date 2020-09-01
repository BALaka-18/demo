s = 'aabbcadaabb'
N = len(s)
mid = N // 2
start1, start2 = 0, 0
end1, end2 = N - 1, N - 1
length = 0

if N % 2 == 0:
    start2 = mid
    while start1 < mid and start2 < N:
        if s[start1] == s[start2]:
            length = length + 1
            start1 = start1 + 1
            start2 = start2 + 1
        else:
            start2 = start2 + 1
            continue
else:
    start2 = mid + 1
    while start1 < mid - 1 and start2 < N:
        if s[start1] == s[start2]:
            length = length + 1
            start1 = start1 + 1
            start2 = start2 + 1
        else:
            start2 = start2 + 1
            continue

print(length)
