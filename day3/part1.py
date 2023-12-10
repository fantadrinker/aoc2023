# goal: sum of all numbers in the input file that:
# is adjacent to a symbol other than 'dot'

# 1. read the file
# 2. for each line and it's next line and previous lines, 
# get a list of indices of all symbols
# 3. when running each line, whenever a digit is found, check it's surrounding symbols.
import re

f = open("data.txt", "r")

def is_digit(char):
  return char.isdigit()

def is_symbol(char):
  return not char.isdigit() and char != '.' and char.strip() != ''

def get_number_at_index(line, index):
  # get number at index, return number and next index
  # first get to start of number
  i = index
  while i >= 0 and is_digit(line[i]):
    i -= 1
  i += 1

  match = re.search(r'\d+', line[i:]).group()

  return int(match), i + len(match), i


def process_line(line, prevLine):
  j = 0
  numbers = []
  currLineNums = {}
  prevLineNums = {}
  lookTopLeft = True
  skipTopUntil = -1
  while j < len(line):
    if line[j].isdigit():
      # only look left to avoid double counting with the second case for checking symbols
      is_next_to_symbol_to_left = j > 0 and is_symbol(line[j-1]) 
      # check top, top left and top right
      is_next_to_symbol_prev_line = prevLine and (is_symbol(prevLine[j]) or (j > 0 and is_symbol(prevLine[j-1])) or (j < len(line) - 1 and is_symbol(prevLine[j+1])))
      if is_next_to_symbol_to_left or is_next_to_symbol_prev_line:
        num, nextIndex, start = get_number_at_index(line, j)
        currLineNums[start] = num
        numbers.append(num)
        j = nextIndex
      else:
        j += 1
    elif is_symbol(line[j]):
      # current line
      if j > 0 and line[j-1].isdigit():
        numLeft, _, start = get_number_at_index(line, j-1)
        currLineNums[start] = numLeft
        numbers.append(numLeft) 
      # previous line, this is gonna double count
      # e.g. ..678..
      #      ..*.&%.
      # 678 is going to get counted three times
      # to solve this, when we get the number back, we also return the next index that isn't a digit
      num = None
      nextIndex = None
      start = None
      if not prevLine or skipTopUntil > j:
        j += 1
        continue

      if prevLine and prevLine[j].isdigit():
        # check if number is directly above the symbol
        # ..678..
        # ...&...
        num, nextIndex, start = get_number_at_index(prevLine, j)
        prevLineNums[start] = num
        if nextIndex > skipTopUntil:
          skipTopUntil = nextIndex
        #print("found number at top", num, nextIndex)

      if prevLine and lookTopLeft and j > 0 and prevLine[j-1].isdigit():
        # check if number is to the top left of the symbol
        # ..678..
        # .....&.
        num, nextIndex, start = get_number_at_index(prevLine, j-1)
        prevLineNums[start] = num
        if nextIndex > skipTopUntil:
          skipTopUntil = nextIndex
        #print("found number at top left", num, nextIndex)

      if prevLine and j < len(prevLine) - 1 and prevLine[j+1].isdigit():
        # check if number is to the top right of the symbol
        # ..678..
        # .*.....
        num, nextIndex, start = get_number_at_index(prevLine, j+1)
        lookTopLeft = False
        prevLineNums[start] = num
        if nextIndex > skipTopUntil:
          skipTopUntil = nextIndex
        #print("found number at top right", num, nextIndex)
      j += 1
    else:
      j += 1
      lookTopLeft = True
  return currLineNums, prevLineNums
i = 0
prevLine = None

result = 0
totalCount = 0
prevResults = {}
for line in f:
  currLineNums, prevLineNums = process_line(line, prevLine)
  if i > 0:
    print(f"line {i - 1}: ", len(prevLineNums), prevLineNums)
  print(f"line {i}: ", len(currLineNums), currLineNums)
  for (index, num) in prevLineNums.items():
    if index not in prevResults:
      totalCount += 1
      result += num
    else:
      print(prevResults)
      print("duplicate found: ", index, num)
  for (index, num) in currLineNums.items():
    totalCount += 1
    result += num
  prevLine = line
  prevResults = currLineNums
  i += 1
print("total sums is: ", result)
print("total count is: ", totalCount)