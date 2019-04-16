import os
import random


def generate(random: random, max: int):
    os.chdir("./input_data/")
    p = 0
    while p < max:
        p = p + 1
        input = open(str(p) + ".txt", "w")
        rantime = random.uniform(0.0, 3.0)
        for i in range(1, 41):
            timespace = random.uniform(0.0, 2.0)
            rantime = rantime + timespace
            ranfloor1 = 0
            while ranfloor1 == 0:
                ranfloor1 = random.randint(-3, 20)
            ranfloor2 = 0
            while ranfloor2 == 0 or ranfloor1 == ranfloor2:
                ranfloor2 = random.randint(-3, 20)
            input.write("[" + str(round(rantime, 1)) + "]" + str(i) + "-FROM-" +
                        str(ranfloor1) + "-TO-" + str(ranfloor2) + "\n")
            if rantime >= 40:
                break
        input.close()

def main():
    n = 50
    generate(random, n)


if __name__ == '__main__':
    main()
