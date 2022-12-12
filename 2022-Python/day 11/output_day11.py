# First Question
# What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?
monkeys = open('input_day11.txt', 'r').readlines()

monkey_dict={}
monkey_dict2={}

class Monkey:
    def __init__(self, number, items, operation, test, true, false) -> None:
        self.number = [v for v in number.replace(':', '').split() if v.isnumeric()][0]
        self.items = [int(w) for w in items.replace('Starting items: ', '').split(',')]
        self.operation = operation.replace('Operation: new = ', '').strip()
        self.test = [int(x) for x in test.split() if x.isnumeric()][0]
        self.true = [int(y) for y in true.split() if y.isnumeric()][0]
        self.false = [int(z) for z in false.split() if z.isnumeric()][0]
        self.inspect=0
        pass

for i in range(0, len(monkeys), 7):
    monkey = Monkey(monkeys[i], monkeys[i+1], monkeys[i+2], monkeys[i+3], monkeys[i+4], monkeys[i+5]) 
    mkey = {monkey.number:monkey}  
    monkey_dict.update(mkey)

for i in range(0, len(monkeys), 7):
    monkey = Monkey(monkeys[i], monkeys[i+1], monkeys[i+2], monkeys[i+3], monkeys[i+4], monkeys[i+5]) 
    mkey = {monkey.number:monkey}  
    monkey_dict2.update(mkey)

for i in range(0,20):
    for key in monkey_dict:
        items=monkey_dict[key].items
        for item in items:
            monkey_dict[key].inspect+=1
            old=item
            new=eval(monkey_dict[key].operation)
            new = int(new/3)
            if new%monkey_dict[key].test==0:
                monkey_dict[str(monkey_dict[key].true)].items.append(new)
            else:   monkey_dict[str(monkey_dict[key].false)].items.append(new)
            monkey_dict[key].items=[]

mb=[]
for key in monkey_dict:
    mb.append(int(monkey_dict[key].inspect))
    print('monkey %s inspected items %s times'% (key, monkey_dict[key].inspect))


mb.sort(reverse=True)
print('monkey business is: ', mb[0]*mb[1])

# Second Question
# what is the level of monkey business after 10000 rounds?

limanel=1
for key in monkey_dict2:
    limanel=limanel*monkey_dict2[key].test
print(limanel)

for i in range(0,10000):
    for key in monkey_dict2:
        items=monkey_dict2[key].items
        for item in items:
            monkey_dict2[key].inspect+=1
            old=item
            new=eval(monkey_dict2[key].operation)
            if new>limanel:
                new=new%limanel
            if new%monkey_dict2[key].test==0:
                monkey_dict2[str(monkey_dict2[key].true)].items.append(new)
            else:   monkey_dict2[str(monkey_dict2[key].false)].items.append(new)
            monkey_dict2[key].items=[]

mb2=[]
for key in monkey_dict2:
    mb2.append(int(monkey_dict2[key].inspect))
    print('parte 2: monkey %s inspected items %s times'% (key, monkey_dict2[key].inspect))


mb2.sort(reverse=True)
print('monkey business 2 is: ', mb2[0]*mb2[1])
