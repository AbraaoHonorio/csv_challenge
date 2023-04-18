from csv_challenge.infrastructure.csv_file import CsvFile
from csv_challenge.processors.count_bills_vote import CountBillsVoteProcessor
from csv_challenge.processors.count_legislators_vote_processor import \
    CountLegislatorsVoteProcessor
from domain.bill import Bill
from domain.legislator import Legislator
from domain.vote import Vote
from domain.voteResult import VoteResult

FILES_PATH_INPUT = 'files/'
FILES_PATH_OUTPUT = 'files_answer/'

CSV_NAMES_READS = ["legislators.csv", "bills.csv", "votes.csv",
                   "vote_results.csv"]

if __name__ == '__main__':
    csv_read = CsvFile(path_from_files=FILES_PATH_INPUT)
    legislators_by_id = csv_read.load_data_by_type(Legislator, CSV_NAMES_READS[0])
    bills_by_id = csv_read.load_data_by_type(Bill, CSV_NAMES_READS[1])
    votes_by_id = csv_read.load_data_by_type(Vote, CSV_NAMES_READS[2])
    vote_result_by_id = csv_read.load_data_by_type(VoteResult, CSV_NAMES_READS[3])

    result_count_bills = CountBillsVoteProcessor \
        .process(vote_result_by_id, bills_by_id, votes_by_id, legislators_by_id)
    result_count_legistators = CountLegislatorsVoteProcessor \
        .process(vote_result_by_id, legislators_by_id)

    csv_write = CsvFile(path_from_files=FILES_PATH_OUTPUT)

    csv_write.save_data(list(result_count_bills),
                        "legislators-support-oppose-count.csv")
    csv_write.save_data(list(result_count_legistators),
                        "bills_with_votes.csv")
