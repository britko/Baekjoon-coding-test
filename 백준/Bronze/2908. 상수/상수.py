a, b = input().split()
rev_a_arr = []
rev_b_arr = []

for i in range(2, -1, -1):
    rev_a_arr.append(a[i])
    rev_b_arr.append(b[i])

rev_a = int(''.join(rev_a_arr))
rev_b = int(''.join(rev_b_arr))

print(max(rev_a, rev_b))