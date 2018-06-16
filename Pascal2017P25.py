def matching_digits(n, g):
    matched = 0
    for i in range(5):
        if (n - g) % 10 == 0:
            matched += 1

        n = n // 10
        g = g // 10

    return matched


def match_all(n):
    return matching_digits(n, 51545) == 2 and \
           matching_digits(n, 21531) == 1 and \
           matching_digits(n, 71794) == 0 and \
           matching_digits(n, 59135) == 1 and \
           matching_digits(n, 58342) == 2 and \
           matching_digits(n, 37348) == 2 and \
           matching_digits(n, 71744) == 1


def match_51545(n):
    return matching_digits(n, 51545) == 2


def match_51545_21531(n):
    return matching_digits(n, 51545) == 2 and \
           matching_digits(n, 21531) == 1


def match_51545_21531_71794(n):
    return matching_digits(n, 51545) == 2 and \
           matching_digits(n, 21531) == 1 and \
           matching_digits(n, 71794) == 0


def compute(matching_condition):
    count = 0
    s = 0
    for g in range(10000, 99999):
        if matching_condition(g):
            print(g, end=" ")
            count += 1
            s += g
    print("count", count)
    print("sum:", s)
    print()


print("matching 51545:")
compute(match_51545)

print("matching 51545 and 21531:")
compute(match_51545_21531)

print("matching 51545, 21531 and 71794:")
compute(match_51545_21531_71794)

print("matching all:")
compute(match_all)

"""
Fourth digit is 4:
    71794  0
    71744  1

5155 1
2151 1
7174 0
5915 1
5832 1
3738 1
7174 0

If first digit is 5:
155 0
151 1
174 0
915 0
832 0
738 1
174 0
          31
        7 1
"""
