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


#------- part 2 -------

# reset sum counter
total_sum = 0

# same basic structure as part 1
for column in columns:
    operator = column[-1]
    
    num1_original = int(column[0])
    num2_original = int(column[1])
    num3_original = int(column[2])
    num4_original = int(column[3])

    num1_str = str(num1_original)
    num2_str = str(num2_original)
    num3_str = str(num3_original)
    num4_str = str(num4_original)

    # get max length to know how many columns
    max_len = max(len(num1_str), len(num2_str), len(num3_str), len(num4_str))

    # read right to left positions
    new_nums = []
    for pos in range(max_len):
        digits = ''
        for num_str in [num1_str, num2_str, num3_str, num4_str]:
            if len(num_str) > pos:
                digits += num_str[-(pos+1)]
        if digits:
            new_nums.append(int(digits))

    new_nums.reverse() 

    for num in new_nums:
        print(num)

    # apply the operator
    if operator == '+':
        total_sum += sum(new_nums)
    elif operator == '*':
        result = 1
        for num in new_nums:
            result *= num
        total_sum += result

print('part 2', total_sum)