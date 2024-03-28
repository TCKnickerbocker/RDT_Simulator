'''
A.py for go_back_n by Thomas Knickerbocker (Mar. 2023)
Implementation of a server at layer 4 capable of sending data to a requesting client 
via go_back_n for RDT3.0
'''

from src.simulator import sim
from src.simulator import to_layer_three
from src.event_list import evl
from src.packet import *
from src.circular_buffer import circular_buffer

class A:
    def __init__(self):
        self.buf = circular_buffer(50) # window size should be 8
        self.windowSize = 8
        self.estimated_rtt = 30
        self.seqNo = 0
        self.unackSeqNo = 0
    
    def A_output(self, m): # send packet
        # print(f"Sending {self.seqNo}")
        if self.buf.isfull():
            print("A's buffer is full, dropping packet")
            return
        # Create packet, send to layer3, add to buf, inc seqNo, startTimer if DNE
        pkt = packet(seqnum=self.seqNo, acknum=self.seqNo, payload=m)
        pkt.checksum = pkt.get_checksum()
        to_layer_three("A", pkt)
        self.buf.push(pkt)
        self.seqNo+=1
        
        if evl.head == None and evl.head.eventity != "A": # if existing timer
            return
        evl.start_timer("A", self.estimated_rtt)

    def A_input(self, pkt): # recv ack/nack
        # Check if flipped, undesired acknum
        if pkt.get_checksum() != pkt.checksum or pkt.acknum < self.unackSeqNo:
            return
        # Update buf, seqNo
        ackDiff = pkt.acknum - self.unackSeqNo
        if ackDiff >= 0:
            for i in range(0, ackDiff+1):
                self.unackSeqNo+=1
                self.buf.pop()

        if self.buf.count > 0: # Set new timer if buffer nonempty
            if evl.head != None and evl.head.eventity == "A":
                return
            evl.start_timer("A", self.estimated_rtt)

    def A_handle_timer(self):
        pkts = self.buf.read_all()
        for i in range(min(self.buf.count, 8)): # timer expired, retransmit all in window
            to_layer_three("A", pkts[i])
        if self.buf.count>0: # Set new timer
            if evl.head != None and evl.head.eventity == "A":
                return
            evl.start_timer("A", self.estimated_rtt)

a = A()