# GreedyMehod-TheFractionalKnapsackProblem
You are the leader of an elite task force that is commissioned to guard the 
borders of your country. You are allowed to build a team of your choice and each 
member can be equipped with one unique weapon. Each weapon fires a different 
type of ammunition and has a different capability of damage. The ammunition for 
these weapons come in packs of 100 units and have specific weights. 
Collectively, the team can carry a total weight of x kgs. As the leader of the task 
force it is your responsibility to decide the ratios of ammunition (full packs or 
partial packs) the team caries in order to maximize damage capability.

# File format
## Input format
```
Weapons : 6
MaxWeight : 118
A1 / 10 / 20
A2 / 30 / 40
A3 / 18 / 38
A4 / 80 / 60
A5 / 10 / 15
A6 / 20 / 22
```
## Output format
```
Total Damage: 157.5
Ammunation Packs Selection Ratio
A1 > 1
A2 > 1
A3 > 1
A4 > 0.375
A5 > 1
A6 > 1
```

# Design steps
We can use greedy method applying the solution of “The Fractional Knapsack Problem”
* Step1: First Calculate the ratio of profit per weight for each of the weapon.
* Step2: Arrange (Sort) the Weapons in the decreasing order of profit per weight ratio.
* Step3: Loop through each weapon in this sorted array.
* Step4: Assign the MaxWeight allowed to the variable rc (remaining capacity)
* Step5: Refer below flow diagram

```
Sorting ()
for i <- 1  to n
	if (w[i] <= rc)
		faction[i] <- 1
		totalDamage <- totalDamage + d[i]
		rc <- rc – w[i]
	else
		faction[i] <- rc/w[i]
totaldamage <- totaldamage + d[i] * faction[i]
rc <- 0
end for
```

# Time complexity
```
Time complexity for sorting is O(NlogN)
Time complexity for the ‘for’ loop is O(n) as it has to loop through all the weapons in the list.
So, Time complexity is O(NlogN)
```
