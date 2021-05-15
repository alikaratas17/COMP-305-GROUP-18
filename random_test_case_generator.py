import random

num_babies = random.randint(1,600)
num_goal_posts = random.randint(1,100)

with open('random_test_case.txt', 'w', newline="") as file:
    file.write(str(num_babies) + " " + str(num_goal_posts) + "\n")
    for baby in range(num_babies):
        for post in range(num_goal_posts):
            score = random.randint(1, 1000000)
            file.write(str(score)+" ")
        file.write("\n")