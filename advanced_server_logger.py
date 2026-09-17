def generate_report(server_name, ping, status):
    print("Server", server_name, ping, sep=": ", end=" -> ")
    print(status)
generate_report("Proxy_1", 45, "ONLINE")
