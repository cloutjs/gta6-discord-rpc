from pypresence import Presence
import time
rpc = Presence("856169082516406273")
rpc.connect()
print("Rich Presence running on localhost")
rpc.update(details="V0.8.1.22",large_image='kms',start=time.time())
while True:  
    time.sleep(15) 
