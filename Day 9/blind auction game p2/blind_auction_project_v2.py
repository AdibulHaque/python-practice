from art import logo
print(logo)  # Print logo from art module


# Function to find the highest bidder from the bidding record
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""  # Store the name of the highest bidder
    # Loop through each bidder in the dictionary
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        # Check if current bid is higher than the highest seen so far
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    # Print the winner and their bid
    print(f"The winner is {winner} with a bid of ${highest_bid}")


# Dictionary to store bids {name: price}
bids = {}
# Flag to control the loop
continue_bidding = True

while continue_bidding:
    # Ask for bidder's name and bid
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    # Store in dictionary
    bids[name] = price

    # Ask if there are more bidders
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        # Stop the loop and determine the winner
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        # Clear screen (simulated by printing multiple new lines)
        print("\n" * 20)
