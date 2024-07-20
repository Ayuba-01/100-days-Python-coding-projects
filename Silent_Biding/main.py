import os
from logo import logo


def getBidWinner(dic):
    max_key = max(dic, key=dic.get)
    print(f"The highest bidder is {max_key} with the bid of ${dic[max_key]}.")
    

print(logo)
bid_dic = {}
more_bids = True
while more_bids:
    name = input("What is your name? ")
    price = input("How much are you willing to pay $")
    bid_dic[name] = price
    answer = input("Type 'yes' if there is more bids or 'no' if you are the final bidder: ")
    os.system('clear') 
    if answer == "no":
        more_bids = False
        getBidWinner(bid_dic)
       


         
    
