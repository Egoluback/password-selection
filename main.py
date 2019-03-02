import random
import sys

res = ''
values = []

def genNumFromLen(len):
    res = '1'
    for i in range(0,len):
        res += '0'
    return int(res) - 1

try:
    length = int(input('Enter message length.'))
    isRand = str(input('Generate message with bot?(Y/N)'))
    if (isRand == 'n' or isRand == 'N'):
        userValue = int(input('Enter message.'))
    elif (isRand == 'y' or isRand == 'Y'):
        userValue = random.randint(0,genNumFromLen(length))
        while len(str(userValue)) < length:
            userValue = random.randint(0,genNumFromLen(length))
        print('Generated ', userValue)
except:
    print('Syntax error, invalid data.')
    input('Press Enter to exit.')
    quit()

if (len(str(userValue)) != length):
    print('Compilation error, length must be equal ', length)
    input('Press Enter to exit.')
else:
    print('Selection started.')
    print('Loading...')

    while res != str(userValue):
        nowRes = ''
        for i in range(0,length):
            val = str(random.randint(0,9))
            val = str(random.randint(0,9))
            nowRes += val
        res = nowRes
        if res in values:
            continue
        values.append(res)

    print('Selection finished.')
    print('Show matched values?(Y/N)')

    ans = str(input())

    if (ans == 'Y' or ans == 'y'):
        print(values)
        print('There are ', len(values),' values.')
    elif (ans == 'N' or ans == 'n'):
        quit()
    else:
        print('Syntax error, invalid data.')
        input('Press Enter to exit.')
        quit()

    input()