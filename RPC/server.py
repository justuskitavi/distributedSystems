from xmlrpc.server import SimpleXMLRPCServer

#Defining the simple functions that will be performed
def add(a, b):
    return a+b

def subtract(a,b):
    return a-b
    
def multiply(a,b):
    return a*b
    
def divide(a,b):
    if b == 0:
        return "Error: Division by zero."
    return a/b
    

def startServer():
    server = SimpleXMLRPCServer(("127.0.0.1", 8000))
    print("RPC server started on port 8000")

    #Register the functions
    server.register_function(add, "add")
    server.register_function(subtract, "subtract")
    server.register_function(multiply, "multiply")
    server.register_function(divide, "divide")

    server.serve_forever()

if __name__ == "__main__":
    startServer()