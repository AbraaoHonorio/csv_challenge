import csv
from typing import Dict

from csv_challenge.domain.CsvNotFound import CsvNotFound
from csv_challenge.domain.LoadDataInterface import LoadDataInterface, T


class CsvRead(LoadDataInterface[T]):

    def __init__(self, path_from_files: str,
                 file_path: str):
        super().__init__()
        self.full_files_path = path_from_files + file_path

    def load_data(self, type_data: T) -> Dict[int, T]:
        try:
            data: Dict[int, T] = {}
            with open(self.full_files_path) as stream:
                reader = csv.reader(stream)
                next(reader, None)  # skip the headers
                for row in reader:
                    obj = type_data(*row)
                    data[obj.id] = obj
            return data
        except FileNotFoundError:
            raise CsvNotFound(
                f"File not found. Please check the file path {self.full_files_path}.")
