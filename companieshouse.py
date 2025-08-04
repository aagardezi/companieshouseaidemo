import requests
from requests.auth import HTTPBasicAuth
import os
import base64
from companieshouse import CompaniesHouseClient

#Converted the companies hosue API into a pip instalable library. The code below is not needed but could be used to
#understand how to access the API so leaving it here.
class CompaniesHouseClient_local:
    """
    A client for interacting with the Companies House API.
    """
    def __init__(self, api_key=None):
        """
        Initializes the Companies House client.

        Args:
            api_key: Your Companies House API key. If not provided, it will
                     look for the COMPANIES_HOUSE_API_KEY environment variable.
        """
        self.api_key = api_key or os.environ.get("COMPANIES_HOUSE_API_KEY")
        if not self.api_key:
            raise ValueError("API key not provided. Please provide it as an argument or set the COMPANIES_HOUSE_API_KEY environment variable.")
        self.base_url = "https://api.company-information.service.gov.uk"

    def _make_request(self, endpoint, params=None):
        """
        Makes a request to the Companies House API.

        Args:
            endpoint: The API endpoint to call.
            params: A dictionary of query parameters.

        Returns:
            A dictionary containing the JSON response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        auth = (self.api_key, "")
        response = requests.get(url, params=params, auth=auth)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()

    def search_companies(self, query):
        """
        Searches for companies.

        Args:
            query: The search query.

        Returns:
            A dictionary containing the search results.
        """
        return self._make_request("search/companies", params={"q": query})

    def get_company_profile(self, company_number):
        """
        Gets the profile of a company.

        Args:
            company_number: The company number.

        Returns:
            A dictionary containing the company profile.
        """
        return self._make_request(f"company/{company_number}")
    
    def get_company_officers(self, company_number):
        """
        Gets the company officers.

        Args:
            company_number: The company number.

        Returns:
            A dictionary containing the company officers.
        """

        return self._make_request(f"company/{company_number}/officers")
    
    def get_company_filing_history(self, filing_history_url):
        """
        Gets the company filing history.

        Args:
            filing_history_url: A final part of the filings url from the company profile record.

        Returns:
            A dictionary containing the filing history.
        """
        return self._make_request(f"{filing_history_url}")

def search_companies(params):
    client = CompaniesHouseClient()
    search_results = client.search_companies(params['company_name_search_string'])
    return search_results

def get_company_profile(params):
    client = CompaniesHouseClient()
    company_profile = client.get_company_profile(params['company_number'])
    return company_profile

def get_company_officers(params):
    client = CompaniesHouseClient()
    company_officers = client.get_company_officers(params['company_number'])
    return company_officers

def get_company_filing_history(params):
    client = CompaniesHouseClient()
    company_filing_history = client.get_company_filing_history(params['filing_history_url'])
    return company_filing_history

function_handler = {
    "search_companies": search_companies,
    "get_company_profile": get_company_profile,
    "get_company_officers": get_company_officers,
    "get_company_filing_history": get_company_filing_history
}


if __name__ == '__main__':
    # Example usage:
    # Make sure to set the COMPANIES_HOUSE_API_KEY environment variable
    # export COMPANIES_HOUSE_API_KEY="YOUR_API_KEY"


    
    # r = requests.get('https://api.company-information.service.gov.uk/company/00002065', auth=(keyEncoded, ''))
    # print(r.text)
    # print("hello")

    client = CompaniesHouseClient()

    # Search for companies
    search_results = client.search_companies("python")
    print(search_results)
    print("Search results:")
    for item in search_results.get("items", []):
        print(f"- {item.get('title')}")

    # Get a company profile (replace with a valid company number)
    if search_results.get("items"):
        company_number = search_results["items"][0]["company_number"]
        company_profile = client.get_company_profile(company_number)
        print("COMPANY PROFILE")
        print(company_profile)
        company_officers =  client.get_company_officers(company_number)
        print("COMPANY OFFICERS")
        print(company_officers)
        print(f"\nCompany profile for {company_profile.get('company_name')}:")
        print(f"  Company number: {company_profile.get('company_number')}")
        print(f"  Status: {company_profile.get('company_status')}")
        print(f"  Creation date: {company_profile.get('date_of_creation')}")
        company_filing_history = client.get_company_filing_history(company_profile['links'].get('filing_history'))
        print(company_filing_history)
