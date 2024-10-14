weight = 5
cost_ground = 10

#Ground shipping
flat_charge = 20

if weight <= 2:
  cost_ground == 1.5 * weight + flat_charge
elif weight <= 6:
  cost_ground == 3.0 * weight + flat_charge
elif weight <= 10:
  cost_ground == 4.0 * weight + flat_charge
else:
  cost_ground == 4.75 * weight + flat_charge

print(cost_ground)