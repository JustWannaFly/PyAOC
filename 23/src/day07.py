from aocd import get_data
from io import StringIO

input = StringIO(get_data(year=2023, day=7))
testInput = [
'32T3K 765',
'T55J5 684',
'KK677 28',
'KTJJT 220',
'QQQJA 483'
]

def parseInput(input):
    bids = []
    for entry in input:
        entry = entry.replace('\n', '')
        parts = entry.split(' ')
        bids.append((parts[0], int(parts[1])))
    return bids

def isLessPowerfulCard(card, checkCard, wilds):
    cards = []
    if wilds:
        cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    else:    
        cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    return cards.index(card) < cards.index(checkCard)

def isLessPowerfulHand(hand, checkhand, wilds):
    for i in range(5):
        if isLessPowerfulCard(hand[i], checkhand[i], wilds):
            return True
        elif not hand[i] == checkhand[i]:
            return False
    return False

def addToOrderedList(bid, list, wilds=False):
    if len(list) == 0:
        list.append(bid)
        return
    hand = bid[0]
    for i in range(len(list)):
        checkHand = list[i][0]
        if isLessPowerfulHand(hand, checkHand, wilds):
            list.insert(i, bid)
            return
    list.append(bid)

def part1(data):
    allBids = parseInput(data)
    fiveOfKinds = []
    fourOfKinds = []
    fullHouses = []
    threeOfKinds = []
    twoPairs = []
    pairs = []
    highCards = []
    
    for bid in allBids:
        if isFiveOfAKind(bid):
            addToOrderedList(bid, fiveOfKinds)
        elif isFourOfAKind(bid):
            addToOrderedList(bid, fourOfKinds)
        elif isFullHouse(bid):
            addToOrderedList(bid, fullHouses)
        elif isThreeOfAKind(bid):
            addToOrderedList(bid, threeOfKinds)
        elif isTwoPair(bid):
            addToOrderedList(bid, twoPairs)
        elif isPair(bid):
            addToOrderedList(bid, pairs)
        else:
            addToOrderedList(bid, highCards)
    
    handsByRank = []
    handsByRank.append(highCards)
    handsByRank.append(pairs)
    handsByRank.append(twoPairs)
    handsByRank.append(threeOfKinds)
    handsByRank.append(fullHouses)
    handsByRank.append(fourOfKinds)
    handsByRank.append(fiveOfKinds)
    
    rank = 1
    winnings = 0
    for handList in handsByRank:
        for hand in handList:
            winnings = winnings + (rank * hand[1])
            rank = rank + 1

    print('Total winnings = ' + str(winnings))

def isFiveOfAKind(bid, wilds=False):
    firstCard = None
    wildCard = 'J'
    for card in bid[0]:
        if firstCard == None:
            firstCard = card
        else:
            if not firstCard == card:
                return False
    return True

def isFourOfAKind(bid):
    firstCard = None
    firstCount = 0
    secondCard = None
    secondCount = 0
    for card in bid[0]:
        if firstCard == None or firstCard == card:
            firstCard = card
            firstCount = firstCount + 1
        elif secondCard == None or secondCard == card:
            secondCard = card
            secondCount = secondCount + 1
        else:
            return False
    if firstCount == 4 or secondCount == 4:
        return True
    return False

def isFullHouse(bid):
    firstCard = None
    firstCount = 0
    secondCard = None
    secondCount = 0
    for card in bid[0]:
        if firstCard == None or firstCard == card:
            firstCard = card
            firstCount = firstCount + 1
        elif secondCard == None or secondCard == card:
            secondCard = card
            secondCount = secondCount + 1
        else:
            return False
    if (firstCount == 2 and secondCount == 3) or (firstCount == 3 and secondCount == 2):
        return True
    return False

def isThreeOfAKind(bid):
    firstCard = None
    firstCount = 0
    secondCard = None
    secondCount = 0
    thirdCard = None
    thirdCount = 0
    for card in bid[0]:
        if firstCard == None or firstCard == card:
            firstCard = card
            firstCount = firstCount + 1
        elif secondCard == None or secondCard == card:
            secondCard = card
            secondCount = secondCount + 1
        elif thirdCard == None or thirdCard == card:
            thirdCard = card
            thirdCount = thirdCount + 1
        else:
            return False
    if firstCount == 3 or secondCount == 3 or thirdCount == 3:
        return True
    return False

def isTwoPair(bid):
    firstCard = None
    firstCount = 0
    secondCard = None
    secondCount = 0
    thirdCard = None
    thirdCount = 0
    for card in bid[0]:
        if firstCard == None or firstCard == card:
            firstCard = card
            firstCount = firstCount + 1
        elif secondCard == None or secondCard == card:
            secondCard = card
            secondCount = secondCount + 1
        elif thirdCard == None or thirdCard == card:
            thirdCard = card
            thirdCount = thirdCount + 1
        else:
            return False
    if (firstCount == 2 and secondCount == 2) or (firstCount == 2 and thirdCount == 2) or (thirdCount == 2 and secondCount == 2):
        return True
    return False

def isPair(bid):
    firstCard = None
    firstCount = 0
    secondCard = None
    secondCount = 0
    thirdCard = None
    thirdCount = 0
    fourthCard = None
    fourthCount = 0
    for card in bid[0]:
        if firstCard == None or firstCard == card:
            firstCard = card
            firstCount = firstCount + 1
        elif secondCard == None or secondCard == card:
            secondCard = card
            secondCount = secondCount + 1
        elif thirdCard == None or thirdCard == card:
            thirdCard = card
            thirdCount = thirdCount + 1
        elif fourthCard == None or fourthCard == card:
            fourthCard = card
            fourthCount = fourthCount + 1
        else:
            return False
    if firstCount == 2 or secondCount == 2 or thirdCount == 2 or fourthCount == 2:
        return True
    return False

def isFiveWild(bid):
    wildCount = 0
    for card in bid[0]:
        if card == 'J':
            wildCount = wildCount + 1
    if wildCount == 0:
        return isFiveOfAKind(bid)
    if wildCount == 1:
        return isFourOfAKind(bid)
    if wildCount == 2 or wildCount == 3:
        return isFullHouse(bid)
    return True

def isFourWild(bid):
    wildCount = 0
    for card in bid[0]:
        if card == 'J':
            wildCount = wildCount + 1
    if wildCount == 0:
        return isFourOfAKind(bid)
    if wildCount == 1:
        return isThreeOfAKind(bid)
    if wildCount == 2:
        return isTwoPair(bid)
    return True

def isFullHouseWild(bid):
    wildCount = 0
    for card in bid[0]:
        if card == 'J':
            wildCount = wildCount + 1
    if wildCount == 0:
        return isFullHouse(bid)
    if wildCount == 1:
        return isThreeOfAKind(bid) or isTwoPair(bid)
    if wildCount == 2:
        return isTwoPair(bid)
    return False

def isThreeWild(bid):
    wildCount = 0
    for card in bid[0]:
        if card == 'J':
            wildCount = wildCount + 1
    if wildCount == 0:
        return isThreeOfAKind(bid)
    if wildCount == 1:
        return isPair(bid)
    return True

def isTwoPairWild(bid):
    wildCount = 0
    for card in bid[0]:
        if card == 'J':
            wildCount = wildCount + 1
    if wildCount == 0:
        return isTwoPair(bid)
    if wildCount == 1:
        return isPair(bid)
    return True

def isPairWild(bid):
    wildCount = 0
    for card in bid[0]:
        if card == 'J':
            wildCount = wildCount + 1
    if wildCount == 0:
        return isPair(bid)
    return True
    
def part2(data):
    allBids = parseInput(data)
    fiveOfKinds = []
    fourOfKinds = []
    fullHouses = []
    threeOfKinds = []
    twoPairs = []
    pairs = []
    highCards = []
    
    for bid in allBids:
        if isFiveWild(bid):
            addToOrderedList(bid, fiveOfKinds, True)
        elif isFourWild(bid):
            addToOrderedList(bid, fourOfKinds, True)
        elif isFullHouseWild(bid):
            addToOrderedList(bid, fullHouses, True)
        elif isThreeWild(bid):
            addToOrderedList(bid, threeOfKinds, True)
        elif isTwoPairWild(bid):
            addToOrderedList(bid, twoPairs, True)
        elif isPairWild(bid):
            addToOrderedList(bid, pairs, True)
        else:
            addToOrderedList(bid, highCards, True)
    
    handsByRank = []
    handsByRank.append(highCards)
    handsByRank.append(pairs)
    handsByRank.append(twoPairs)
    handsByRank.append(threeOfKinds)
    handsByRank.append(fullHouses)
    handsByRank.append(fourOfKinds)
    handsByRank.append(fiveOfKinds)
    
    rank = 1
    winnings = 0
    for handList in handsByRank:
        for hand in handList:
            winnings = winnings + (rank * hand[1])
            rank = rank + 1

    print('Total winnings = ' + str(winnings))

part2(input)
