base=int(input('enter base'))
power=int(input('enter power'))
helper=1
for i in range (1,power+1):
    helper=helper*base
print(helper)