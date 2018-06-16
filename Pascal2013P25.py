geb = [1, 3, 7, 12]
diff = [2, 4, 5]

for g in range(4, 20001):
    for d in range(diff[g - 2] + 1, 2000000):
        if d not in geb and d not in diff:
            diff.append(d)
            geb.append(geb[-1] + d)
            break
    if len(geb) > 99:
        break

# print(geb)
print([t - s for s, t in zip(geb, geb[1:])])
print(geb[99])

print()

# Is there a general formula for geb? an asymptotic formula?
alpha = ((5 ** 0.5) - 1) / 2
# print([(n+1)*(n+2)//2 + n//2  - geb[n] for n in range(0,100)])
# print([n + int(n**0.5) + int((n*2)**0.25) + 4  - diff[n] for n in range(0,1000)])
# print([int((n + int((2 * n) ** 0.5 / 2) + 2 - diff[n]) * 100 / ((n-1) ** 0.5)) + 60 for n in range(10, 20000, 200)])
# print([n + int(n ** 0.5) + 10 - diff[n] for n in range(0, 10000, 100)])
