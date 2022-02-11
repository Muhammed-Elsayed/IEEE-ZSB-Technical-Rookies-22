def climbingLeaderboard(ranked, player):
    ranked = list(set(ranked))
    ranked.sort()
    i = 0
    n = len(ranked)
    list1 = []

    for score in player:
        while i < n and score >= ranked[i]:
            i += 1
        list1.append(n - i + 1)

    return list1
