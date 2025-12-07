# read in the given input for me 
with open('days/day6/day6_input.txt', 'r') as f:
    lines = f.read().split('\n')

rows = [line.split() for line in lines]
columns = [list(col) for col in zip(*rows)]


#------- part 1 -------

# sum counter
total_sum = 0

# loop through each column (now represented as an item in a list)
for column in columns:
    # find out the operator 
    operator = column[-1]
    
    # extract the 4 numbers 
    num1 = int(column[0])
    num2 = int(column[1])
    num3 = int(column[2])
    num4 = int(column[3])

    if operator == '+':
        total_sum += num1 + num2 + num3 + num4
    elif operator == '*':
        total_sum += num1 * num2 * num3 * num4

print('part 1', total_sum)