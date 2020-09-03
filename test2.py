num = int(raw_input('enter a number'))
sum = 0
for i in range(1,num):
    if i % 3 == 0:
        print(i)
        sum += i
    elif i % 5 == 0:
        print(i)
        sum += i
print(sum)
