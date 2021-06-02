# COMP-305-GROUP-18
TODO List:
  > Randomized Test Case Generator
  > Ideas to improve best yet solution
  > Monte Carlo method -> use each l value with some probability
  > Analyze important l values

How to run the codes?
1.withSet.py (in python_files directory)
-After compiling the code, you need to give the pathway of a test case input file (test cases can be found in inputs folder)
-Final results can be found in output1.txt
2.mc.py (in python_files directory)
-After compiling the code, you need to give the pathway of a test case input file (test cases can be found in inputs folder)
-Final results can be found in outputMC.txt
3.solution.c (in main branch)
-After compiling the code, you need to give the pathway of a test case input file (test cases can be found in inputs folder)
-Final results can be found in outputC.txt

Results of the test cases:
Test case 1:
Runtime of withSet.py
Runtime of mc.py
Runtime of solution.c
Test case 2:
Runtime of withSet.py
Runtime of mc.py
Runtime of solution.c
Test case 3:
Runtime of withSet.py
Runtime of mc.py
Runtime of solution.c
Test case 4:
Runtime of withSet.py
Runtime of mc.py
Runtime of solution.c

Summary:
Brute Force:
In order to understand the problem correctly, we used brute force method. In this method maximum possible l value was found and all l values were tried until 1 (inclusive) and the orders were found for each.
Then the minimum orders were returned. 
Using Set:
To improve this method, we decided not to try all possible l values and implemented an algorithm withSet.py. We used only the distinct scores of the players as possible l values by using set data structure. 
We tried all these l values in descending order to find the minimum placements of the players.
We saw that deciding on the l values to be tried is critical for the complexity and run time of the algorithm. 
Augmentation:
Our most efficient method (solution.c) is using augmentation added to the previous algorithm (withSet.py). 
One of the augmentations is to keep track of the total scores of each player in an array which is used later for each l value trial in order not to recalculate the total scores of each player. Only the changes in the scores are added to these total scores to update them for each l. 
Another augmentation is an array to keep the index of the last changed score for each player. This augmentation is performed in order to decrease the number of iteration while comparing the l value and players' scores.
By keeping the total scores and the index of the last changed score for each player, we do not need to update the scores that were updated with the previous l values.
Monte Carlo:
Another method we used was Monte Carlo to decrease the number of l values tried. In this method, probability was taken as 1/number of goal posts (roundCount in mc.py). 
This method works very fast but it does not give the correct output all the time. 

MC'DE NE YAPTIK


How does solution.c work?
1. Test case file path is taken.
2. File is parsed into players and scores of the players are sorted in descending order using insertion sort and players' scores are stored in numbers array.
3. With insert_number method, distinct l values are added into an array (l_values) and size of the array is returned.
4. With calculate_sums method, each player's total scores are calculated and added into sums array.
5. Calculate_orders method is created for finding the final places of each player using their total scores in the sums array. Without changing any scores initially, orders are found and stored in min_orders array.
6. k array is defined to store the index of the last changed score value of each player. At the begining k is initialized as 0 array with size n(number of players).
7. old_l variable is defined to be the last used l value from the l_values array.
8. All distinct l values were traveled with for loop.
	8.1. All players are travelled with for loop.
	8.1.1. Corresponding sum value of the player was updated according to current l value and old_l value by using the corresponding last changed score's index stored in k.
		(sums[player number] += (k[player number]* (l - old_l)))
	8.1.2. dv variable is defined as 0.
	8.1.3 While loop is created to travel the scores that are larger than or equal to l. In this loop, the difference between score and l value is added to dv.
	8.1.4 dv is subtracted from the corresponding player's sum in sums array to update the total score value according to current l.
	8.2 Orders of the player are found with calculate_orders method with respect to their updated total scores in sums array.
	8.3 Using compare_orders method, previous order and the current order of the players are compared and if current order is smaller, it is saved to min_orders array that stores the minimum places.
	8.4 old_l value is updated with the current l value. For loop continues with the next l value from step 8.1.
9. After completion of step 8, min_orders array is written into the file outputC.txt to store the final minimum places of the players.
		





