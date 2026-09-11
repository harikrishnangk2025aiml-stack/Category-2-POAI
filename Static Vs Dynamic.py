environment = input("Enter environment (Static/Dynamic): ")
if environment == "Static":
    print("Environment does not change.")
    print("Action: Make decision normally")
elif environment == "Dynamic":
    print("Environment can change.")
    print("Action: Observe and react continuously")
else:
    print("Invalid environment")