class Votes:
    def __init__(self, id, bill_id):
        self.id = id
        self.bill_id = bill_id

    def __repr__(self):
        return f"Votes({self.id!r}, {self.bill_id!r}, "