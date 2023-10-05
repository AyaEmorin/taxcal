def cal_tax(income):
    if income >= 30000.00:
        taxtotal = income - (income*0.05)
    else :
        taxtotal = income - (income*0.00)
    return  taxtotal

def total(income,com):
    finaltotal = income + com
    return finaltotal





    
