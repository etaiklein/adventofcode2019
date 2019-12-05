input_min = 136760
input_max = 595730
'''
--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 
'''

def is_solution(val):
    characters = list(str(val))
    prev_character = '-1'
    has_adjacent_duplicate = False
    for character_index in range(0, len(characters)):
        character = characters[character_index]
        if character == prev_character:
            has_adjacent_duplicate = True
        if int(character) < int(prev_character):
            return False
        prev_character = character
    return has_adjacent_duplicate

assert(is_solution(111111) == True)
assert(is_solution(223450) == False)
assert(is_solution(123789) == False)

def solve(min, max):
    solutions = 0
    for i in range(min, max):
        if is_solution(i):
            solutions += 1
    return solutions

print(solve(input_min, input_max))

'''
--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?
'''

def is_solution_part_two(val):
    # characters = list(str(val))
    # print(characters[0:2])
    # num_duplicates = 0
    # for character_index in range(1, len(characters) + 1):
    #     so_far = ''.join(characters[0:character_index])
    #     print(so_far)
    #     print(is_solution(so_far))
    #     # if(is_solution(characters[0:character_index]) and is_solution(characters[0:character_index - 1])):
    #     #     num_duplicates -= 1
    #     # elif(is_solution(characters[0:character_index])):
    #     #     num_duplicates += 1
    # return num_duplicates > 0
    characters = list(str(val))
    prev_character = '-1'
    has_adjacent_duplicate = False
    num_same = 0
    for character_index in range(0, len(characters)):
        character = characters[character_index]
        if character == prev_character:
            num_same += 1
        if character != prev_character and num_same == 1:
            has_adjacent_duplicate = True
        if character != prev_character:
            num_same = 0
        if int(character) < int(prev_character):
            return False
        prev_character = character
    if num_same == 1:
        has_adjacent_duplicate = True
    return has_adjacent_duplicate

assert(is_solution_part_two(112233) == True)
assert(is_solution_part_two(123444) == False)
assert(is_solution_part_two(111122) == True)

def solve_part_two(min, max):
    solutions = 0
    for i in range(min, max):
        if is_solution_part_two(i):
            solutions += 1
    return solutions

print(solve_part_two(input_min, input_max))
