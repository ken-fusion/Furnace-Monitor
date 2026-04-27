# Furnace Temperature Monitor & Procedural Version
print("--- SYSTEM START: Glass Furnace Monitoring ---")

while True:
    user_input = input("Furnace Temperature: ")

    if user_input == 'STOP'.lower():
        print("system shutting down")
        break
    
    try:
        temp = float(user_input)
        if temp <= 1200:
            print(f"Status: Too Low ({temp}) - Increase Heat! ")
        elif temp >= 1500:
            print(f"Status: Too Hot ({temp}) - Decrease Heat! ")
        else:
            print("Status: Stable - Don't Change Anything")

    except ValueError:
        print("WARNING! Temperature is not correct")
print("System Stopped")
