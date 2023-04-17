from domain.legislator import Legislator


class ResultFromLegislator:
    def __init__(self, legislator: Legislator, count_yes: int, count_no: int):
        self.legislator = legislator
        self.count_yes = count_yes
        self.count_no = count_no

    def increment_yes(self):
        self.count_yes += 1

    def increment_no(self):
        self.count_no += 1

    def __repr__(self):
        return f"ResultFromLegislator({self.legislator.id!r}, {self.legislator.name!r}, {self.count_yes!r}, {self.count_no!r})"
