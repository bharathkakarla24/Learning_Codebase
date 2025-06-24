# Why Loops in DevOps?
# Loops help automate repetitive tasks, like:
# Iterating over server IPs
# Processing logs line-by-line
# Checking statuses in batch


#while loop () : If we dont know number of times the loop needs to be
# Syntax:

# while condition:
      # do something

count = 1
while count < 3:
    print("Checking system...")
    count += 1


#for loop : We know the value no of times the loop will iterate.
# for item in iterable:
      # do something

#Loop over list of regions
regions = ["us-east-1", "us-west-2", "eu-central-1"]
for region in regions:
    print("Checking region:", region)


# Loop over numbers
for i in range(1, 6):
    print("Try attempt:", i)
    
    


#break and continue

#break: Exit the loop
for i in range(10):
    if i == 5:
        break
    print(i)

# continue: Skip current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)


# List Comprehension
#A compact way to build lists.

squares = [x*x for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
