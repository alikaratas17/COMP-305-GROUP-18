import random
import sys

MAX_NUM = 1000000

# python3 random_test_case_generator.py n m index 
testcasename = './../inputs/rng_input'
if len(sys.argv) == 4:
    testcasename += sys.argv[3]
    num_babies = int(sys.argv[1])
    num_goal_posts = int(sys.argv[2])
else:
    num_babies = random.randint(1,600)
    num_goal_posts = random.randint(1,100)
testcasename+=".txt"
with open(testcasename, 'w', newline="") as file:
    file.write(str(num_babies) + " " + str(num_goal_posts) + "\n")
    for baby in range(num_babies):
        for post in range(num_goal_posts):
            score = random.randint(1, MAX_NUM)
            file.write(str(score)+" ")
        file.write("\n")