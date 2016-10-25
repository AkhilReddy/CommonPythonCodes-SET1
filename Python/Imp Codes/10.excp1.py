def getSubjectStats(subject, weights):
    return [[elt[0], elt[1], avg(elt[1], weights)] for elt in subject]

def dotProduct(a,b):
    result = 0.0
    for i in range(len(a)):
        result += a[i]*b[i]
    return result

def avg(grades, weights):
    return dotProduct(grades, weights)/len(grades)

test = [[['fred', 'flintstone'], [10.0, 5.0, 85.0]],
        [['barney', 'rubble'], [10.0, 8.0, 74.0]],
        [['wilma', 'flintstone'], [8.0, 10.0, 96.0]]]
weights = [.3, .2, .5]
