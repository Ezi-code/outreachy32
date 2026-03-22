"""get and print the status code of the response of a list of URLs from a .csv file."""

import requests
import os
import csv
from datetime import datetime

CSV_FILE=os.path.join(os.getcwd(),"app/Task 2 - Intern.csv")

def create_error_file(error_msg):
    """save urls with errors for reference."""
    with open("errors.txt", "a") as f:
        f.write(f"{error_msg} {str(datetime.now())}\n")
    

def get_url_from_file(file_path: str) -> list[str]:
    """get urls from csv a file."""
    urls = []
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if row:
                urls.append(row[0])
    return urls


def get_status_code(url: str) -> int:
    """get the status code of a url."""
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except requests.exceptions.RequestException as err:
        create_error_file(f"(Error) {url} -> {err}")
        return None
    

def main():
    """main function."""
    urls = get_url_from_file(CSV_FILE)
    for url in urls:
        try:
            status = get_status_code(url)
            if isinstance(status, int):
                print(f"({status}) {url}")
        except Exception as e:
           create_error_file(f"(Error) {url} -> {e}")


if __name__=="__main__":
    main()
