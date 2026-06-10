Server_Config = {
    'Server1':{'IP': '192.168.1.1', 'port': '8080', 'status': 'active'},
    'Server2':{'IP': '192.168.1.2', 'port': '8000', 'status': 'inactive'},
    'Server3':{'IP': '192.168.1.3', 'port': '9000', 'status': 'active' }
}

def get_server_status(server_name):
    print(Server_Config['Server1']['status'])
    return(Server_Config['Server1']['status'])

get_server_status(Server_Config)