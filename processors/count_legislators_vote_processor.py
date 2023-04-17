from typing import Dict

from csv_challenge.domain.legislator import Legislator
from csv_challenge.domain.result_from_legislator import ResultFromLegislator
from csv_challenge.domain.voteResult import VoteResult
from csv_challenge.processors.processor_base import ProcessorBase


class CountLegislatorsVoteProcessor(ProcessorBase):
    def process(self, data: Dict[int, VoteResult]) -> None:
        legislators_by_id: Dict[int, Legislator] = {}
        resultFromLegislators: Dict[int, ResultFromLegislator] = {}
        for vote_result in data.values():
            result = resultFromLegislators.get(vote_result.legislator_id)
            legislator = legislators_by_id[vote_result.legislator_id]
            if not result:
                no = 1 if vote_result.is_no() else 0
                yes = 1 if vote_result.is_yes() else 0
                resultFromLegislators[vote_result.legislator_id] = \
                    ResultFromLegislator(legislator,
                                         yes,
                                         no)
                continue
            result.increment_votes(vote_result.is_yes())
        return result
