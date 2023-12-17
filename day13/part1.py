from lib import getNextPuzzle, findMirrorHorizontal, findMirrorVertical

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
    horizontalMirror = findMirrorHorizontal(puzzle)
    verticalMirror = findMirrorVertical(puzzle)
    print(f"Case {i}: {horizontalMirror} {verticalMirror}")
    if horizontalMirror > 0:
      horizontalSum += horizontalMirror
      continue
    elif verticalMirror > 0:
      verticalSum += verticalMirror
  f.close()
  print(f"Horizontal sum: {horizontalSum}")
  print(f"Vertical sum: {verticalSum}")
  print(f"answer key: {horizontalSum + 100 * verticalSum}")

if __name__ == "__main__":
  __main__()