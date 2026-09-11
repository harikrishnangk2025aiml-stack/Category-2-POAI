environment = input("Enter environment (Discrete/Continuous): ")
if environment == "Discrete":
    print("Environment has separate states and actions.")
    print("Example: Chess")
elif environment == "Continuous":
    print("Environment has continuously changing values.")
    print("Example: Self-driving car")
else:
    print("Invalid environment")