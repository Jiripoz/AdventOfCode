# First Question
# After the rearrangement procedure completes, what crate ends up on top of each stack?

crates = open('input_day5.txt', 'r').readlines()

matrix = [[y+x*8 for y in range(0,9)] for x in range(0,8)]

Colunas ={
    0:[],
    1:[],
    2:[],
    3:[],
    4:[],
    5:[],
    6:[],
    7:[],
    8:[],
}

for i in range(0,8):
    for j in range(0,33,4):
        aux=crates[i][j:(j+4)]
        aux=aux.replace('[','').replace(']','').replace('\n','').strip()
        if aux!='': Colunas[int(j/4)].append(aux)

# def grabtop(qtdd, origem, destino, Columns):
#     pack = Columns[origem][:qtdd]
#     Columns[origem] = Columns[origem][qtdd:]
#     for p in pack:
#         Columns[destino].insert(0, p)

# def first_question(Columns):
#     for l in range(10, len(crates)):
#         aus=crates[l].split()
#         clean=[int(x) for x in aus if x.isdigit()]
#         grabtop(clean[0], clean[1]-1, clean[2]-1, Columns)

#     answer = ''
#     for i in range(0,9):
#         answer=answer+Columns[i][0]

#     return answer

# Second Question
# After the rearrangement procedure completes, what crate ends up on top of each stack?

def new_grabtop(qtdd, origem, destino, Columns):
    pack = Columns[origem][:qtdd]
    Columns[origem] = Columns[origem][qtdd:]
    while pack:
        Columns[destino].insert(0, pack[-1])
        pack.pop()

def second_question(Columns):
    for l in range(10, len(crates)):
        aus=crates[l].split()
        clean=[int(x) for x in aus if x.isdigit()]
        new_grabtop(clean[0], clean[1]-1, clean[2]-1, Columns)

    answer = ''
    for i in range(0,9):
        answer=answer+Columns[i][0]

    return answer

# print(Colunas)
# new_grabtop(2, 2, 3)
# print(Colunas)
print(Colunas)
# print(first_question(Colunas))
print(Colunas)
print(second_question(Colunas))

