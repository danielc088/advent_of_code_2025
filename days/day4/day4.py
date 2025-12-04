# read in the given input for me 
with open('days\day4\day4_input.txt', 'r') as f:
    paper_position = f.read().splitlines()

#------- part 1 -------

# rolls counter
total_rolls = 0 

# loop through each row
for row_idx in range(len(paper_position)):
    # loop through each column in the row
    for col_idx in range(len(paper_position[row_idx])):
        # check if current position is '@'
        if paper_position[row_idx][col_idx] == '@':
            # counter for adjacent '@' symbols
            adj_count = 0
            # check all 8 adjacent positions like a king in chess
            # row offsets
            for dr in [-1, 0, 1]:
                # column offsets
                for dc in [-1, 0, 1]: 
                    # skip the center position (current @)
                    if dr == 0 and dc == 0:
                        continue
                    # calculate neighbor position
                    new_row = row_idx + dr
                    new_col = col_idx + dc
                    # check if neighbor is within bounds
                    if 0 <= new_row < len(paper_position) and 0 <= new_col < len(paper_position[new_row]):
                        # check if neighbor is '@'
                        if paper_position[new_row][new_col] == '@':
                            adj_count += 1
            # if fewer than 4 adjacent @ we can add it
            if adj_count < 4:
                total_rolls += 1

print("part 1:", total_rolls)

#------- part 2 -------

# convert to mutable list of lists as we want to be able to update it with x -> .
paper_position = [list(row) for row in paper_position]

# rolls counter
total_rolls = 0 

# any left for our while loop
any_left = True

while any_left:
    # firslt assume that there are no more accessible rolls
    any_left = False 
    
    # exact same as before
    for row_idx in range(len(paper_position)):
        for col_idx in range(len(paper_position[row_idx])):
            if paper_position[row_idx][col_idx] == '@':
                adj_count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]: 
                        if dr == 0 and dc == 0:
                            continue
                        new_row = row_idx + dr
                        new_col = col_idx + dc
                        if 0 <= new_row < len(paper_position) and 0 <= new_col < len(paper_position[new_row]):
                            if paper_position[new_row][new_col] == '@':
                                adj_count += 1
                if adj_count < 4:
                    total_rolls += 1
                    # difference now is we update the list
                    paper_position[row_idx][col_idx] = '.'
                    # since we found something we need to keep going
                    any_left = True 

print("part 2:", total_rolls)