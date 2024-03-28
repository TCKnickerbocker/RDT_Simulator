'''
B.py for stop_and_wait by Thomas Knickerbocker (Mar. 2023)
Implementation of a client in layer 4 with RDT3.0 via stop_and_wait protocol
'''

from src.simulator import to_layer_five
from src.packet import send_ack

class B:
    def __init__(self):
        self.expSeqNo = 0

    def output(self, m):
        return

    def B_input(self, pkt):
        # Check for corruption
        if pkt.checksum != pkt.get_checksum():
            return # drop corrupted packet

        if pkt.seqnum == self.expSeqNo: # ack case
            # Send to layer5, ack, increment expected sequence number
            to_layer_five("B", pkt.payload.data)
            send_ack("B", pkt.seqnum) # ack
            self.expSeqNo += 1
        else: # nack case
            send_ack("B", self.expSeqNo-1) 

    def B_handle_timer(self):
        return


b = B()

