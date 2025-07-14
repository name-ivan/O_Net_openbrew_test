import pytest
import allure
from o_net_openbrew_test.endpoints.brewery_endpoint import BreweryEndpoint
from o_net_openbrew_test.utils.generators import random_letters, random_numbers, random_mixed

invalid_inputs = [
    random_letters(),
    random_numbers(),
    random_mixed(),
]

@allure.feature("Filter breweries by type")
@allure.story("Valid brewery type")
@pytest.mark.parametrize("brewery_type", ["micro", "brewpub", "large"])
def test_by_type_valid_multiple(brewery_type):
    response = BreweryEndpoint.get_by_type(brewery_type)
    assert response.status_code == 200

    breweries = BreweryEndpoint.get_json(response)
    assert isinstance(breweries, list)
    for b in breweries:
        assert b["brewery_type"] == brewery_type



@allure.feature("Filter breweries by type")
@allure.story("Invalid brewery types - letters, numbers, and mixed")
@pytest.mark.parametrize("brewery_type", invalid_inputs, ids=["letters_only", "numbers_only", "mixed"])
def test_by_type_invalid(brewery_type):
    response = BreweryEndpoint.get_by_type(brewery_type)
    assert response.status_code == 200

    data = BreweryEndpoint.get_json(response)
    assert not isinstance(data, list)
    assert "message" in data
