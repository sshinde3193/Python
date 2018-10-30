from Task_6 import HashTable
import string


common = 0
uncommon = 0                                                        # initialise four variables
rare = 0
misspelled = 0

file = 'book2.txt'
infile = open(file, 'r')                                            # read new book
for line in infile:
    n = line.strip('\n').split()                                    # process each word
    for x in n:
        x = x.strip(string.punctuation).lower()
        try:
            if HashTable[x] >= (HashTable.maximum_frequency / 100):                 # check rarity of each word using max freq of hashtable
                common += 1
            elif HashTable[x] >= (HashTable.maximum_frequency / 1000):
                uncommon += 1
            else:
                rare += 1
        except:
            misspelled += 1

total = common + uncommon + rare + misspelled
common_percentage = (common / total) * 100                                          # calculate percentages
uncommon_percentage = (uncommon / total) * 100
rare_percentage = (rare / total) * 100
misspelled_percentage = (misspelled / total) * 100


print('common words percentage: ' + str(common_percentage))
print('uncommon words percentage: ' + str(uncommon_percentage))                           # print percentages
print('rare words percentage: ' + str(rare_percentage))
print('misspelled words percentage: ' + str(misspelled_percentage))
