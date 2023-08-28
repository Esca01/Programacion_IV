# api_module.py
from sodapy import Socrata

def fetch_data():
    client = Socrata("www.datos.gov.co", None)
    results = client.get("ch4u-f3i5", limit=2000)
    return results
