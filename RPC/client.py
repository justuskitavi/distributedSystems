import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:6001/")

print("=== Temperature Conversion Program (RPC) ===")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice: "))

if choice == 1:
    print(f"\nYou selected: Celsius to Fahrenheit")
elif choice == 2:
    print(f"\nYou selected: Fahrenheit to Celsius")
else:
    print("Invalid choice")
    exit()



# RPC call
if choice == 1:
    value = float(input("Enter the temperature value: "))
    print(f"\nInput temperature: {value}")
    result = proxy.c_to_f(value)
    print(f"\nResult in Fahrenheit: {result:.2f}")
else:
    value = float(input("Enter the Fahrenheit value: "))
    print(f"\nInput Fahrenheit: {value}")
    result = proxy.f_to_c(value)
    print(f"\nResult in Celsius: {result:.2f}")
