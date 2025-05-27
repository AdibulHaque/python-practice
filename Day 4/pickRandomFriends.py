# Figure out how to pick a random name from the list of friends.

import random
# Solution 1 with condition
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_number = random.randrange(5)
if random_number == 0:
    print("Alice")
elif random_number == 1:
    print("Bob")
elif random_number == 2:
    print("Charlie")
elif random_number == 3:
    print("David")
else:
    print("Emanuel")

#Solution 2 random.choice [Single random element from a sequence]
print(random.choice(friends))

#Solution 3 random.randint
random_index = random.randint(0,4) #we will get 0 to 4 including them
print(friends[random_index])
