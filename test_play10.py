from openpyxl import load_workbook
import pytest

@pytest.mark.excelwrite
def test_excelhandlewritingwrite():
    exceldata=load_workbook("testdata/excel123.xlsx")
    sheet=exceldata["Sheet1"]
    sheet["A4"]="testing000"
    exceldata.save("testdata/excel123.xlsx")
