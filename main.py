

def arithmic(problems, workout=False):
    # check if it has 5 or less problems
    if len(problems) > 5:
        # print("Error: Too many problems.")
        return "Error: Too many problems."

    first_nums = []
    plus_minus = []
    second_nums = []

    for item in problems:
        x = item.split()
        first_nums.append(x[0])
        plus_minus.append(x[1])
        second_nums.append(x[2])

        # check if correct operator
        if x[1] == '/' or x[1] == '*':
            return "Error: Operator must be '+' or '-'."

        first = x[0]
        second = x[2]

        # checking if the input is all numeric/ no letters
        if not first.isnumeric() or not second.isnumeric():
            return "Error: Numbers must only contain digits."

        # check length of numbers

        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."
        # elif len(first) >= len(second):
        #     length = len(first)
        # else:
        #     length = len(second)

    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    for item in range(len(first_nums)):

        if len(first_nums[item]) >= len(second_nums[item]):
            first_line.append(' '*2 + first_nums[item])
        else:
            first_line.append(' '*2 + (len(second_nums[item]) - len(first_nums[item]))*" " + first_nums[item])

    for item in range(len(second_nums)):

        if len(first_nums[item]) >= len(second_nums[item]):
            second_line.append('+ ' + (len(first_nums[item]) - len(second_nums[item])) * ' ' + second_nums[item])
        else:
            second_line.append('+ ' + second_nums[item])

    for item in range(len(first_nums)):
        if len(first_nums[item]) >= len(second_nums[item]):
            third_line.append('_' * (len(first_nums[item]) + 2))
        else:
            third_line.append('_' * (len(second_nums[item]) + 2))

    if workout:
        for item in range(len(first_nums)):
            if plus_minus[item] == '+':
                result_plus = int(first_nums[item]) + int(second_nums[item])
                fourth_line.append(' '*(len(third_line[item])-len(str(result_plus) )) + str(result_plus))
            elif plus_minus[item] == '-':
                result_minus = first_nums[item] - second_nums[item]
                fourth_line.append(' ' * (len(third_line[item]) - len(str(result_minus))) + str(result_minus))


    spacer = '    '

    line1 = spacer.join(first_line)
    line2 = spacer.join(second_line)
    line3 = spacer.join(third_line)
    line4 = spacer.join(fourth_line)

    print(line1)
    print(line2)
    print(line3)
    if workout:
        print(line4)





arithmic(['21 + 111', '32 + 2', '6 + 5'])