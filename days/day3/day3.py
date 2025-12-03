# read in the given input for me 
with open('days\day3\day3_input.txt', 'r') as f:
    banks = f.read().splitlines()

#------- part 1 -------

# joltage counter
total_joltage = 0 

# loop through each bank
for bank in banks:
    # pseudo code idea:
        # find largest digit except for the last
        # if there are multiple pick first
        # find the largest digit from that position onwards
    f_large = max(bank[:-1])
    f_position = bank.index(f_large)
    s_large = max(bank[f_position+1:])
    joltage = int(str(f_large) + str(s_large))
    total_joltage+=joltage

print("part 1", total_joltage)

#------- part 2 -------

# reset joltage counter
total_joltage = 0 

for bank in banks:
    # pseudo code idea:
        # find largest digit with atleast 12 digit
        # ensure each next digit has to be atleast 12 - n digits left
        # find the largest digit that meets the criteria 
    # empty string to store each digit
    optimal = ""
    start_position = 0
    # loop through 1 digits
    for i in range(12):
        # make sure we still have enough space left 
        min_space = 12 - i - 1
        # we can only search as long as the bank is WITH the min space
        max_search = len(bank) - min_space
        # store the largest
        largest = max(bank[start_position:max_search])
        # find the largest position (from the start position as we dont want to go backwards later)
        l_position = bank.index(largest, start_position)
        # add it to the string
        optimal += largest
        # update our start_position
        start_position = l_position + 1 
    
    total_joltage += int(optimal)


print("part 2", total_joltage)