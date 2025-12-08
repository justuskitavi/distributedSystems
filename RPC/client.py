import xmlrpc.client
def startClient():
    proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:8000/")
    print("Connected to the RPC server\n")
    while True:
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Show operation menu
        print("\nSelect operation:")
        print("\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exit\n")
        

        choice =int (input("Enter choice (1-5): ")
)
        if choice == 1:
            result = proxy.add(a, b)
        elif choice == 2:
            result = proxy.subtract(a, b)
        elif choice == 3:
            result = proxy.multiply(a, b)
        elif choice == 4:
            if b == 0:
                print("Cannot divide by zero")
            result = proxy.divide(a, b)
        elif choice == 5:
            print("Exiting client.")
            break
        else:
            print("Invalid choice. Please select 1-5.")
            continue

        print(f"Result: {result}\n")


if __name__ == "__main__":
    startClient()