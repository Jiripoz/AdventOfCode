# First Problem: 
# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
elfs = open('input_day1.txt', 'r').readlines()
elfs_calories = [0]

for calories in elfs:
    if calories!='\n':    
        elfs_calories[-1]=elfs_calories[-1]+int(calories)
        continue
    elfs_calories.append(0)

print(elfs_calories)
print('the elf carrying most calories is carrying %i calories'%max(elfs_calories))

# Second Problem: 
# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

elfs_calories.sort()
print('top three elfs are: ', elfs_calories[-3:])
print('the total sum is: %i'%sum(elfs_calories[-3:]))