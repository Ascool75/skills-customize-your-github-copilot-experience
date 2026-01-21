"""
REST APIs with RapidAPI - Starter Code

This starter code provides a template for integrating and consuming REST APIs
using the RapidAPI platform.

Instructions:
1. Sign up for a free account at https://rapidapi.com
2. Find two APIs in the marketplace that interest you
3. Subscribe to each API (free tier available for many)
4. Copy your API key from the RapidAPI dashboard
5. Replace API_KEY below with your actual key
6. Choose your APIs and implement the functions
"""

import requests
import json

# Your RapidAPI key (get this from your RapidAPI dashboard)
API_KEY = "YOUR_API_KEY_HERE"

# Headers for RapidAPI requests
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "api-host-name.p.rapidapi.com"  # Replace with your API host
}


def fetch_from_api(url, headers, params=None):
    """
    Generic function to fetch data from an API
    
    Args:
        url (str): The API endpoint URL
        headers (dict): Request headers including API key
        params (dict): Query parameters for the request
    
    Returns:
        dict: Parsed JSON response from the API
    """
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching from API: {e}")
        return None


def get_api_data(query):
    """
    Example function to fetch data from your chosen API
    
    TODO: Implement this function with your API endpoint
    """
    # Example: Replace with your actual API endpoint
    # url = "https://api-name.p.rapidapi.com/endpoint"
    # params = {"q": query}
    # return fetch_from_api(url, HEADERS, params)
    pass


def display_results(data):
    """
    Display API results in a user-friendly format
    
    Args:
        data (dict): The API response data
    """
    if data is None:
        print("No data to display")
        return
    
    # TODO: Format and display your API results
    print(json.dumps(data, indent=2))


def main():
    """Main program logic"""
    print("Welcome to the RapidAPI Integration App!")
    print("=" * 50)
    
    # TODO: Add your program logic here
    # Example: Get user input, fetch from APIs, display results
    
    # Sample query
    query = input("Enter your search query: ")
    
    # Fetch and display data
    data = get_api_data(query)
    display_results(data)


if __name__ == "__main__":
    main()
