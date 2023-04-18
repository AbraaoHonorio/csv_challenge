from typing import List


class Bill:
    def __init__(self, id: int, title: str, sponsor_id: int):
        self.id = int(id)
        self.title = title
        self.sponsor_id = int(sponsor_id)
        self.vote = None
        self.supporter_count = 0
        self.opposer_count = 0
        self.primary_sponsor = None

    def add_vote(self, vote) -> None:
        self.vote = vote

    def add_supporter(self, is_vote_yes: bool) -> None:
        if is_vote_yes:
            self.supporter_count += 1
            return
        self.opposer_count += 1

    def add_primary_sponsor(self, name_of_sponsor: str | None) -> None:
        self.primary_sponsor = name_of_sponsor or "Unknown"

    @staticmethod
    def header() -> List[str]:
        return ["id", "title", "supporter_count", "opposer_count", "primary_sponsor"]

    def __repr__(self) -> str:
        return f"Bills({self.id!r}, {self.title!r}, {self.supporter_count!r}, {self.opposer_count!r}, {self.primary_sponsor!r})"

    def __iter__(self):
        return iter([self.id, self.title, self.supporter_count, self.opposer_count,
                     self.primary_sponsor])
