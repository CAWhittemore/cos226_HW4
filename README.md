Reflection

For this assignment, I tested five different hash table approaches using movie titles and movie quotes as keys.

Attempt 1: I used a very simple hash function and a small table size of 1000. This caused a very large number of collisions and no empty slots, showing that the table was too small.

Attempt 2: I kept the simple hash function but changed the table size to 20000. This reduced collisions a lot and created many empty slots.

Attempt 3: I used the larger table size and a better hash function that multiplied the running total by 31 before adding each character, which improved how keys were distributed across the table.

Attempt 4: I used chaining to handle collisions. Instead of replacing old values, each bucket stored a list of movies. 

Attempt 5: I used linear probing. When a collision happened, the program moved forward until it found an empty slot. This also stored all records correctly, but it took longer than chaining.

The best methods were chaining and linear probing because they handled collisions correctly without losing data. The larger table size and better hash function also helped reduce collisions. I learned that hash function design and collision-handling strategies make a large difference in a hash table’s performance.

