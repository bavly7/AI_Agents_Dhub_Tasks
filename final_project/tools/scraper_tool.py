import requests
from bs4 import BeautifulSoup
import re

def scrape_website(url: str) -> dict:
    result = {
        "homepage_text": "",
        "emails": [],
        "contact_text": ""
    }

    try:
        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        result["homepage_text"] = soup.get_text(separator=" ", strip=True)[:3000]

        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", response.text)
        result["emails"].extend(emails)

        for path in ["/contact", "/contact-us", "/about"]:
            try:
                contact_response = requests.get(url.rstrip("/") + path, headers=headers, timeout=10)
                if contact_response.status_code == 200:
                    contact_soup = BeautifulSoup(contact_response.text, "html.parser")
                    result["contact_text"] = contact_soup.get_text(separator=" ", strip=True)[:3000]
                    contact_emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", contact_response.text)
                    result["emails"].extend(contact_emails)
                    break
            except:
                continue

        result["emails"] = list(set(result["emails"]))

    except Exception as e:
        result["error"] = str(e)

    return result