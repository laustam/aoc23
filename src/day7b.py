file = open("input/day7", "r")

class Hand:
    def __init__(self, hand: str, bid: int) -> None:
        self.hand: str = hand
        self.bid: int = bid
    
rel_strength: dict[int] = {
    "A" : 13,
    "K" : 12,
    "Q" : 11,
    "T" : 9,
    "9" : 8,
    "8" : 7,
    "7" : 6,
    "6" : 5,
    "5" : 4,
    "4" : 3,
    "3" : 2,
    "2" : 1,
    "J" : 0,
}

def sort_hand(hand: Hand) -> list[int]:
    return [rel_strength.get(card) for card in hand.hand]

# 1. group by type
type_5_eq: list[Hand] = []
type_4_eq: list[Hand] = []
type_3_2_eq: list[Hand] = []
type_3_eq: list[Hand] = []
type_2_pairs: list[Hand] = []
type_1_pair: list[Hand] = []
type_all_diff: list[Hand] = []

for line in file:
    hand, bid = line.strip().split(" ")
    new_hand: Hand = Hand(hand=hand, bid=int(bid))

    card_count = {}
    for card in hand:
        card_count[card] = card_count.get(card, 0) + 1

    max_eq: int = max([value if key != 'J' else 0 for key, value in card_count.items()])
    eq_card_count: int = len(card_count)

    print(hand, max_eq, eq_card_count)

    if max_eq == 5 or max_eq + card_count.get('J', 0) == 5:
        type_5_eq.append(new_hand)
    elif max_eq == 4 or max_eq + card_count.get('J', 0) == 4:
        type_4_eq.append(new_hand)
    elif (max_eq == 3 or max_eq + card_count.get('J', 0)) and (eq_card_count == 2 or 'J' in card_count and eq_card_count - 1 == 2):
        type_3_2_eq.append(new_hand)
    elif max_eq == 3 or max_eq + card_count.get('J', 0) == 3:
        type_3_eq.append(new_hand)
    elif (max_eq == 2 or max_eq + card_count.get('J', 0) == 2) and (eq_card_count == 3 or 'J' in card_count and eq_card_count - 1 == 2):
        type_2_pairs.append(new_hand)
    elif max_eq == 2 or max_eq + card_count.get('J', 0) == 2:
        type_1_pair.append(new_hand)
    else:
        type_all_diff.append(new_hand)

# 2. sort types
type_5_eq = sorted(type_5_eq, key=sort_hand)
type_4_eq = sorted(type_4_eq, key=sort_hand)
type_3_2_eq = sorted(type_3_2_eq, key=sort_hand)
type_3_eq = sorted(type_3_eq, key=sort_hand)
type_2_pairs = sorted(type_2_pairs, key=sort_hand)
type_1_pair = sorted(type_1_pair, key=sort_hand)
type_all_diff = sorted(type_all_diff, key=sort_hand)
sorted_hands: list[Hand] =  type_all_diff + type_1_pair + type_2_pairs + type_3_eq + type_3_2_eq + type_4_eq + type_5_eq

# 3. compute total winnings
total_winnings: int = 0

for i in range(len(sorted_hands)):
    rank: int = i + 1
    hand: Hand = sorted_hands[i]
    total_winnings += rank * hand.bid

print(total_winnings)