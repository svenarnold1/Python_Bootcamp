# this is a blind auction
bids = {}
keep_running = True
score = 0
winner = 'no one'
while keep_running:

    name = input('Input your name:\n')
    bid = int(input('Input your bid:'))

    # add name and price in dictionary
    bids[name] = bid

    again = input('Are there other users who want to bid?\n').lower()

    if again == 'no':
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

print(f"Congratulations! {winner.upper()} has won the auction with the bid of {bids[winner]}$!")
