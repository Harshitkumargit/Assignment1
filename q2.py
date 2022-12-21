incm=int(input("enter income "))
tax_rt=20/100
if(incm>10000):
    d=int(input("number of dependants "))
    taxable_incm=incm-(d*3000)-10000
    tax=taxable_incm*tax_rt
    print("taxable income = ",taxable_incm)
    print("tax rate = ",tax_rt)
    print("Tax = ",tax)
else:
    print("no tax.!")
