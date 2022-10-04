from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline
n = int(input())
n_card = sorted(list(map(int, input().split())))

m = int(input())
m_card = list(map(int, input().split()))

for i in m_card:
    left_index = bisect_left(n_card, i)
    right_index = bisect_right(n_card, i)
    print(right_index - left_index, end=' ')