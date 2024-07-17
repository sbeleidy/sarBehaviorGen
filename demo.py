from pyshop.pyshop import PyShop
from pyshop.pyshop import State

ps = PyShop("init")
ps.declare_methods("models/general.hddl")
ps.declare_operators("models/general.hddl")


print("\nOperators")
ps.print_operators()

print("\nMethods")
ps.print_methods()

# Initial State Definition
initial_state = State("initial")

# Scenario 1
# initial_state.add(["confusion", "early"])
# initial_state.add(["level", "l2"])

# Scenario 2
# initial_state.add(["time", "long"])
# initial_state.add(["level","l2"])
# initial_state.add(["game", "no-error"])

initial_tasks = [
    "confirm"
]

for task in initial_tasks:
    print("Task:", task, task in ps.methods.keys(), task in ps.operators)


print("Initial State")
print(initial_state)
print(initial_state.facts)

# Plan what to do based on the initial state and tasks
print("\nPlan")
initial_plan = ps.pyshop(initial_state, initial_tasks, 3)
print(initial_plan)

# print("Next State")
# print(initial_state)
# print(initial_state.facts)