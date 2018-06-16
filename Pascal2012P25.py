# verify that consecutive double equal signs will check whether all of the items are equal to each other
# for a in [0, 1, 2, True, False]:
#     for b in [0, 1, 2, True, False]:
#         for c in [0, 1, 2, True, False]:
#             if a == b == c:
#                 if not (a == b and b == c and a == c):
#                     print("A counter example", end="")
#                 print(str((a, b, c)) + " " + str(a == b == c))
#
# print()

disconnected_count = 0

for a12 in range(0, 2):
    for a13 in range(0, 2):
        for a14 in range(0, 2):
            for a23 in range(0, 2):
                for a24 in range(0, 2):
                    for a34 in range(0, 2):
                        # Two situations:
                        # -- there are at most 2 pairs of people that are not friends
                        # -- there are exactly 3 pairs of friends that forms a friendship triangle.
                        if (a12 + a13 + a14 + a23 + a24 + a34 >= 6 - 2) or \
                                ((a12 + a13 + a14 + a23 + a24 + a34 == 3) and
                                 (a23 == a24 == a24 == 1 or  # missing 1
                                  a13 == a14 == a34 == 1 or  # missing 2
                                  a12 == a14 == a24 == 1 or  # missing 3
                                  a12 == a23 == a13 == 1)):  # missing 4
                            disconnected_count += 1

print(2 ** 6 - disconnected_count)
