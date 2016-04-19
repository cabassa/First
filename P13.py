def max_number(l):
    max_value = l[0]
    for n in l:
        if n > max_value:
            max_value = n
    return max_value

l = [0,-2,100,200,4]
print "max:", max_number(l)


