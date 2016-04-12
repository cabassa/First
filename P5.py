def absolute(N):
    if N < 0:
        return -1 * N
    else:
        return N
print "|-1| = ", absolute(-1)
print "|100| = ", absolute(100)
print "|0| =", absolute(0)

################ EXAMPLE 1
x = 9
if x < 0:
    print 'Negative'
elif x == 0:
    print 'Zero'
else:
    print
    print "Resultado del codigo 1"
    print 'Positive'

############### EXAMPLE 2
x = 0
if x < 0:
    print 'Negative'
elif x == 0:
    print
    print 'Zero'
    print
else:
    print
    print 'Positive'

########## TAX EXAMPLE
def get_tax_amount(salary):
    if salary < 20000:
        return 0
    elif salary >= 20000 and salary < 50000:
        return 0.15 * salary
    elif salary >= 50000 and salary < 100000:
        return 0.20 * salary
    else:
        return 0.33 * salary

print "Bob Tax: ", get_tax_amount(30000)
print "Jil Tax: ", get_tax_amount(45000)
print "Apu Tax: ", get_tax_amount(130000)
print "Tom Tax: ", get_tax_amount(17000)


