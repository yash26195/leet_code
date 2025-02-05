//Best time to buy and sell a stock
// 1. buy low and sell high 
// day 1 price 4 
// day 2 price 5
// ..


// Two pointer
// Left pointer on day 1(buy) and right pointer on day 2(sell)
// if left pointer value > right pointer value the left point ++ and right pointer ++
// if left pointer value<= right pointer value then only update the right pointer ++
// maintain a max profit and keep updating it

def max_profit(prices: List[int]):
	l, r = 0, 1
	max_profit = 0
	while r < len(prices):
		if prices[l] > prices[r]:
			l = r
		else if prices[l] < prices[r]:
			max_profit = max(max_profit, prices[r]-prices[l])

		r = r+1
		


def max_profit(prices: list[int]) -> int:
    """
    Function to calculate the maximum profit that can be achieved
    by buying and selling a stock on different days.
    Two pointer
	Left pointer on day 1(buy) and right pointer on day 2(sell)
	left pointer value > right pointer value the left point ++ and right pointer ++
	if left pointer value<= right pointer value then only update the right pointer ++
	maintain a max profit and keep updating it
	    
    Parameters:
    prices (list[int]): List of stock prices for each day.
    
    Returns:
    int: Maximum profit achievable.
    """
    # Initialize two pointers: left (buy) and right (sell)
    left, right = 0, 1  # Left points to the buy day, right points to the sell day
    max_profit = 0  # Variable to store the maximum profit

    while right < len(prices):
        # If the price at 'left' is greater than at 'right', update the buy day to 'right'
        if prices[left] > prices[right]:
            left = right
        else:
            # Calculate the profit and update max_profit if it's greater
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)

        # Move the sell pointer to the next day
        right += 1

    return max_profit

# Test cases
def test_max_profit():
    """
    Function to test the max_profit function with multiple scenarios.
    """
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5, "Test case 1 failed"  # Buy at 1, sell at 6
    assert max_profit([7, 6, 4, 3, 1]) == 0, "Test case 2 failed"    # No profit possible
    assert max_profit([1, 2, 3, 4, 5]) == 4, "Test case 3 failed"    # Buy at 1, sell at 5
    assert max_profit([3, 3, 3, 3, 3]) == 0, "Test case 4 failed"    # Prices are the same
    assert max_profit([1]) == 0, "Test case 5 failed"                # Single-day prices
    assert max_profit([]) == 0, "Test case 6 failed"                 # Empty list of prices
    print("All test cases passed!")

# Run tests
test_max_profit()
