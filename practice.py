
dial = 3
nudge = 0.001

for i in range(20):

    screen_before = dial * dial
    screen_after = (dial + nudge) * (dial + nudge)

    nudge_result = (screen_after - screen_before) / nudge

    dial = dial - 0.1 * nudge_result

    #print(dial)

    print(nudge_result)
