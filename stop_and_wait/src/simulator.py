from src.msg import *
from src.event_list import *
from src.event import *

import random
import copy


class simulator:
    def __init__(self):
        # Adjustable parameters for testing
        self.lossprob = 0.8  # Prob(losing a packet)
        self.corruptprob = 0.8  # Prob(bit in packet flips)
        self.Lambda = 100000  # Arrival rate of messages from layer 5
        self.nsimmax = 20  # numMessages to generate before stopping and waiting for events to complete
        self.TRACE = 0  # Debugging help


        self.nsim = 0  # Total numMessages from 5 to 4
        self.ntolayer3 = 0  # Total numMessages sent to layer3
        self.nlost = 0  # Total numMessages lost in transit
        self.ncorrupt = 0  # Total numMessages where a bit flip occurred (aka corruption)
        self.time = 0.0  # Inits time at 0 when sim starts

        self.envlist = evl # eventlist from event.py

        self.generate_next_arrival()  # Inserts the first event for the simulator to process

# Creates anotehr arrival from A with a TTL
    def generate_next_arrival(self):
        time = self.time + self.Lambda
        self.envlist.insert(event(time, "FROM_LAYER5", "A"))
        return

# Runs simulator
    def run(self):
        while (1):
            env = self.envlist.remove_head()
            if env == None:
                print("simulation end!")
                return
            else:
                self.time = env.evtime

            if self.nsim == self.nsimmax:
                print("simulation end")
                return

            if env.evtype == "FROM_LAYER5":
                self.generate_next_arrival()
                ch = chr(97 + self.nsim % 26)
                m = msg(ch)
                self.nsim = self.nsim + 1
                if env.eventity == "A":
                    from src.A import a
                    a.A_output(m)
                else:
                    from src.A import b
                    b.B_output(m)

            elif env.evtype == "FROM_LAYER3":
                pkt2give = env.pkt
                if env.eventity == "A":
                    from src.A import a
                    a.A_input(pkt2give)
                else:
                    from src.B import b
                    b.B_input(pkt2give)

            elif env.evtype == "TIMER_INTERRUPT":
                if env.eventity == "A":
                    a.A_handle_timer()
                else:
                    b.B_handle_timer()

            else:
                print("!!!!!!!????")

# Sends data to network layer
def to_layer_three(AorB, pkt):
    if random.uniform(0, 1) < sim.lossprob:
        return

    packet = copy.deepcopy(pkt)

    if random.uniform(0, 1) < sim.corruptprob:
        if packet.payload!=0:
            packet.payload.data = packet.payload.data[0:-1] + "*"
        else:
            packet.seqnum=-1

    q = sim.envlist.head
    lasttime = sim.time
    while q != None:
        if q.eventity == AorB and q.evtype == "FROM_LAYER3":
            lasttime = q.evtime

        q=q.next

    eventime = lasttime + 1 + 9 * random.uniform(0, 1)
    if AorB == "A":
        sim.envlist.insert(event(eventime, "FROM_LAYER3", "B", packet))
    else:
        sim.envlist.insert(event(eventime, "FROM_LAYER3", "A", packet))

# Received packet. Nice.
def to_layer_five(AorB, data):
    print("data recieved：{}".format(data))


sim = simulator()
