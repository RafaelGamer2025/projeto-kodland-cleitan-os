import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re

def find_emails(html, log):
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", html)
    for e in set(emails):
        log(f"Email: {e}")

def detect_tech(html, log):
    techs = ["wordpress", "bootstrap", "jquery", "react"]

    for t in techs:
        if t in html.lower():
            log(f"[TEC] {t}")

def analyze_site(url, log):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
    except Exception as e:
        log(f"Erro: {e}")
        return

    log("[OK] Conectado")

    for a in soup.find_all("a", href=True)[:10]:
        log(urljoin(url, a["href"]))

    find_emails(r.text, log)
    detect_tech(r.text, log)