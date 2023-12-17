from lib import getNextPuzzle, findMirrorHorizontal, findMirrorVertical, getAllPossibleFlips, printPuzzle
problematic = [
  4,
  20,
  30,
  56,
  64,
  82,
  86,
]
def __main__():
  verticalMirrors = []
  horizontalMirrors = []
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
    # print(f"Case {i} OG: {horizontalMirrorOG} {verticalMirrorOG}, all possible flips: {len(allPossibleFlips)}")
    for flip in allPossibleFlips:
      horizontalMirror = findMirrorHorizontal(flip, avoid=horizontalMirrorOG)
      verticalMirror = findMirrorVertical(flip, avoid=verticalMirrorOG)

      if horizontalMirror > 0 and horizontalMirror != horizontalMirrorOG:
        if not found:
          horizontalSum += horizontalMirror
          found = True
        print(f"{i}, {horizontalMirror}, vertical;")
        if i in problematic:
          printPuzzle(puzzle)
          print('flip')
          printPuzzle(flip)
        break
      if verticalMirror > 0 and verticalMirror != verticalMirrorOG:
        if not found:
          verticalSum += verticalMirror
          found  = True
        print(f"{i}, {verticalMirror}, horizontal;")
        # printPuzzle(flip
        if i in problematic:
          printPuzzle(puzzle)
          print('flip')
          printPuzzle(flip)
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