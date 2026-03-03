import requests
import json

PINATA_API_KEY = "e4d9da83f2720d7f378d"
PINATA_SECRET_KEY = "bcfe4c287a98b0f2163e43bd8d90cf1c06bb74b8743aae5338e91f24f8fea43f"

def pin_to_ipfs(data):
    assert isinstance(data, dict), "Error pin_to_ipfs expects a dictionary"
    
    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"  # <-- Changed endpoint
    headers = {
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_SECRET_KEY,
        "Content-Type": "application/json"  # <-- Added content type
    }
    
    response = requests.post(url, json=data, headers=headers)  # <-- Send as JSON body
    result = response.json()
    cid = result["IpfsHash"]
    return cid

def get_from_ipfs(cid, content_type="json"):
    assert isinstance(cid, str), "get_from_ipfs accepts a cid in the form of a string"
    
    url = f"https://gateway.pinata.cloud/ipfs/{cid}"
    response = requests.get(url)
    data = response.json()
    
    assert isinstance(data, dict), "get_from_ipfs should return a dict"
    return data
