data = [(2, 10), (3, 15), (5, 25)]   # (toppings, real price)

def error(dial):
    total = 0
    for toppings, real_price in data:
        guess = dial * toppings
        total += (guess - real_price) ** 2
    return total

dial = 1.0
nudge = 0.001
for step in range(10):
    nudge_result = (error(dial + nudge) - error(dial)) / nudge
    dial = dial - 0.01 * nudge_result
    print(step, "dial:", round(dial, 3), "error:", round(error(dial), 3))