def resultQuadratic():
    inputData = ("a", "b", "c")
    factors = []
    for i in inputData:
        print("Give "+i)
        factors.append(float(input()))
    delta = pow(factors[1],2)- (4 * factors[0]*factors[2])
    if delta < 0:
        print ("No solution")
        return
    elif delta == 0:
        x = -(factors[1]/(2*factors[0]))
        print("Solution:", x)
        return
    else:
        x1 = ((-factors[1])+pow(delta, 1/2)) / (2*factors[0])
        x2 = ((-factors[1])-pow(delta, 1/2)) / (2*factors[0])
        print("First solution:", x1)
        print("Second solution:", x2)
        return
if __name__ == '__main__':
    resultQuadratic()