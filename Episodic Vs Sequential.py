environment = input("Enter environment (Episodic/Sequential): ")
if environment == "Episodic":
    print("Each action is independent.")
    print("Example: Image classification")
elif environment == "Sequential":
    print("Current action affects future actions.")
    print("Example: Chess")
else:
    print("Invalid environment")