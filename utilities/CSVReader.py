import csv
import os


class ReadCSV:
    @staticmethod
    def read_csv_by_id(target_id, key):
        csv_file_path = os.getcwd() + '//resources//testdata.csv'
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['ID'] == target_id:
                    result = dict(row)
                    return result[key]
            else:
                print(f"No data found for ID {target_id}")
        return None

