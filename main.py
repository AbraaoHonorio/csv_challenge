from csv_challenge.infrastructure.csv_read import CsvRead
from domain.bill import Bill
from domain.legislator import Legislator
from domain.vote import Votes
from domain.voteResult import VoteResult

FILES_PATH = 'files/'

CSV_NAMES_READS = ["legislators.csv", "bills.csv", "votes.csv",
                   "vote_results.csv"]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    legislators = CsvRead(path_from_files=FILES_PATH,
                          file_path=CSV_NAMES_READS[0]).load_data(Legislator)
    bills = CsvRead(path_from_files=FILES_PATH,
                    file_path=CSV_NAMES_READS[1]).load_data(Bill)
    votes = CsvRead(path_from_files=FILES_PATH,
                    file_path=CSV_NAMES_READS[2]).load_data(Votes)
    vote_results = CsvRead(path_from_files=FILES_PATH,
                           file_path=CSV_NAMES_READS[3]).load_data(VoteResult)

