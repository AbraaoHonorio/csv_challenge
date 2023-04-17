class Votes:
    def __init__(self, id:int, bill_id:int):
        self.id = int(id)
        self.bill_id =int(bill_id)

    def __repr__(self):
        return f"Votes({self.id!r}, {self.bill_id!r}, "