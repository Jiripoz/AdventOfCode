# First Question
# What would your total score be if everything goes exactly according to your strategy guide?

strategy_guide = open('input_day2.txt', 'r').readlines()

# A for Rock, B for Paper, C for Scissors
# X for Rock, Y for Paper, Z for Scissors

map_1 = {
    tuple(['A', 'X']):4, #EMPATE
    tuple(['A', 'Y']):8, #VITÓRIA
    tuple(['A', 'Z']):3, #DERROTA
    tuple(['B', 'X']):1, #DERROTA
    tuple(['B', 'Y']):5, #EMPATE
    tuple(['B', 'Z']):9, #VITÓRIA
    tuple(['C', 'X']):7, #VITÓRIA
    tuple(['C', 'Y']):2, #DERROTA
    tuple(['C', 'Z']):6  #EMPATE
}

result=0
for line in strategy_guide:
    result = result + map_1[tuple(line.split())]

print('following the first rule, the final score is: ', result)

# Second Question
# Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

# A for Rock, B for Paper, C for Scissors
# X for Lose, Y for Draw, Z for Win

map_2 = {
    tuple(['A', 'X']):3, #Derrota
    tuple(['A', 'Y']):4, #Empate
    tuple(['A', 'Z']):8, #Vitória
    tuple(['B', 'X']):1, #Derrota
    tuple(['B', 'Y']):5, #Empate
    tuple(['B', 'Z']):9, #Vitória
    tuple(['C', 'X']):2, #Derrota
    tuple(['C', 'Y']):6, #Empate
    tuple(['C', 'Z']):7  #Vitória
}

result2=0
for line in strategy_guide:
    result2 = result2 + map_2[tuple(line.split())]

print('following the second rule, the final score is: ', result2)