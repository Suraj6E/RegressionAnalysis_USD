import requests
import json


def get_data_from_api(api_url, headers):
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Check for any errors in the response

        data = response.json() 
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None


headers = {
    'authority': 'calendar-api.fxstreet.com',
    'method': 'GET',
    'path': '/en/api/v1/events/38ec9435-34cc-4704-9445-80fabf6c0120/historical',
    'scheme': 'https',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Origin': 'https://www.fxstreet.com',
    'Referer': 'https://www.fxstreet.com/',
    'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183'
}

# USD_manufaturing_PMI_URL = 'https://calendar-api.fxstreet.com/en/api/v1/events/38ec9435-34cc-4704-9445-80fabf6c0120/historical'
# USD_Service_PMI_URL = 'https://calendar-api.fxstreet.com/en/api/v1/events/5085ec6f-0c90-43d0-83f0-b936a41da1e7/historical'
# api_url = 'https://calendar-api.fxstreet.com/en/api/v1/events/ac172f6c-6b25-4a45-a986-c96789740c8b/historical'
# api_url = 'https://calendar-api.fxstreet.com/en/api/v1/events/0ba3bb41-ebb9-4a54-89f3-36346484dcfb/historical'
# api_url = 'https://calendar-api.fxstreet.com/en/api/v1/events/79282c38-c914-4080-9f7f-a085c86ba308/historical'
# api_url = 'https://calendar-api.fxstreet.com/en/api/v1/events/2e1d69f3-8273-4096-b01b-8d2034d4fade/historical'
# USD_Factory_Orders_MoM = 'https://calendar-api.fxstreet.com/en/api/v1/events/583bbfd1-2cf5-4f17-823e-e5ce34f91f49/historical'
# ISM_Manufacturing_Prices_Paid = 'https://calendar-api.fxstreet.com/en/api/v1/events/3b4f3bf2-fe18-4e5d-86af-8edc17d68680/historical'
# USD_ISM_Manufacturing_PMI = 'https://calendar-api.fxstreet.com/en/api/v1/events/2e1d69f3-8273-4096-b01b-8d2034d4fade/historical'
# api_url = 'https://calendar-api.fxstreet.com/en/api/v1/events/af5d396d-eff7-4023-add2-5a208861e63d/historical' #Producer Price Index ex Food & Energy (MoM)
# api_url = 'https://calendar-api.fxstreet.com/en/api/v1/events/ae8bd4b2-1a5f-4b9f-9b9c-6df04d23faee/historical' #Producer Price Index ex Food & Energy (YoY)
# api_url = 'https://calendar-api.fxstreet.com/en/api/v1/events/cba6f39e-5566-4fc8-86b3-1d0771fd5e3b/historical'  #Monthly Budget Statement
# api_url = 'https://calendar-api.fxstreet.com/en/api/v1/events/375f089e-b51b-4c95-9217-188bb36803f3/historical'  #UoM 5-year Consumer Inflation Expectation
# api_url = 'https://calendar-api.fxstreet.com/en/api/v1/events/31b216da-2502-4428-af5b-d3c54b68ebe4/historical'  #Retail Sales (MoM)
# api_url = 'https://calendar-api.fxstreet.com/en/api/v1/events/a2a2843d-443a-480a-b83a-a8f0dd0c3f04/historical'  #Retail Sales Control Group
# api_url = 'https://calendar-api.fxstreet.com/en/api/v1/events/2635188a-b377-4179-864c-029cad0ed529/historical'  #Industrial Production (MoM)
# api_url = 'https://calendar-api.fxstreet.com/en/api/v1/events/9ba65d91-c2d2-4e4b-b6f3-dfe3677dc980/historical'  #JOLTS Job Openings
# api_url = 'https://calendar-api.fxstreet.com/en/api/v1/events/b7abce59-89c3-42cc-8696-c4b6877cdee3/historical'  #Average Hourly Earnings (MoM)
# api_url = 'https://calendar-api.fxstreet.com/en/api/v1/events/fcfae951-09a7-449e-b6fe-525e1335aaba/historical'  #Fed Interest Rate Decision
# api_url = 'https://calendar-api.fxstreet.com/en/api/v1/events/9c689bbf-af2a-4f65-81a8-c5f5e2b78d70/historical'  #Initial Jobless Claims
# api_url = 'https://calendar-api.fxstreet.com/en/api/v1/events/fd5a3b53-db1c-4ec4-8393-ff91ca73a272/historical'  #Core Personal Consumption Expenditures
# api_url = 'https://calendar-api.fxstreet.com/en/api/v1/events/f056cc38-d62a-4a1f-8660-8160867fe480/historical'  #Gross Domestic Product Price
# api_url = 'https://calendar-api.fxstreet.com/en/api/v1/events/a25fb503-3399-4cb2-9c48-b335a966faf7/historical'  #Challenger Job Cuts
# api_url = 'https://calendar-api.fxstreet.com/en/api/v1/events/5bbf4174-08fe-4294-a2bf-2226b4b9b802/historical'  #Building Permits
api_url = 'https://calendar-api.fxstreet.com/en/api/v1/events/6c5853c1-a409-4722-bdea-17ad5d8a193f/historical'  #ISM Services PMI
data = get_data_from_api(api_url, headers)

if data:
    # Process the retrieved data here
    #print(data)

      # Save the api_data to a JSON file
    with open('./data/USD - ISM Services PMI.json', 'w') as json_file:
        json.dump(data, json_file)
else:
    print("Failed to retrieve data from the API.")