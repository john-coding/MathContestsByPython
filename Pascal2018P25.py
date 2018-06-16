count = 0

m = 500
for n in range(1, 500):
    r = m % n

    if r == 0:
        s = 0
    else:
        s = n % r

    if s == 0:
        t = 0
    else:
        t = r % s

    if 1 <= r <= 15 and 2 <=s <=9 and t == 0:
        print("r=" + str(r) + " s=" + str(s) + " t=" + str(t) + " n=" + str(n))
        # print(n, end=" ")
        count += 1

print()
print(count)
