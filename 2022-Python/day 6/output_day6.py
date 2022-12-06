# First Question
# How many characters need to be processed before the first start-of-packet marker is detected?

datastream = open('input_day6.txt', 'r').readlines()
        
def question_1(stream):
    marker = stream[:4]
    if len(marker)==len(set(marker)): return marker
    for i in range(4,len(stream)):
        marker=marker[1:]+stream[i]
        if len(marker)==len(set(marker)): return marker, i+1

    return 'not found'

# Second Question
# How many characters need to be processed before the first start-of-packet marker is detected?

def question_2(stream):
    marker = stream[:14]
    if len(marker)==len(set(marker)): return marker
    for i in range(14,len(stream)):
        marker=marker[1:]+stream[i]
        if len(marker)==len(set(marker)): return marker, i+1
    return 'not found'

print(question_1(datastream[0]))
print(question_2(datastream[0]))
