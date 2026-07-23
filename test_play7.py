import json
import pytest
#json file
@pytest.mark.jsonformat
def test_jsonfilehandling():
 with open("testdata\\creds.json") as data:
  finaldata= json.load(data)
  print(finaldata)