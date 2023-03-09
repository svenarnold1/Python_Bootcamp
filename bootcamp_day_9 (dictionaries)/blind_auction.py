from auction_logo import logo
# this is a blind auction
bids = {}
keep_running = True
score = 0
winner = 'no one'

print(logo)
while keep_running:

    name = input('Input your name:\n')
    bid = float(input('Input your bid: $'))

    # add name and price in dictionary
    bids[name] = bid

    should_continue = input('Are there other users who want to bid?\n').lower()

    if should_continue == 'no':
        keep_running = False
    else:
        print('\n'*500)  # clear the console

# finding the winner.
for name in bids:
    if bids[name] > score:
        score = bids[name]
        winner = name
    else:
        continue

print(f"Congratulations! {winner.upper()} has won the auction with the bid of ${bids[winner]}!")
