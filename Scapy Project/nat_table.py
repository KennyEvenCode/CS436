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

    # class constructor
    # creates data structures for storing data
    def __init__(self):
        # NAT translation table
        # ============================ WORK WHERE =====================================
        # IMPLEMENT THIS
        # creates an empty list to store registered port num and LAN IP
        self.data = [] 
        # creates a list to store port num and LAN IP (initialized with 0-63)
        self.lanList = list(range(64)) 
        # creates a list to store port num and WAN IP (initialized with 0-63)
        self.wanList = list(range(64)) 

    # generate random number within valid port range (between 30000, 65535, all availbe if greater than 30000)
    def _random_id(self):
        return random.randint(30001, 65535)

    # set function 
    # Creates a new random port for each NEW connection 
    # otherwise, returns saved data if source ip and port numbers are found
    def set(self, ip_src, id_src) -> Tuple[str, int]:
        
        # set ip equal to public ip
        new_ip_src = PUBLIC_IP

        # get new random port
        new_id_src = self._random_id()
        
        # get LAN from WAN port num
        lanPort = new_id_src % 64 

        # get WAN from LAN port num 
        wanPort = id_src % 64 

        # if IP and Port numbers are already mapped 
        if (ip_src, id_src) in self.data: 
            # get value from the WAN List
            wanValue = self.wanList[wanPort] 
            # seperate tuple into individual variables/objects
            ip_src = wanValue[0]
            id_src = wanValue[1]
            
            # returns port num and WAN IP
            return ip_src, id_src 

        else: 
            # create new connection and add info to lists
            self.lanList[lanPort] = (ip_src, id_src)
            self.wanList[wanPort] = (new_ip_src, new_id_src)
            # add to table
            self.data.append((ip_src, id_src))
            #return new ip and port numbers
            return new_ip_src, new_id_src

    # get function 
    # retrieves the LAN side mapping ip_src and id_src
    def get(self, ip_dst, id_dst) -> Tuple[str, int]:

        #set source ip equal to destination ip
        ip_src = ip_dst 
        # set source port equal to destination port
        id_src = id_dst 
        
        # hash lanPort
        lanPort = id_src % 64
        # get value (tuple) from Lan List
        lanValue = self.lanList[lanPort]
        
        # seperate tuple into individual variables/objects
        ip_src = lanValue[0]
        id_src = lanValue[1]
        
        # ISSUE: not needed
        self.data

        # return the corresponding ip and port numbers
        return ip_src, id_src


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