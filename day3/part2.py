

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


i = 0
prevLine = None

result = 0
sample_gear = {
  "line": 100,
  "position": 40,
  "numbers": [300, 32]
}
sample_gears_map = {
  32: [300, 32],
  54: [],
  93: [774]
}
gears_map = []
line_map = []
for line in f:
  line_map.append(line[:-1])

for line in line_map:
  j = 0
  gears = {}
  while j < len(line):
    if line[j] == '*':
      gears[j] = []
      # check left
      if j > 0 and line[j-1].isdigit():
        num, _, start = get_number_at_index(line, j-1)
        gears[j].append(num)
      # check right
      if j < len(line) - 1 and line[j+1].isdigit():
        num, _, start = get_number_at_index(line, j+1)
        gears[j].append(num)
      # check top
      if i > 0:
        prevLine = line_map[i-1]
        top_j = j - 1
        while top_j < len(prevLine) and top_j <= j + 1:
          if prevLine[top_j].isdigit():
            num, top_j, start = get_number_at_index(prevLine, top_j)
            gears[j].append(num)
          else:
            top_j += 1
      # check bottom
      if i < len(line_map) - 1:
        nextLine = line_map[i+1]
        bot_j = j - 1
        while bot_j < len(nextLine) and bot_j <= j + 1:
          if nextLine[bot_j].isdigit():
            num, bot_j, start = get_number_at_index(nextLine, bot_j)
            gears[j].append(num)
          else:
            bot_j += 1
    j += 1
  gears_map.append(gears)
  for (key, value) in gears.items():
    if len(value) == 2:
      result += value[0] * value[1]
  i += 1

print(result)