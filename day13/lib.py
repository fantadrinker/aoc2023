# first read input

def getNextPuzzle(inputFile):
  puzzle = []
  while True:
    line = inputFile.readline()
    if line == "\n" or line == "":
      break
    puzzle.append(line[:-1] if line[-1] == "\n" else line)
  return puzzle

def getPuzzleSize(puzzle):
  return len(puzzle), len(puzzle[0])

def cmpRow(puzzle, row1, row2):
  return puzzle[row1] == puzzle[row2]

def cmpCol(puzzle, col1, col2):
  numRows, numCols = getPuzzleSize(puzzle)
  for i in range(numRows):
    if puzzle[i][col1] != puzzle[i][col2]:
      return False
  return True

def findMirrorHorizontal(puzzle):
  # to find horizontal, first try to match left-most column
  # with any other column. If found, then try to match  
  # columns in between them
  # if not found, try to match the right-most column and 
  # repeat the process
  _, numCols = getPuzzleSize(puzzle)
  for i in range(1, int(numCols/2)+1):
    # i is potential mirror position
    # print(f"compare cols {0} and {2*i - 1}")
    mirror = i
    if cmpCol(puzzle, 0, 2 * i - 1):
      # found a match, now try to match the columns in between
      isMirror = True
      # print(f"potential horizontal mirror at {mirror}")
      for j in range(1, i):
        if not cmpCol(puzzle, j, 2*i - j - 1): # i = 4, (1, 7), (2, 6), (3, 5)
          isMirror = False
          break
      if isMirror:
        return mirror
  # if we reach here, then repeat from the right
  for i in range(1, int(numCols/2)+1):
    # numCols - i - 1 is potential mirror position
    # print(f"compare cols {numCols - 1} and {numCols - 2*i}")
    mirror = numCols - i
    if cmpCol(puzzle, numCols - 1, numCols - 2*i):
      # found a match, now try to match the columns in between
      isMirror = True
      # print(f"potential horizontal mirror at {i}")
      for j in range(1, i):
        if not cmpCol(puzzle, numCols - 1 - j, numCols - 2*i + j):
          isMirror = False
          break
      if isMirror:
        return mirror
  return 0

def findMirrorVertical(puzzle):
  # to find vertical, first try to match top-most row
  # with any other row. If found, then try to match
  # rows in between them
  numRows, _ = getPuzzleSize(puzzle)
  for i in range(1, int(numRows/2)+1):
    # i is potential mirror position
    #print(f"compare {0} and {2*i - 1}")
    mirror = i
    if cmpRow(puzzle, 0, 2*i - 1):
      # found a match, now try to match the rows in between
      isMirror = True
      #print(f"potential vertical mirror at {mirror}")
      for j in range(1, i):
        if not cmpRow(puzzle, j, 2*i - 1 - j):
          isMirror = False
          break
      if isMirror:
        return mirror
  # if we reach here, then repeat from the bottom
  for i in range(1, int(numRows/2)+1):
    # i is potential mirror position
    # mirror position is numRows - 1 - i
    #print(f"compare {numRows - 1} and {numRows - 2*i}")
    mirror = numRows - i
    if cmpRow(puzzle, numRows - 1, numRows - 2*i):
      # found a match, now try to match the rows in between
      isMirror = True
      #print(f"potential vertical mirror at {mirror}")
      for j in range(1, i):
        if not cmpRow(puzzle, numRows - 1 - j, numRows - 2*i + j):
          isMirror = False
          break
      if isMirror:
        return mirror
  return 0