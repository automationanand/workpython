import pytest
import requests
import pytest

# def test_divisible_by_3(input_value):
#    assert input_value % 3 == 0
#
# def test_divisible_by_6(input_value):
#    assert input_value % 6 == 0


def test_get_locations_for_us_90210_check_status_code_equals_200():
   response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo&datatype=csv")
   assert response.status_code == 200

   response.content()