from src.event import event


class event_list:
    def __init__(self):
        self.head = None
    # Insert packet
    def insert(self, p):
        q = self.head
        if (q == None):  # if head is None
            self.head = p
            self.head.next = None
            self.head.prev = None
        else:
            qold = q
            while (q != None and p.evtime > q.evtime):
                qold = q
                q = q.next

            # now qold.next==q, p.evtime<=q.evtime
            if (q == None):
                qold.next = p
                p.prev = qold
                p.next = None

            else:
                if (q == self.head):
                    p.next = q
                    p.prev = None
                    q.prev = p
                    self.head = p
                else:
                    p.next = q
                    p.prev = q.prev
                    p.prev.next = p
                    q.prev = p

    # Displays events, timing
    def print_self(self):
        q = self.head
        print("--------------\nEvent List Follows:\n")
        while (q != None):
            print("Event time:{} , type: {} entity: {}\n".format(q.evtime, q.evtype, q.eventity))
            q = q.next

        print("--------------\n")

    # Removes head of event list
    def remove_head(self):
        temp = self.head
        if temp == None:
            return None
        if (self.head.next == None):
            self.head = None
            return temp
        else:
            self.head.next.prev = None
            self.head = self.head.next
            return temp

    # Begins a timer
    def start_timer(self, AorB, time):
        from src.simulator import sim
        self.insert(event(sim.time+time, "TIMER_INTERRUPT", AorB))

    # Ends timer
    def remove_timer(self):
        q = self.head
        while (q.evtype != "TIMER_INTERRUPT"):
            q = q.next

        if q.prev == None:
            self.head = q.next
        elif q.next == None:
            q.prev.next = None
        else:
            q.next.prev = q.prev
            q.prev.next = q.next

# Declare instance
evl = event_list()