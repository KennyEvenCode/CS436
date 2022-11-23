# DO NOT IMPORT ANY OTHER PACKAGES THAT ARE NOT IN THE STANDARD LIBRARY
import random
from typing import Tuple

# CONSTANT USED INSIDE THE UPCOMING NAT PROJECT
# USE THIS <<<<<<<<<<<<<<<<<<
PUBLIC_IP = "172.16.20.2"

# This Class will support both ICMP and TCP packets
## icmp_mapping = NATTable()
## tcp_mapping = NATTable()
## and expose only set(x,y) and get(x,y) functions
class NATTable:
    def __init__(self):
        # NAT translation table
        # ============================ WORK WHERE =====================================
        # IMPLEMENT THIS
        # {} symbol to initialize dictionary of tuples
        self.data = {Tuple[str, int] : Tuple[str, int]}

    def _random_id(self):
        return random.randint(30001, 65535)

    def set(self, ip_src, id_src) -> Tuple[str, int]:
        # REMEMBER: Create a new random port for each NEW connection else return saved data if source ip and id is found
        # Set WAN side mapping PUBLIC_IP, random_id [range 30,000 - 65,535]
        # ============================ WORK WHERE =====================================
        new_ip_src = PUBLIC_IP
        new_id_src = _random_id()
        if ((ip_src, id_src) in self.data) {
            return ( new_ip_src , self.data[(ip_src, id_src)][1] )
        }
        else {
            # return unique/unused port
            # ERROR: infinite loop if all 35,535 ports get used up
            maxIt = 0
            while _isUsed(new_id_src):
                maxIt += 1
                new_id_src = self._random_id()
                if maxIT == 35534:
                    raise SystemExit(1)
            # save connection to table
            self.data.update( { ( ip_src , id_src ) : ( new_ip_src , new_id_src ) } )
            return ( new_ip_src , new_id_src ) 
        }

    def get(self, ip_dst, id_dst) -> Tuple[str, int]:
        # Get LAN side mapping ip_src and id_src
        # ============================ WORK WHERE =====================================
        ip_src = dict((value , key) for key , value in self.data.items()).get((ip_src, id_src))[0]
        id_src = dict((value , key) for key , value in self.data.items()).get((ip_src, id_src))[1]
        return ip_src, id_src

    def _isUsed (portNo: int) -> bool:
        # return true false if id_src is already in use        
        for ke , va in self.data.items():
            # va = ( IP , port )
            # va[1] = port
            if va[1] == portNo :
                return true                
        return false

            

        


































# DO NOT MODIFY TEST FUNCTION
def test_datastructure():
    datastructure = NATTable()

    used_ports = []

    computer1_ip = "10.0.0.1"
    computer1_port1 = 33450
    computer1_port2 = 39999

    computer2_ip = "10.0.0.50"
    computer2_port1 = 33450
    computer2_port2 = 34898

    computer3_ip = "10.0.0.120"
    computer3_port1 = 33450
    computer3_port2 = 35255
    computer3_port3 = 36878

    ip_src, port_src = datastructure.set(computer1_ip, computer1_port1)
    used_ports.append(port_src)
    assert ip_src == PUBLIC_IP

    ip_src, port_src = datastructure.get(ip_src, port_src)
    assert ip_src == computer1_ip
    assert port_src == computer1_port1
    
    ip_src, port_src = datastructure.set(computer2_ip, computer2_port1)
    assert ip_src == PUBLIC_IP
    assert port_src not in used_ports
    used_ports.append(port_src)

    ip_src, port_src = datastructure.set(computer2_ip, computer2_port1)
    assert ip_src == PUBLIC_IP
    assert port_src in used_ports

    ip_src, port_src = datastructure.get(ip_src, port_src)
    assert ip_src == computer2_ip
    assert port_src == computer2_port1

    ip_src, port_src = datastructure.set(computer3_ip, computer3_port1)
    assert ip_src == PUBLIC_IP
    assert port_src not in used_ports
    used_ports.append(port_src)

    ip_src, port_src = datastructure.set(computer2_ip, computer2_port2)
    assert ip_src == PUBLIC_IP
    assert port_src not in used_ports
    used_ports.append(port_src)

    for port in used_ports:
        assert port > 30000
    
    ip_src, port_src = datastructure.get(*datastructure.set(computer1_ip, computer1_port2))
    assert ip_src == computer1_ip
    assert port_src == computer1_port2

    ip_src, port_src = datastructure.get(*datastructure.set(computer1_ip, computer1_port2))
    assert ip_src == computer1_ip
    assert port_src == computer1_port2

    ip_src, port_src = datastructure.get(*datastructure.set(computer3_ip, computer3_port2))
    assert ip_src == computer3_ip
    assert port_src == computer3_port2

    ip_src, port_src = datastructure.get(*datastructure.set(computer3_ip, computer3_port3))
    assert ip_src == computer3_ip
    assert port_src == computer3_port3


# THIS IS A PROGRAM TO TEST YOUR IMPLEMENTED DATA STRUCTURE
# THIS PROGRAM MUST NOT CRASH OR SEND ANY ERRORS   
test_datastructure()
print("GOOD JOB :)")
print("Save your data structure for the upcoming NAT project")
