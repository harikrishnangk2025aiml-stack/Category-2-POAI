environment = input("Enter environment (Fully/Partially): ")
if environment == "Fully":
    print("Agent can see the complete environment.")
    print("Action: Make decision directly")
elif environment == "Partially":
    print("Agent cannot see the complete environment.")
    print("Action: Use available information and memory")
else:
    print("Invalid environment")