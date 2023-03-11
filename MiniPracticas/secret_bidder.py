
print("logo")

bids = {} #creamos inicialmente hashmap
bidding_finished = False #boolen para poder cortar el loop eventualmente

def find_highest_bidder(bidding_record): #encontrar el bidder mas alto
  highest_bid = 0 #donde guardamos la mayor 
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record: #bidder = Angela, bid_amount = 123
    bid_amount = bidding_record[bidder] #itera en el hashmaps EN LOS VALUEs
    if bid_amount > highest_bid: #Si el item iterado es mayor que la mayor bid
      highest_bid = bid_amount #guarda el mayor bid
      winner = bidder #guarda el bidder (key) del momento
  print(f"The winner is {winner} with a bid of ${highest_bid}")
  #lo imprime

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price #añadiendo a nuestro hashmap
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
   "---------------"