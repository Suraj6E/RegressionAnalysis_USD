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

USD_PMI_URL = 'https://calendar-api.fxstreet.com/en/api/v1/events/38ec9435-34cc-4704-9445-80fabf6c0120/historical'
USD_PMI = get_data_from_api(USD_PMI_URL, headers)

if USD_PMI:
    # Process the retrieved data here
    #print(USD_PMI)

      # Save the api_data to a JSON file
    with open('./data/USD_PMI.json', 'w') as json_file:
        json.dump(USD_PMI, json_file)
else:
    print("Failed to retrieve data from the API.")