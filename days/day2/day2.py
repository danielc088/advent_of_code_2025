# read in the given input for me 
with open('days\day2\day2_input.txt', 'r') as f:
    ids = f.read().splitlines()

# split each line by commas
all_ranges = []
for line in ids:
    all_ranges.extend(line.split(','))

#------- part 1 -------

# invalid counter
invalids = 0 

# loop through each id 
for id in all_ranges:
    # find the lower and upper bound
    low, upp = map(int, id.split('-'))
    # loop through each number within the range
    for num in range(low, upp+1):
        num_str = str(num)
        # testing if odd
        if len(num_str) % 2 == 1:
            continue
        else:
            # split the number in half
            mid = len(num_str) // 2
            first_half = num_str[:mid] 
            second_half = num_str[mid:]
            # check if first and second half are equal
            if first_half == second_half:
                invalids += num
                continue
            continue 

print("part 1:",invalids)

#------- part 2 -------

# reset counter
invalids = 0 

# loop through each id 
for id in all_ranges:
    # find the lower and upper bound
    low, upp = map(int, id.split('-'))
    # loop through each number within the range
    for num in range(low, upp+1):
        num_str = str(num)
        # i want to loop through each possible pattern length (obviously half being the max)
        for pattern_len in range(1, len(num_str)//2 + 1):
            # the pattern length needs to be perfectly divisible for it to be potentially invalid
            if len(num_str) % pattern_len != 0:
                continue
            # we can now look for the pattern
            pattern = num_str[:pattern_len]
            # if we repeat the pattern x times does it look like the number
            if pattern * (len(num_str) // pattern_len) == num_str:
                invalids+=num
                # move on to next number
                break

print("part 2:",invalids)
