def MathExponent(a,b):
    if b==1: 
        return a
    else:
        return a * MathExponent(a,b-1)