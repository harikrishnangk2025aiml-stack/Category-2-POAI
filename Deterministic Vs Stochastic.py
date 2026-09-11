environment = input("Enter environment (Deterministic/Stochastic): ")
if environment == "Deterministic":
    print("Result of the action is predictable.")
    print("Example: Chess")
elif environment == "Stochastic":
    print("Result of the action is uncertain.")
    print("Example: Self-driving car")
else:
    print("Invalid environment")