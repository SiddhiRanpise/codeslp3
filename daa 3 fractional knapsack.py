class ItemValue:
    """Item Value DataClass"""

    def __init__(self, wt_, val_, ind_):
        # Initialize an ItemValue object with weight, value, and index
        self.wt = wt_
        self.val = val_
        self.ind = ind_
        # Calculate cost as value divided by weight
        self.cost = val_ / wt_

    def __lt__(self, other):
        # Comparator function to compare costs of two items
        return self.cost < other.cost


def fractionalKnapSack():
    # Take input from the user for items' weights and values
    wt = list(map(int, input("Enter the weights of the items: ").split()))
    val = list(map(int, input("Enter the values of the items: ").split()))

    # Take input from the user for the capacity of the knapsack
    capacity = int(input("Enter the capacity of the knapsack: "))

    # Create a list of ItemValue objects
    iVal = [ItemValue(wt[i], val[i], i) for i in range(len(wt))]
    # Sort the list of ItemValue objects based on cost in descending order
    iVal.sort(key=lambda x: x.cost, reverse=True)

    totalValue = 0
    # Loop through each item to find the maximum value in the knapsack
    for i in iVal:
        curWt = i.wt
        curVal = i.val
        if capacity - curWt >= 0:
            # If the item fits entirely in the knapsack, add its value to the total value
            capacity -= curWt
            totalValue += curVal
        else:
            # If the item doesn't fit, add the fraction that can fit to the total value
            fraction = capacity / curWt
            totalValue += curVal * fraction
            capacity = int(capacity - (curWt * fraction))
            break  # Break the loop as the knapsack is full

    return totalValue


if __name__ == "__main__":
    # Execute the fractional knapsack algorithm and display the maximum value in the knapsack
    maxValue = fractionalKnapSack()
    print("Maximum value in Knapsack =", maxValue)

"""

Working: 
example:
Enter the weights of the items: 1 3 5 4 1 3 2
Enter the values of the items: 5 10 15 7 8 9 4
Enter the capacity of the knapsack: 15

Item   | Value | Weight | Ratio
-------------------------------
  1    |   5   |   1    |   5
  5    |   8   |   1    |   8
  3    |  15   |   5    |   3
  6    |   9   |   3    |   3
  4    |   7   |   4    | 1.75
  7    |   4   |   2    |   2
  2    |  10   |   3    | 3.33
"""