import csv
import pytest
#csv file
@pytest.mark.csvfile1
def test_csvfilehandling():
 with open("testdata\\credentials.csv") as data:
  finaldata= csv.DictReader(data)
  print(finaldata)
  listdata=list(finaldata)
  print(listdata)