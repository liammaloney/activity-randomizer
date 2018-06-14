import random
import csv

import csv
with open('../data/data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        rows=[r for r in reader]

randInt = random.randint(0,270)

print('Welcome to the Simpsons Randomizer. The Simpsons episode you should watch is:')
print("Season "+rows[randInt][0]+", Episode "+rows[randInt][1])