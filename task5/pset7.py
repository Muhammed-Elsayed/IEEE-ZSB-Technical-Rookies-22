def acmTeam(topic):
    maxsub = 0
    counter = 0

    n = len(topic)
    for i in range(n):
        for j in range(i, n):
            sub  = 0

            for x, y in zip(topic[i], topic[j]):
                if x == "1" or y == "1":
                    sub += 1

                if sub > maxsub:
                    maxsub = sub
                    counter = 1
                elif sub == maxsub:
                    counter += 1


    return [maxsub, counter]
