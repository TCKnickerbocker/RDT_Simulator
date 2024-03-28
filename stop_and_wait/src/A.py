'''
A.py for stop_and_wait by Thomas Knickerbocker (Mar. 2023)
Implementation of a server at layer 4 capable of sending data to a requesting client 
via stop_and_wait for RDT3.0
'''

from src.simulator import sim
from src.simulator import to_layer_three
from src.event_list import evl
from src.packet import *

class A:
    def __init__(self):
        self.seqNo = 0
        self.prevPkt = None # most recent packet sent, used for retransmission
        self.state = "WAIT_LAYER5" # Becomes WAIT_ACK when packet is en-route to B/back
        self.estimated_rtt = 30

    def A_output(self, m):
        # If ready to send again
        if self.state == "WAIT_LAYER5":
            # Create packet, initialze checksum, set lastPacket
            pkt = packet(seqnum=self.seqNo, payload=m)
            pkt.checksum = pkt.get_checksum()
            self.prevPkt = pkt
            # Send to layer3, start timer, update state to be waiting for an ack
            to_layer_three("A", pkt) 
            evl.start_timer("A", self.estimated_rtt)
            self.state = "WAIT_ACK"

    def A_input(self, pkt):
        # Verify checksunm, ackNo
        if pkt.checksum == pkt.get_checksum():
            if pkt.acknum == self.seqNo:
                # Succcess. Remove timer, set state accordingly, inc seqNo
                evl.remove_timer()
                self.state = "WAIT_LAYER5"
                self.seqNo += 1
            elif pkt.acknum < self.seqNo: # old packet, ignore
                return
            else: 
                # unsuccessful, send last packet back to layer3, reset timer
                to_layer_three("A", self.prevPkt)
                evl.start_timer("A", self.estimated_rtt)

    def A_handle_timer(self):
        # packet not delivered. Resend, reset timer
        to_layer_three("A", self.prevPkt)
        evl.start_timer("A", self.estimated_rtt)

a = A()

