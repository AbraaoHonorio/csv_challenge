import csv
from collections import defaultdict

from domain.bill import Bill
from domain.legislator import Legislator
from domain.result_from_legislator import ResultFromLegislator
from domain.vote import Votes
from domain.voteResult import VoteResult

FILES_PATH = 'files/'

CSV_NAMES_READS = ["legislators.csv", "bills.csv", "votes.csv",
                         "vote_results.csv"]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hello World!")
