def expandSeeds(seeds):
  currNum = None
  result = []

  for num in seeds:
    if not currNum:
      currNum = num
      continue
    else:
      result += range(currNum, currNum + num)
      currNum = None
  
  return result

testSeeds = [79, 14, 55, 13]
print("test expand seeds", len(expandSeeds(testSeeds)))

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

def getNextKey(key, mapping):
  # for given key id, get the next key from parsing the file
  for mapItem in mapping:
    #print(f"Key: {key}, mapItem: {mapItem}")
    dist = key - mapItem['src']
    if dist >= 0 and dist < mapItem['range']:
      return mapItem['dest'] + dist
  return key

mappingFilesList = [
  'data-seed-soil.txt',
  'data-soil-fertilizer.txt',
  'data-fert-water.txt',
  'data-water-light.txt',
  'data-light-temp.txt',
  'data-temp-humidity.txt',
  'data-hum-loc.txt',
]

seedsInput = open('data-seeds.txt', 'r')
seeds = [int(x) for x in seedsInput.read().split(' ') if x != '']

part2seeds = expandSeeds(seeds)

print('got part 2 seeds', len(part2seeds))

for mappingFile in mappingFilesList:
  mapping = parseMappingFile(mappingFile)
  part2seeds = [getNextKey(seed, mapping) for seed in part2seeds]
  print(f"Mapping file: {mappingFile}, seeds: {min(part2seeds)}")
  #print(f"Mapping file: {mappingFile}, seeds: {seeds}")

print(min(part2seeds))