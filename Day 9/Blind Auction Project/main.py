from art import logo

# TODO-1: Ask the user for input
print(logo)
print("Welcome to the secret auction program.")


# TODO-2: Save data into dictionary {name: price}

# TODO-3: Whether if new bids need to be added
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bidders = {}
ask_again = True
while ask_again == True:
    name = input("What is your name? ")
    bid = int(input("What's your bid? "))
    bidders[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if other_bidders == 'no':
        ask_again = False
        find_highest_bidder(bidders)
    else:
        print("\n" * 20)

# TODO-4: Compare bids in dictionary

