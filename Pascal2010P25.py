count = 0
for a12 in [0, 1]:
    for a13 in [0, 1]:
        for a14 in [0, 1]:
            for a15 in [0, 1]:
                for a16 in [0, 1]:
                    for a23 in [0, 1]:
                        for a24 in [0, 1]:
                            for a25 in [0, 1]:
                                for a26 in [0, 1]:
                                    for a34 in [0, 1]:
                                        for a35 in [0, 1]:
                                            for a36 in [0, 1]:
                                                for a45 in [0, 1]:
                                                    for a46 in [0, 1]:
                                                        for a56 in [0, 1]:
                                                            if a12 + a13 + a14 + a15 + a16 == 3 and \
                                                                    a12 + a23 + a24 + a25 + a26 == 3 and \
                                                                    a13 + a23 + a34 + a35 + a36 == 3 and \
                                                                    a14 + a24 + a34 + a45 + a46 == 3 and \
                                                                    a15 + a25 + a35 + a45 + a56 == 3 and \
                                                                    a16 + a26 + a36 + a46 + a56 == 3:
                                                                count += 1
                                                                print(a12, a13, a14, a15, a16, a23, a24, a25, a26, a34,
                                                                      a35, a36, a45, a46, a56)

print("total schedules:", count)

# Here is the deduction by logic. Let us denote the 6 different teams by t1, t2, t3, t4, t5, and t6.
#
# Let us choose 3 teams to play against team t1, which we have 10 ways to do. They are t2t3t4, t2t3t5,
# t2t3t6, t2t4t45, t2t4t6, t2t5t6, t3t4t5, t3t4t6, t3t5t6, t4t5t6.  Without loss of generality, let we
# choose team t2, t3 and t4. So t1 will not play against t5 or t6.
#
# There are two cases to extend our arrangement.
#
# Case one: team t5 does not play against team t6.  Each of team t5 and team t6 must play against all of
# team t2, t3 and t4. That is, each of the team t1, t5 and t6 plays against each of the team t2, t3 and
# t4, with no other matches possible. This is one satisfying schedule.

# Case two: team t5 plays against team t6. The other 2 opponents of team t5 must be chosen from team t2,
# t3 and t4. We have 3 way to select those 2 opponents. Without loss of generality, let us say we select
# team t2 and t3.
#
# Besides team t5, the other 2 opponents of team t6 must be chosen from team t2, t3 and t4. If we choose
# team t2 and t3 just as what have chosen for team t5, then each of team t2, t3, t5 and t6 has three
# opponents, that is, each of them will not play with team t4, which means teams t4 can only against team
# t1 at most, a violation of the requirement. So the other two opponents of team t6 cannot be team t2 and
# t3. There are 2 ways to choose these 2 opponents. We can choose them to be either team t2 and t4 or
# team t3 and t4. Without loss of generality, let us choose team t2 and team t4 to play against team t6.
#
# Note that we have chosen all three opponents for team t1, t2, t5 and t6. We have also arranged team t3
# to plays against team t1 and t5 and we have arranged team t4 to play against team t1 and t6. So team t3
# and team t4 have to play against each other. Now all teams have their three opponents specified.

# So there are 10 * ( 1 + 3 * 2) = 70 ways to schedule the tournament.
