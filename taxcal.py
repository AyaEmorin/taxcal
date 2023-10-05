from taxcal.func import cal_tax
from taxcal.func import total 


income = float(input("input Your total income: "))
comm = float(input("input your total commision: "))

tax = cal_tax(income)
allcomm = total(tax, comm)

print(f"salary after tax : {allcomm} Bath")