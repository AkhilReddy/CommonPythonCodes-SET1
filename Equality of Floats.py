#Comparing Equality of two floats:

x = float(raw_input('Pls give float 1:'))
y = float(raw_input('Pls give float 2:'))

if abs(x-y) < 0.01:
    print('Two floats are Equal')

else:
    print('Two floats are not Equal')

