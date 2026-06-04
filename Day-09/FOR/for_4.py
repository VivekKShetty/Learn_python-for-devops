Servers = ("Server1", "Server2" , "Server3")

def configure_monitoring_agent(server):
    print("Configure monitoring agent on server", server)

for server in Servers:
    configure_monitoring_agent(server)


