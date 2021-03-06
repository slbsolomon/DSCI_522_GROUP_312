# author: Group 312, George, Eithar, Sam
# date: 2020-1-18

"""
Downloads data csv data from the web to a local filepath as either a csv or feather file format.

Usage: scripts/load_data.py --url=<url> --file_path=<file_path> 

Options:
--url=<file_path>  url from where to download the data
--file_path=<file_path>  Path (including filename) to the csv file.
"""


  
from docopt import docopt
import requests
import os
import pandas as pd
import os.path

opt = docopt(__doc__)

def main(url, file_path):
  
  data = pd.read_csv(url, header = None)
  data.to_csv(file_path, index = False)

  # tests
  assert os.path.isfile(file_path)
  return

if __name__ == "__main__":
   main(url = opt["--url"], file_path = opt["--file_path"])
