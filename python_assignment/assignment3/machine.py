import math

cost_of_machine = 6000
annual_earning = 1000
salvage_value = 2000
rate_of_return = 0.12

def npv_machine(n):
    pv_earnings = sum(annual_earning / (1 + rate_of_return) ** t for t in range(1, n+1))
    pv_salvage = salvage_value / (1 + rate_of_return) ** n
    return -cost_of_machine + pv_earnings + pv_salvage

n = 1
while npv_machine(n) < 0:
    n += 1

print(f"The minimum life of the machine for it to be more attractive compared to alternative investment is {n} years.")
