from collections import defaultdict
from typing import Dict, Iterable

from csv_challenge.domain.legislator import Legislator
from csv_challenge.domain.legislator_with_votes import LegislatorWithVotes
from csv_challenge.domain.voteResult import VoteResult


class CountLegislatorsVoteProcessor:

    @staticmethod
    def process(vote_result_by_id: Dict[int, VoteResult],
                legislators_by_id: Dict[int, Legislator]
                ) -> Iterable[LegislatorWithVotes]:
        legislator_votes = defaultdict(lambda: LegislatorWithVotes(None, 0, 0))

        for vote_result in vote_result_by_id.values():
            legislator_id = vote_result.legislator_id
            legislator = legislators_by_id[legislator_id]
            legislator_with_votes = legislator_votes[legislator_id]
            if vote_result.is_yes():
                legislator_with_votes.count_yes += 1
            elif vote_result.is_no():
                legislator_with_votes.count_no += 1
            legislator_with_votes.legislator = legislator

        return legislator_votes.values()
