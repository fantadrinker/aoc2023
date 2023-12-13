# need to rethink this approach

# start from the lowest range in the last step.
# back trace the range of numbers in the seed that could have produced this range



mappingFilesList = [
  'data-seed-soil.txt',
  'data-soil-fertilizer.txt',
  'data-fert-water.txt',
  'data-water-light.txt',
  'data-light-temp.txt',
  'data-temp-humidity.txt',
  'data-hum-loc.txt'
]

def parseMappingFile(file):
  mapFile = open(file, 'r')
  mapping = []
  for line in mapFile:
    [dest, src, rangeNum] = [int(x) for x in line.split(' ') if x != '']
    mapping.append({
      'dest': dest,
      'src': src,
      'range': rangeNum
    })
  return mapping

mappingsList = [parseMappingFile(file) for file in mappingFilesList]
reverseMappingsList = mappingsList[-1::-1]

seedsInput = open('data-seeds.txt', 'r')
seeds = [int(x) for x in seedsInput.read().split(' ') if x != '']


def backTraceRange(ranges, nextMappings):
  # sample range item: { start: 10, range: 20 }
  # sample nextMappings: [{ dest: 20, src: 10, range: 5 }, { dest: 20, src: 10, range: 5 }]
  # should return a list of range items 
  result = []
  toDoStack = ranges.copy()
  while toDoStack:
    currRange = toDoStack.pop()
    foundOverlap = False
    for nextMapping in nextMappings:
      # if mapping has no overlap with current range, skip
      if nextMapping['dest'] >= currRange['start'] + currRange['range'] or nextMapping['dest'] + nextMapping['range'] <= currRange['start']:
        continue

      foundOverlap = True
      # main segment.
      overlapStart = max(currRange['start'], nextMapping['src'])
      overlapEnd = min(currRange['start'] + currRange['range'], nextMapping['dest'] + nextMapping['range'])
      if overlapStart >= overlapEnd:
        continue
      result.append({
        'start': overlapStart,
        'range': overlapEnd - overlapStart
      })
      print(f"found overlap: {overlapStart}, {overlapEnd}, {currRange}")
      # now we decide left over part of the current range need to be popped back to the stack
      if currRange['start'] < overlapStart:
        toDoStack.append({
          'start': currRange['start'],
          'range': overlapStart - currRange['start']
        })
      if currRange['start'] + currRange['range'] > overlapEnd:
        toDoStack.append({
          'start': overlapEnd,
          'range': currRange['start'] + currRange['range'] - overlapEnd
        })

    # now we deal with case if there is no overlap
    if not foundOverlap:
      result.append(currRange)
  
  return result

def checkOverlap(rangeItems1, rangeItems2):
  overlap = []
  for rangeItem1 in rangeItems1:
    for rangeItem2 in rangeItems2:
      if rangeItem1['start'] < rangeItem2['start'] + rangeItem2['range'] and rangeItem1['start'] + rangeItem1['range'] > rangeItem2['start']:
        overlap.append({
          'start': max(rangeItem1['start'], rangeItem2['start']),
          'range': min(rangeItem1['start'] + rangeItem1['range'], rangeItem2['start'] + rangeItem2['range']) - max(rangeItem1['start'], rangeItem2['start'])
        })
  return overlap

def getNextKey(key, mapping):
  # for given key id, get the next key from parsing the file
  for mapItem in mapping:
    #print(f"Key: {key}, mapItem: {mapItem}")
    dist = key - mapItem['src']
    if dist >= 0 and dist < mapItem['range']:
      return mapItem['dest'] + dist
  return key

def expandOverlapSeeds(overlap):
  result = []
  for rangeItem in overlap:
    result += range(rangeItem['start'], rangeItem['start'] + rangeItem['range'])
  return result

def readSeedsIntoRangeItems(seeds):
  currNum = None
  result = []

  for num in seeds:
    if not currNum:
      currNum = num
      continue
    else:
      result.append({
        'start': currNum,
        'range': num
      })
      currNum = None
  
  return result



locationsMapping = parseMappingFile('data-hum-loc.txt')
locationsMapping.sort(key=lambda x: x['dest'])
for mapItem in locationsMapping:
  # first translate the mapitem to a range item
  rangeItems = [{
    'start': mapItem['src'],
    'range': mapItem['range']
  }]
  print('working on final mapping range', mapItem)
  # then loop over the mappings and find the ones that overlap with this range
  i = 0
  for mappings in reverseMappingsList:
    print('back tracing mapping', i)
    i += 1
    rangeItems = backTraceRange(rangeItems, mappings)
  # then we need a function that checks if two lists of rangeitems overlap
  overlap = checkOverlap(rangeItems, readSeedsIntoRangeItems(seeds)) 
  if overlap:
    print(f"found overlap: {overlap}")
    overlapSeeds = expandOverlapSeeds(overlap)
    print(f"total number of overlap seeds: {len(overlapSeeds)}")
    j = 0
    for mapping in mappingsList:
      print(f"forward trace mapping: {j}")
      j += 1
      overlapSeeds = [getNextKey(seed, mapping) for seed in overlapSeeds]
    print(f"min seeds: {min(overlapSeeds)}")
