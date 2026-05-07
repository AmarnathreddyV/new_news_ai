import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

def _clean_text(soup):
    # remove scripts/styles
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    # collect paragraphs
    paragraphs = [p.get_text(" ", strip=True) for p in soup.find_all("p")]
    text = " ".join(paragraphs)

    # normalize spaces
    text = " ".join(text.split())
    return text

def extract_article(url: str) -> str:
    try:
        # 1) Try normal request
        resp = requests.get(url, headers=HEADERS, timeout=10)
        if resp.status_code != 200 or "captcha" in resp.text.lower():
            raise Exception("Blocked or non-200")

        soup = BeautifulSoup(resp.text, "html.parser")
        text = _clean_text(soup)

        # If too small, likely blocked/JS site
        if len(text) < 500:
            raise Exception("Content too small / blocked")

        return text[:5000]

    except Exception:
        # 2) Fallback via textise (textise dot iitty) or textise alternative
        # Using textise-style mirror to bypass blocks
        try:
            alt_url = f"https://textise.net/showtext.aspx?strURL={url}"
            resp = requests.get(alt_url, headers=HEADERS, timeout=10)
            soup = BeautifulSoup(resp.text, "html.parser")
            text = _clean_text(soup)

            if len(text) < 200:
                raise Exception("Fallback failed")

            return text[:5000]
        except Exception:
            return "ERROR: Unable to extract article content (site may block scraping)."