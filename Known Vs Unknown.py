environment = input("Enter environment (Known/Unknown): ")
if environment == "Known":
    print("Agent knows the environment.")
    print("Action: Make decision using known information")
elif environment == "Unknown":
    print("Agent does not know the environment.")
    print("Action: Explore and learn from the environment")
else:
    print("Invalid environment")