
from pathlib import Path
import json
import pytest
#json file
@pytest.mark.usertest
def test_jsonfilehandling():
    file_path = Path(__file__).parent.parent / "testdata" / "creds.json"

    with open(file_path, "r") as data:
        json_data = json.load(data)

    print(json_data) 
    abc=json_data["password"]
    print(abc)