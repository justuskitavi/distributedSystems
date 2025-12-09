from xmlrpc.server import SimpleXMLRPCServer

# Function to change celcius to farenheit
def c_to_f(c):
    return (c * 9/5) + 32

# Function to change farenheit to celcius

def f_to_c(f):
    return (f - 32) * 5/9

server = SimpleXMLRPCServer(("127.0.0.1", 6001))
print("RPC Server running on 127.0.0.1:6001...")

server.register_function(c_to_f, "c_to_f")
server.register_function(f_to_c, "f_to_c")

server.serve_forever()
