class ResultFromBill:
    def __init__(self, bill_id: int,
                 title_name: str,
                 supporter_count: int,
                 opposer_count: int,
                 primary_sponsor: str = "Unknown"):
        self.bill_id = bill_id
        self.title_name = title_name
        self.supporter_count = supporter_count
        self.opposer_count = opposer_count
        self.primary_sponsor = primary_sponsor

    def __repr__(self):
        return f"ResultFromBill({self.bill_id!r}, {self.title_name!r}, {self.supporter_count!r}, {self.opposer_count!r}, {self.primary_sponsor!r})"
