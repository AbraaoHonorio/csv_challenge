class VoteResult:
    def __init__(self, id: int, legislator_id: int, vote_id: int, vote_type: int):
        self.id = int(id)
        self.legislator_id = int(legislator_id)
        self.vote_id = int(vote_id)
        self.vote_type = int(vote_type)

    def is_yes(self) -> bool:
        return self.vote_type == 1

    def is_no(self) -> bool:
        return self.vote_type == 2
