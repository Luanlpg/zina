from core import is_bouncy

def is_99_percent(num):
    bouncy = 0
    for i in range(num):
        if is_bouncy(i):
            bouncy += 1
    percent = 100 - ((num - bouncy) / bouncy * 100)
    if percent >= 99:
        print('passou')
        return True, percent
    return False, percent

init = 21780
interval = 1000000
result = 0
for i in range(7):
    for i in range(init, 9999999999, interval):
        bool, percent = is_99_percent(i)
        if bool == True:
            print(percent, i)
            result = i
            print('break')
            break
        print(percent, i)
    init = result - interval
    interval = int(interval/10)

print('==============================================')
print(f'================={result}======================')
print('==============================================')
