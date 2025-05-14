
e_approx = 1.0
factorial = 1


for i in range(1, 10):
    factorial *= i
    e_approx += 1 / factorial


print(f"Approximation of e after 10 terms: {e_approx}")
