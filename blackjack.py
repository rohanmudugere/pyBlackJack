def deal(deck):
    import random as r
    userCards = []
    dealerCards = []
    for i in range(0, 4):
        num = r.choice(list(deck))
        if i % 2 == 0:
            userCards.append(deck.pop(num))
        else:
            dealerCards.append(deck.pop(num))
    return userCards, dealerCards

def deal1(deck):
    import random as r
    num = r.choice(list(deck))
    card = deck.pop(num)
    return card

def calcTotal(cards):
    total = 0
    for i in range(0, len(cards)):
        card = cards[i].split()
        if card[0] == "Ace":
            total += 11
        elif card[0] == "Two":
            total += 2
        elif card[0] == "Three":
            total += 3
        elif card[0] == "Four":
            total += 4
        elif card[0] == "Five":
            total += 5
        elif card[0] == "Six":
            total += 6
        elif card[0] == "Seven":
            total += 7
        elif card[0] == "Eight":
            total += 8
        elif card[0] == "Nine":
            total += 9
        else:
            total += 10
    if total > 21:
        for i in range(0, len(cards)):
            card = cards[i].split()
            if card[0] == "Ace":
                total -= 10
            if total > 21:
                break
    return total

def uChoice(deck, userCards, uTotal):
    while uTotal <= 21:
        choice = input('  Would you like to "HIT" or "STAY"? ')
        while (choice.lower() != "hit") & (choice.lower() != "stay") :
            print('  Invalid input. Please type "HIT" or "STAY".')
            choice = input('  Would you like to "HIT" or "STAY"? ')
        if choice.lower() == "hit":
            nextUserCard = deal1(deck)
            print(f"\n  You were dealt the {nextUserCard}.")
            userCards.append(nextUserCard)
            uTotal = calcTotal(userCards)
        else:
            break
    return uTotal

def dChoice(deck, dealerCards, uTotal, dTotal):
    while dTotal < uTotal:
            nextDealerCard = deal1(deck)
            print(f"\n  The dealer was dealt the {nextDealerCard}.")
            dealerCards.append(nextDealerCard)
            dTotal = calcTotal(dealerCards)
    return dTotal

def main():
    print("\nWelcome to BlackJack!")
    #initiailze deck
    deck = {
    "1": "Ace of Spades",
    "2": "Two of Spades",
    "3": "Three of Spades",
    "4": "Four of Spades", 
    "5": "Five of Spades",
    "6": "Six of Spades",
    "7": "Seven of Spades",
    "8": "Eight of Spades",
    "9": "Nine of Spades",
    "10": "Ten of Spades",
    "11": "Jack of Spades",
    "12": "Queen of Spades",
    "13": "King of Spades",
    "14": "Ace of Hearts",
    "15": "Two of Hearts",
    "16": "Three of Hearts",
    "17": "Four of Hearts", 
    "18": "Five of Hearts",
    "19": "Six of Hearts",
    "20": "Seven of Hearts",
    "21": "Eight of Hearts",
    "22": "Nine of Hearts",
    "23": "Ten of Hearts",
    "24": "Jack of Hearts",
    "25": "Queen of Hearts",
    "26": "King of Hearts",
    "27": "Ace of Clubs",
    "28": "Two of Clubs",
    "29": "Three of Clubs",
    "30": "Four of Clubs", 
    "31": "Five of Clubs",
    "32": "Six of Clubs",
    "33": "Seven of Clubs",
    "34": "Eight of Clubs",
    "35": "Nine of Clubs",
    "36": "Ten of Clubs",
    "37": "Jack of Clubs",
    "38": "Queen of Clubs",
    "39": "King of Clubs",
    "40": "Ace of Diamonds",
    "41": "Two of Diamonds",
    "42": "Three of Diamonds",
    "43": "Four of Diamonds", 
    "44": "Five of Diamonds",
    "45": "Six of Diamonds",
    "46": "Seven of Diamonds",
    "47": "Eight of Diamonds",
    "48": "Nine of Diamonds",
    "49": "Ten of Diamonds",
    "50": "Jack of Diamonds",
    "51": "Queen of Diamonds",
    "52": "King of Diamonds",
    }
    userCards, dealerCards = deal(deck)
    print(f"\n  You have been dealt the {userCards[0]} & the {userCards[1]}.")
    uTotal = calcTotal(userCards)
    dTotal = calcTotal(dealerCards)

    uTotal = uChoice(deck, userCards, uTotal)
    
    if uTotal > 21:
        print("  You busted.")
        result = "lost"
    else: 
        print(f"\n  The dealer has {dealerCards[0]} & the {dealerCards[1]}.")
        dTotal = dChoice(deck, dealerCards, uTotal, dTotal)
    if dTotal > 21:
        print("  The dealer busted.")
        result = "won"
    elif dTotal == uTotal:
        result = "tied"
    else:
        result = "lost"
    
    print(f"\nYou {result}.\n")

if __name__ == "__main__":
    main()
       
