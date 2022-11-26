# https://www.hackerrank.com/challenges/three-month-preparation-kit-zig-zag-sequence/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-three

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) - 1 # change 1: switch with middle index
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2 # change 2: start with second last index
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 # change 3: iterate backwards

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)
