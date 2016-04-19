def tax_deduction(salary, num_dep):
    if salary < 18000:
        return 10000 - salary
    elif salary <= 25000 and num_dep:
        return 20000 - salary
    else:
        return 10000




















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
