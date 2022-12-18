from replit import clear
# HINT: You can call clear() to clear the output in the console.

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid} ")

    # quando se usa o for loop no dicionário ele itera pela chave e não pelo conteúdo,
    # por isso criou uma nova variável bid_amount. O código vai guardando os códigos
    # e comparando-os, guardando o mais alto


while not bidding_finished:
    name = input("What's your name?")
    price = int(input("what's your bid? $"))
    bids[name] = price
    should_continue = input("Are there any others bidders? Type 'yes or no'.")
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
        # name é a chave e price é o item