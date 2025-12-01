# read in the given input for me 
with open('days\day1\day1_input.txt', 'r') as f:
    rotations = f.read().splitlines()

#------- part 1 -------
# as stated, set the starting position to 50
position = 50
# set a counter to track each time 0 happens
count = 0 

# loop through each rotation in the input 
for rotation in rotations: 
    # parse the first character to find out L or R 
    direction = rotation[0]
    # parse how big of a rotation (everything after L or R)
    mag =  int(rotation[1:])
    # if the direction is left we know that we moving the tick 'toward lower numbers'
    if direction == 'L':
        vec = -mag 
    elif direction == 'R':
        vec = mag
    # we can use modulo to handle rotations that go above/below 99
    # we can confirm using https://www.calculatorsoup.com/calculators/math/modulo-calculator.php
    position = (position + vec) % 100
    # add to counter if 0 
    if position == 0:
        count += 1

print("part 1: ",count) 

#------- part 2 -------
# reset the counter and position for part 2
count = 0
position = 50 

# similar start to part 1
for rotation in rotations: 
    direction = rotation[0]
    mag = int(rotation[1:])
    if direction == 'R':
        vec = mag
        # count how many times we cross through 0 during the rotation
        # we divide by 100 to see how many laps we complete
        # subtract where we started from where we end to get the number of crossings
        zeros = (position + mag) // 100 - position // 100
    # left rotations are a bit trickier
    elif direction == 'L':
        vec = -mag 
        # if we're starting at 0, we don't immediately hit 0 (we go to 99 first)
        # so we only count complete laps
        if position == 0:
            zeros = mag // 100
        # if the magnitude is large enough to reach 0 from our current position
        elif mag >= position:
            # count how many times we pass through 0
            # we subtract position to account for the distance to reach 0 the first time
            # then add 1 because we do hit 0 that first time
            zeros = (mag - position) // 100 + 1
        # if the magnitude isn't large enough to reach 0, we don't cross it
        else:
            zeros = 0
    position = (position + vec) % 100
    # add the number of times we crossed 0 to our total count
    count += zeros

print("part 2:", count)