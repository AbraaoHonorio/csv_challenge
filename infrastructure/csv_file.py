import csv
import os
import pathlib
from typing import Dict, List, TypeVar

from csv_challenge.domain.csvNotFound import CsvNotFound

T = TypeVar("T")


class CsvFile:

    def __init__(self, path_from_files: str):
        super().__init__()
        self.path_from_files = path_from_files

    def load_data_by_type(self, type_data: T,
                          file_path: str, ) -> Dict[int, T]:
        """
               Loads a CSV file as a dictionary of objects of a given type.

               Args:
                   type_data (Type[T]): the type of object to be loaded from the CSV file
                   file_path (str): the name of the CSV file to be loaded (relative to path_from_files)

               Returns:
                   A dictionary mapping object IDs to instances of type_data loaded from the CSV file.

               Raises:
                   CsvNotFound: if the specified file_path does not exist.
                   Exception: if an unexpected error occurs while loading the CSV file.
        """
        try:
            data: Dict[int, T] = {}
            filename = self.path_from_files + file_path
            with open(filename) as stream:
                reader = csv.reader(stream)
                next(reader, None)  # skip the headers
                for row in reader:
                    obj = type_data(*row)
                    data[obj.id] = obj
            return data
        except FileNotFoundError as e:
            raise CsvNotFound(
                f"File not found. Please check the file path {filename}.",
                e)
        except Exception as e:
            raise Exception(
                f"An unexpected error occurred, please check log:.", e)

    def save_data(self, data: List[T], file_path: str):
        """
                Saves a list of objects to a CSV file.

                Args:
                    data (List[T]): the list of objects to be saved to the CSV file
                    file_path (str): the name of the CSV file to be saved (relative to path_from_files)

                Returns:
                    True if the file was successfully saved.

                Raises:
                    Exception: if an unexpected error occurs while saving the CSV file.
       """
        try:
            filename = self.path_from_files + file_path
            path = pathlib.Path(filename)
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(filename, "w") as stream:
                writer = csv.writer(stream)
                writer.writerow(data[0].header())
                writer.writerows(data)
                return True
        except Exception as e:
            raise Exception(
                f"An unexpected error occurred, please check log:.", e)
