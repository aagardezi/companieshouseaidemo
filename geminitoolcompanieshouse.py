search_companies = dict(
    name="search_companies",
    description="Search for company details from companies house API",
    parameters={
        "type": "OBJECT",
        "properties": {
            "company_name_search_string": {
                "type": "STRING",
                "description": "Name of a company you want to search for in the companies house database",
            },
        },
    },
)

get_company_profile = dict(
    name="get_company_profile",
    description="Get the profile of a company as listed in the companies house database",
    parameters={
        "type": "OBJECT",
        "properties": {
            "company_number": {
                "type": "STRING",
                "description": "Company number used to identify a company in the companies house database",
            },
        },
    },
)

get_company_officers = dict(
    name="get_company_profile",
    description="Get the list of company offices as listed in the companies house database of a company",
    parameters={
        "type": "OBJECT",
        "properties": {
            "company_number": {
                "type": "STRING",
                "description": "Company number used to identify a company in the companies house database",
            },
        },
    },
)

get_company_filing_history = dict(
    name="get_company_filing_history",
    description="Get the the filing history of a company as listed in the companies house database of a company",
    parameters={
        "type": "OBJECT",
        "properties": {
            "filing_history_url": {
                "type": "STRING",
                "description": "Get the the filing history of a company in the companies house database using the url listed in the company profile record",
            },
        },
    },
)
