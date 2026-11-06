a = 2.0
b = a * a      # link 1
c_before = 5 * b      # link 2

nudge = 0.001

a = a + nudge

b = a * a

c_after = 5 * b

change = (c_after - c_before) / nudge

print(change)