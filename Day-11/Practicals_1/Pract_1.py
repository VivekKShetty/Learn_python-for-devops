Server_Config = {
    'Server1':{'IP': '192.168.1.1', 'port': '8080', 'status': 'active'},
    'Server2':{'IP': '192.168.1.2', 'port': '8000', 'status': 'inactive'},
    'Server3':{'IP': '192.168.1.3', 'port': '9000', 'status': 'active' }
}

print(Server_Config['Server1'])
print(Server_Config['Server1']['status'])

server_name = 'Server4'
print(Server_Config.get(server_name, {}).get('status', 'Server not found'))