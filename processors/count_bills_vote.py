from typing import Dict, Iterable

from csv_challenge.domain.bill import Bill
from csv_challenge.domain.legislator import Legislator
from csv_challenge.domain.vote import Vote
from csv_challenge.domain.voteResult import VoteResult


class CountBillsVoteProcessor:

    @staticmethod
    def process(vote_result_by_id: Dict[int, VoteResult],
                bills_by_id: Dict[int, Bill],
                votes_by_id: Dict[int, Vote],
                legislators_by_id: Dict[int, Legislator]) -> Iterable[Bill]:
        bill_id_by_vote_id = {vote.id: vote.bill_id for vote in votes_by_id.values()}

        for vote in vote_result_by_id.values():
            bill = bills_by_id[bill_id_by_vote_id[vote.vote_id]]
            legislator = legislators_by_id.get(bill.sponsor_id, None)
            name_of_sponsor = legislator.name if legislator else None
            bill.add_vote(vote)
            bill.add_supporter(vote.is_yes())
            bill.add_primary_sponsor(name_of_sponsor)

        return bills_by_id.values()
