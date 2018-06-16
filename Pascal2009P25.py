obtainable = {(0, 1)}

todo = [(0, 1)]
current_index = 0
counter = 0

while counter < 100000:
    current = todo[current_index]

    new1 = (current[1], current[0])
    if new1 not in obtainable:
        obtainable.add(new1)
        todo.append(new1)

    new2 = (current[0] + 3 * current[1], current[1])
    if new2 not in obtainable:
        obtainable.add(new2)
        todo.append(new2)

    new3 = (current[0] - 2 * current[1], current[1])
    if new3 not in obtainable:
        obtainable.add(new3)
        todo.append(new3)

    current_index += 1
    counter += 1

small_limit = 21
small_obtainable = set()
for t in obtainable:
    if 0 <= t[0] < small_limit and 0 <= t[1] < small_limit:
        small_obtainable.add(t)

print(small_obtainable)
print()
print(sorted(small_obtainable))
print()

for i in range(0, small_limit):
    print(i, [b[1] for b in sorted([a for a in small_obtainable if a[0] == i])])

''' here is the output.
0 [1]
1 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
2 [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
3 [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20]
4 [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
5 [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19]
6 [1, 5, 7, 11, 13, 17, 19]
7 [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20]
8 [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
9 [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20]
10 [1, 3, 7, 9, 11, 13, 17, 19]
11 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]
12 [1, 5, 7, 11, 13, 17, 19]
13 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20]
14 [1, 3, 5, 9, 11, 13, 15, 17, 19]
15 [1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19]
16 [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
17 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20]
18 [1, 5, 7, 11, 13, 17, 19]
19 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20]
20 [1, 3, 7, 9, 11, 13, 17, 19]

The pattern is clear. Let (m,n) be a possible pair if and only if the only common divisor of m and n is 1.
So the answer is (2009, 1008) since 2009 and 1008 are both multiples of 7.
'''
