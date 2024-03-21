import json
import unittest
from utils.searchdoc import searchdoc_api
import os

AZURE_APIM_ENDPOINT = os.getenv("AZURE_APIM_ENDPOINT")
APIM_SUB_KEY = os.getenv("APIM_SUB_KEY")

class TestSearchDocAPI(unittest.TestCase):

    def test_searchdoc_api_success(self):
        # Mock the API response
        # m.post('http://example.com/docsearch', text=json.dumps({"result": "success"}))

        # Define the input parameters for the test
        apim_endpoint = AZURE_APIM_ENDPOINT
        options = {
            "history": "some history",
            "approach": "certain approach",
            "overrides": "necessary overrides"
        }

        # Call the function with the test parameters
        response = searchdoc_api(apim_endpoint, options, APIM_SUB_KEY)

        # Assert that the response is as expected
        self.assertEqual(response, {"result": "success"})

    # You can add more test cases here to cover different scenarios,
    # such as handling errors or different inputs.

if __name__ == '__main__':
    unittest.main()
