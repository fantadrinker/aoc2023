
data = open("data.txt", "r")
#data = open("testdata.txt", "r")

def compareHands(target, hand):
  target.sort()
  hand.sort()
  score = 0
  i = 0
  j = 0
  while i < len(target) and j < len(hand):
    if target[i] == hand[j]:
      score += 1
      i += 1
      j += 1
    elif target[i] < hand[j]:
      i += 1
    else:
      j += 1
  return score

sumScores = 0

next10 = [1] * 10

for line in data:
  [cardNum, cardInfo] = line.split(":")
  [cardTarget, cardHand] = cardInfo.split("|")
  cardTargetNums = [int(x) for x in cardTarget.strip().split(" ") if x != ""]
  cardHandNums = [int(x) for x in cardHand.strip().split(" ") if x != ""]
  wonCopies = compareHands(cardTargetNums, cardHandNums)
  currLineCopies = next10[0]
  for i in range(10):
    next10[i] = next10[i+1] if i < 9 else 1
    if i < wonCopies:
      next10[i] += currLineCopies
    
  print(f"Card {cardNum}: {currLineCopies} copies", next10)
  sumScores += currLineCopies

print(sumScores)