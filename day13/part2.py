from lib import getNextPuzzle, findMirrorHorizontal, findMirrorVertical, getAllPossibleFlips, printPuzzle

def __main__():
  f = open("data.txt", "r")
  horizontalSum = 0
  verticalSum = 0
  i = 0
  while True:
    i += 1
    puzzle = getNextPuzzle(f)
    if not puzzle:
      break
    # first find the original mirror
    horizontalMirrorOG = findMirrorHorizontal(puzzle)
    verticalMirrorOG = findMirrorVertical(puzzle)
    found = False
    # add in a step: to flip 1 bit of the puzzle
    allPossibleFlips = getAllPossibleFlips(puzzle)
    print(f"Case {i} OG: {horizontalMirrorOG} {verticalMirrorOG}, all possible flips: {len(allPossibleFlips)}")
    for flip in allPossibleFlips:
      horizontalMirror = findMirrorHorizontal(flip, avoid=horizontalMirrorOG)
      verticalMirror = findMirrorVertical(flip, avoid=verticalMirrorOG)

      if horizontalMirror > 0 and horizontalMirror != horizontalMirrorOG:
        horizontalSum += horizontalMirror
        print(f"Case {i}: {horizontalMirror} {verticalMirror}")
        # printPuzzle(flip)
        found = True
        break
      if verticalMirror > 0 and verticalMirror != verticalMirrorOG:
        verticalSum += verticalMirror
        print(f"Case {i}: {horizontalMirror} {verticalMirror}")
        # printPuzzle(flip)
        found  = True
        break
    if not found:
      print(f"case {i} not found")
      printPuzzle(puzzle)
  f.close()
  print(f"Horizontal sum: {horizontalSum}")
  print(f"Vertical sum: {verticalSum}")
  print(f"answer key: {horizontalSum + 100 * verticalSum}")
  pass

if __name__ == "__main__":
  __main__()