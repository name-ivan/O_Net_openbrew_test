import requests
import allure


class BreweryEndpoint:
    BASE_URL = "https://api.openbrewerydb.org/v1/breweries"

    @staticmethod
    @allure.step("Send GET request to /breweries with by_type={brewery_type}")
    def get_by_type(brewery_type: str):
        url = f"{BreweryEndpoint.BASE_URL}?by_type={brewery_type}"
        response = requests.get(url)

        # Attach response for visibility (optional, but helpful)
        allure.attach(
            response.text,
            name=f"Response for by_type={brewery_type}",
            attachment_type=allure.attachment_type.JSON
        )
        
        return response


    @staticmethod
    @allure.step("Parse response as JSON")
    def get_json(response):
        try:
            return response.json()
        except Exception:
            allure.attach(response.text, name="Invalid JSON", attachment_type=allure.attachment_type.TEXT)
            raise
