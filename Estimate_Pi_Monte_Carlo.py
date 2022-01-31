def monte_carlo_pi(total_points) -> float :
    import math
    import random

    in_circ = 0
    x_loc = random.random()
    y_loc = random.random()

    for _ in range(total_points) :
        if (x_loc**2 + y_loc**2 <= 1) :
            in_circ += 1
        x_loc = random.random()
        y_loc = random.random()
    return((4 * in_circ)/total_points)

if __name__ == "__main__" :
    import random
    total_points = random.randrange(1000,100000)
    print(total_points)
    pi = monte_carlo_pi(total_points)
    print(pi)
