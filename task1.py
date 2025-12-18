import pulp

# Initialize the model
# We use LpMaximize because we want to maximize the total production
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Define decision variables
# x = Quantity of Lemonade to produce
# y = Quantity of Fruit Juice to produce
# Both must be >= 0 and should be integers (since we produce unit by unit)
x = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
y = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Objective Function
# We want to maximize the total number of products: Lemonade + Fruit Juice
model += x + y, "Total_Production"

# Define Constraints based on resources
# Water constraint: 2*Lemonade + 1*Fruit_Juice <= 100
model += 2 * x + 1 * y <= 100, "Water_Constraint"

# Sugar constraint: 1*Lemonade <= 50
model += 1 * x <= 50, "Sugar_Constraint"

# Lemon Juice constraint: 1*Lemonade <= 30
model += 1 * x <= 30, "Lemon_Juice_Constraint"

# Fruit Puree constraint: 2*Fruit_Juice <= 40
model += 2 * y <= 40, "Fruit_Puree_Constraint"

# Solve the problem
model.solve()

# Output the results
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lemonade to produce: {int(x.varValue)}")
print(f"Fruit Juice to produce: {int(y.varValue)}")
print(f"Total products: {int(pulp.value(model.objective))}")