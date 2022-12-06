# First Question
# In how many assignment pairs does one range fully contain the other?

cleaning = open('input_day4.txt', 'r').readlines()

cont=0
cont2=0

def elfminmax(line):
    aus = line.split(',')

    elf1 = aus[0]
    elf1min = int(elf1.split('-')[0])
    elf1max = int(elf1.split('-')[1])   

    elf2 = aus[1]
    elf2min = int(elf2.split('-')[0])
    elf2max = int(elf2.split('-')[1])

    return elf1min, elf1max, elf2min, elf2max

def question_1(elf1min, elf1max, elf2min, elf2max):

    if elf1min >= elf2min:
        if elf1max <= elf2max:
            return True

    if elf2min >= elf1min:
        if elf2max <= elf1max:
            return True

    return False

# # Second Question
# # In how many assignment pairs do the ranges overlap?

def question_2(elf1min, elf1max, elf2min, elf2max):

    if elf2max>=elf1min:
        if elf2min<=elf1max: return True
    
    if elf1max>=elf2min:
        if elf1min<=elf2max:    return True
    
    return False

for line in cleaning:
    temp = elfminmax(line)
    if question_1(temp[0], temp[1], temp[2], temp[3]): cont+=1
    if question_2(temp[0], temp[1], temp[2], temp[3]): cont2+=1

print('resposta 1: ', cont)
print('resposta 2: ', cont2)