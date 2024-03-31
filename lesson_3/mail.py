from Address import Address

class Mailing:
    def __init__(self,to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def print_toadr(self):
        print(self.to_address)
    
    def print_fromadr(self):
        print(self.from_address)

    def print_cost(self):
        print(self.cost)

    def print_track(self):
        print(self.track)