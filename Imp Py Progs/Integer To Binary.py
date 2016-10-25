def IntegerToBinary(input):
    out = list()
    for a in input:
        div = a
        i=0
        sol = 0
        while div != 0:
            ten = pow(10,i)
            sol = div%2*ten + sol
            div = div/2
            i += 1
        out.append(sol)
    return out

def PrintInput(input):
    return [ i for i in input]

if __name__ == '__main__':
    input = [23,100,34,2234,0]
    print "Input list in Integer Format: ",PrintInput(input)
    output = IntegerToBinary(input)
    print "Output list in Binary Format: ",output
    print "\n\n"
    
