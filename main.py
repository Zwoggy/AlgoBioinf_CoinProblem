"""
Algorithmische Bioinformatik Aufgabe 4: Erstellen Sie ein Programm, welches die minimale Anzahl an Münzen in
einem Münzsystem C für einen Restbetrag X ermittelt. Verwenden Sie dazu folgende zwei Algorithmenprinzipien:
    - greedy
    - Dynamische Programmierung


Beispielsysteme:

X = 77, C = {7,3,1}
X = 67, C = {6,5,4,3}
X = 83, C = {50,20,10,5,2,1}
X = 83, C = {50,25,10,5,1}

Author: Florian Zwicker
"""
return_sum_1 = 77
coin_system_1 = {7,3,1}
return_sum_2 = 67
coin_system_2 = {6,5,4,3}
return_sum_3 = 83
coin_system_3 = {50,20,10,5,2,1}
return_sum_4 = 83
coin_system_4 = {50,25,10,5,1}


def greedy(coin_system, return_sum):
    """
    The function `greedy` performs a greedy algorithm approach to find the minimum number
    of coins for a given amount to refund.

    :param coin_system: List of coins available in the coin system.
    :param return_sum: The total amount of money to be returned.

    The algorithm works by initializing the amount_of_coins to 0, then for each coin in the coin system
    (sorted in descending order), it keeps subtracting the current coin value from the total amount until
    it can no longer do so, while each time incrementing the `amount_of_coins`.

    :return: Returns the minimum number of coins required to make the change.
    """
    amount_of_coins = 0  # Initialize the coin counter with 0
    for coin in sorted(coin_system, reverse = True):  # Iterates over each coin in the system in descending order
        amount_of_coins += return_sum // coin  # Add to the coin counter the maximum number of times the current coin can be used
        return_sum %= coin  # Calculate the remaining amount to refund

    return amount_of_coins  # Return the minimum number of coins


def dynamic(coin_system, return_sum = None):
    """
    This function calculates the amount of coins the customer receives using the dynamic programming algorithm.
    :param coin_system: the coinsystem used for the calculation
    :param return_sum: the amount of change the customer receives
    :return: the amount of coins the customer receives calculated by the dynamic programming algorithm
    """

    coin_table = [float('inf')] * (return_sum + 1)
    # This line initializes coin_table with infinite values at all indices except the first one, as 0 coins are needed for a change of 0.

    coin_table[0] = 0
    # This line sets the first value of coin_table to 0, as no change is needed.

    for i in range(1, return_sum + 1):
        # This loop is used to fill up the coin_table from 1 to the value of change needed.

        for coin in coin_system:
            # This loop checks every coin in the coinsystem.

            if coin <= i:
                # This condition checks if the coin value is less than or equal to the current change needed.
                # It prevents accessing a negative index in the coin_table.

                coin_table[i] = min(coin_table[i], coin_table[i - coin] + 1)
                # This line updates the coin_table[i] with the minimum coin number between the existing one and the coin number from the new coin used.

    return coin_table, coin_table[-1]
    # This function returns two values:
    # First is the complete table filled with minimum coin counts for every amount from 0 to return_sum.
    # Second is the minimum number of coins needed to get the amount of change.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """
    This is the main function of the program.
    """
    try:
        y = return_sum_2
        x = coin_system_2
        print("Using the greedy algorithm the customer receives " +  str(greedy(x, y)) + " coins.")
        coin_table, coin_amount = dynamic(x, y)
        print("Using the dynamic programming approach the customer recives " + str(coin_amount) + " coins.")
        print(coin_table)
    except:
        print("Verify your inputs and try again.")

