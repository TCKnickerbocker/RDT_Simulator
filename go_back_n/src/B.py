'''
B.py for go_back_n by Thomas Knickerbocker (Mar. 2023)
Implementation of a client in layer 4 with RDT3.0 via go_back_n protocol
'''

from src.simulator import to_layer_five
from src.packet import send_ack


class B:
    def __init__(self):
        self.expected_seq = 0

    def B_output(self, m):
        return

    def B_input(self, pkt):
        # Check seqnum, corruption
        if pkt.checksum == pkt.get_checksum() and pkt.seqnum == self.expected_seq: 
            to_layer_five("B", pkt.payload.data) # print, ack, increment seqNo
            send_ack("B", pkt.seqnum)
            self.expected_seq += 1
        else:
            send_ack("B", self.expected_seq - 1) # wrong seqNo or corrupted. nak
        return

    def B_handle_timer(self):
        return


b = B()