from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

card = deque()
for i in range(n):
    card.append(i+1)

i = 0
while len(card) != 1:
    card.popleft() if i % 2 == 0 else card.append(card.popleft())
    i += 1

print(card[0])