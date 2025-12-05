# read in the given input for me 
with open('days/day5/day5_input.txt', 'r') as f:
    inventory = f.read().split('\n\n')

fresh = inventory[0].splitlines()
ingredients = inventory[1].splitlines()

#------- part 1 -------

# counter for ingredients that are fresh
available = 0

# loop over each ingredient
for ingredient in ingredients:
    # loop over each fresh ingredient range
    for f in fresh:
        # extract the lower and upper bound
        lower, upper = map(int, f.split('-'))
        # simple check if the ingredient is within the bound
        if lower <= int(ingredient) <= upper:
            available += 1
            # if it is great lets stop this loop
            break

print('part 1', available)


