#Cameron Whittemore 
# Assignment description: this program reads a csv file of movies and stores it in hash tables. 
#I tested different hash functions/collision handling strategies to see how they affected collisions, space, and performance.
#4/10/26 

import csv 
import time 



movies = [] 

file = open('movies.csv', 'r', encoding='utf-8') 
reader = csv.reader(file) 

next(reader) #skips header

for row in reader:
    if len(row) < 9: 
        continue 


    title = row[0].strip()
    qoute = row[8].strip() 

    if title == "" or qoute == "":
        continue

    movies.append((title, qoute)) 

file.close() 

#setup hash tables 

table_size = 20000 
hashTable = [None] * table_size 
collisions = 0

for i in range(5):
    print("Title:", movies[i][0]) 
    print("Quote:", movies[i][1])
    print()


#better hash this time 

def simpleHash(key): 
    total = 0 
    for char in key:  
        total = total * 31 + ord(char) 
    return total % table_size 
    
for i in range(len(movies)):
    title = movies[i][0] 

    index = simpleHash(title) 

    if hashTable[index] != None: 
        collisions = collisions + 1 

    hashTable[index] = movies[i]

#Qoute hash table with linear probing

quoteHashTable = [None] * table_size
qouteCollisions = 0 

start = time.time() 

for i in range(len(movies)): 
    qoute = movies[i][1] 

    index = simpleHash(qoute) 

    if quoteHashTable[index] != None: 
        qouteCollisions = qouteCollisions + 1 

    while quoteHashTable[index] != None: 
        index = (index + 1) % table_size 

    quoteHashTable[index] = movies[i] 
end = time.time() 

qouteBuildTime = end - start

qouteEmpty = 0 
for i in range(len(quoteHashTable)):
    if quoteHashTable[i] == None:
        qouteEmpty = qouteEmpty + 1 


#title hash table with linear probing

titleHashTable = [None] * table_size
titleCollisions = 0 

start = time.time() 

for i in range(len(movies)): 
    title = movies[i][0] 
    index = simpleHash(title) 

    if titleHashTable[index] != None: 
        titleCollisions = titleCollisions + 1 

    while titleHashTable[index] != None: 
        index = (index + 1) % table_size 

    titleHashTable[index] = movies[i]
end = time.time() 

titlebuildTime = end - start
titleEmpty = 0 

for i in range(len(titleHashTable)):
    if titleHashTable[i] == None:
        titleEmpty = titleEmpty + 1


print("Title Hash Table Collisions:", titleCollisions)
print("Title Hash Table Empty Slots:", titleEmpty)
print("Title Hash Table Build Time:", titlebuildTime, "seconds")

print("Quote Hash Table Collisions:", qouteCollisions)
print("Quote Hash Table Empty Slots:", qouteEmpty)
print("Quote Hash Table Build Time:", qouteBuildTime, "seconds")