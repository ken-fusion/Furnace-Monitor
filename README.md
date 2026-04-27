# Furnace Temperature Monitor & Procedural Version
Python-based tool for tracking glass furnace temperature and preventing operational errors...

```
print("--- SYSTEM START: Glass Furnace Monitoring ---")

while True:
    user_input = input("Furnance Temprature: ")

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


    # Step 7: Except block (Agar user ghalat input de)
    except ValueError:
        print("WARNING! Temprature is not correct")
print("System Stopped")
                       ```
