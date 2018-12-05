# -*- coding: utf-8 -*-

# load input file
with open("input.txt") as file:
    input = list(file.read())

def reactPoli(combi):
    if len(combi) > 1:
        if combi[0].lower() == combi[1].lower():
            if any(letter.isupper() for letter in combi) and any(letter.islower() for letter in combi):
                return True
    return False


# first star (slow)
def firstStar(input):

    currentInput = []
    markedForDeletion = []

    while True:
        found = False
        for i in range(len(input)):
            combi = input[i:i+2]
            # print(combi)
            if reactPoli(combi):
                markedForDeletion.extend([i, i+1])
                input = [i for j, i in enumerate(
                    input) if j not in markedForDeletion]
                markedForDeletion = []
                found = True
                break
        if not found:
            print('final')
            break

        print(len(input))

# firstStar(input)

# second star
alpha = 'abcdefghijklmnopqrstuvwxyz'

M = {}

for c in alpha:
     M[c.lower()] = c.upper()
     M[c.upper()] = c.lower()

answer = 9999999999999
for letter in alpha:
     s2 = [c for c in input if c != letter.lower() and c != letter.upper()]
     stack = []
     for c in s2:
         if stack and c == M[stack[-1]]:
             stack.pop()
         else:
             stack.append(c)
     answer = min(answer, len(stack))
print(answer)
