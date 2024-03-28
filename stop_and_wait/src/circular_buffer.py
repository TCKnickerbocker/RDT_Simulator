class circular_buffer:
    # Init buffer, vars
    def __init__(self,n):
        self.read=0
        self.write=0
        self.max= n
        self.count=0
        self.buffer=[]
        for i in range(n):
            self.buffer.append(None)

    # Pushes packet to buffer
    def push(self,pkt):
        if(self.count==max):
            return -1
        else:
            self.buffer[self.write]=pkt

        self.write=(self.write+1)% self.max
        self.count=self.count+1

    # Removes a packet from buffer, if present. if !present, ret -1
    def pop(self):
        if(self.count==0):
            return -1

        temp=self.buffer[self.read]
        self.read=(self.read+1)%self.max
        self.count=self.count-1

    # Reads all packets in buffer
    def read_all(self):
        temp=[]
        read=self.read
        for i in range(self.count):
            temp.append(self.buffer[read])
            read=(read+1)%self.max
        return temp

    # Simple check to see if buffer is full
    def isfull(self):
        if(self.count==self.max):
            return True
        else:
            return False
