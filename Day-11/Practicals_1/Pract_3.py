Server_Config = {
    'Server1':{'IP': '192.168.1.1', 'port': '8080', 'status': 'active'},
    'Server2':{'IP': '192.168.1.2', 'port': '8000', 'status': 'inactive'},
    'Server3':{'IP': '192.168.1.3', 'port': '9000', 'status': 'active' }
}

def get_server_status(server_name):
    return(Server_Config.get(server_name , {}).get('status', 'Server Not Found'))

server_name = 'Server1'
Status = get_server_status(server_name)
print(f"{server_name} : Status {Status}")