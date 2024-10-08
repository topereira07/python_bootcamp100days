import art
print(art.logo)
print("Welcome to the Secret Auction!!")
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
more_bidders = True
bidder = {}

def find_winner(dic):
    highest_bid = 0
    winner = ""

    max_bidder = max(dic)
    print(max_bidder)


    for key in dic:
        current_nr = int(dic[key])
        if current_nr > highest_bid:
            highest_bid = current_nr
            winner = key
    print(f"The winner was: {winner} with the bid: ${highest_bid}")


while more_bidders:
    name = input("What is your name?")
    bid = int(input("What's your bid?: $"))
    bidder[name] = bid
    print("\n" * 20)
    more_bids = input("Are there any more bidders? Type 'yes' or 'no'..\n").lower()
    if more_bids == "no":
        find_winner(bidder)
        more_bidders = False





