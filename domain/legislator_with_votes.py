from typing import List

from csv_challenge.domain.legislator import Legislator


class LegislatorWithVotes:
    def __init__(self, legislator: Legislator, count_yes: int, count_no: int):
        self.legislator = legislator
        self.count_yes = count_yes
        self.count_no = count_no

    def increment_yes(self):
        self.count_yes += 1

    def increment_no(self):
        self.count_no += 1

    def increment_votes(self, is_yes: bool):
        if is_yes:
            self.increment_yes()
            return

        self.increment_no()

    def __repr__(self):
        return f"ResultFromLegislator({self.legislator.id!r}, {self.legislator.name!r}, {self.count_yes!r}, {self.count_no!r})"

    def __iter__(self):
        return iter([self.legislator.id, self.legislator.name, self.count_yes, self.count_no])
    @staticmethod
    def header() -> List[str]:
        return ["id", "name", "num_supported_bills", "num_opposed_bills"]