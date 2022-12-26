import re
import time
import urllib.parse
from base64 import standard_b64encode
from bot.modules.important import humanbytes, TimeFormatter
import cloudscraper
import requests
from bs4 import BeautifulSoup

from bot import Config





def mdis_k(urlx):
    scraper = cloudscraper.create_scraper(interpreter="nodejs", allow_brotli=False)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"
    }
    apix = f"http://x.egraph.workers.dev/?param={urlx}"
    response = scraper.get(apix, headers=headers)
    query = response.json()
    return query


def mdisk(url):
    check = re.findall(r"\bhttps?://.*mdisk\S+", url)
    if not check:
        textx = f"**Invalid Mdisk Url**"
        return textx
    else:
        try:
            fxl = url.split("/")
            urlx = fxl[-1]
            uhh = mdis_k(urlx)
            duration = {uhh["duration"]}
            text = f'**📂 Title** : `{uhh["filename"]}`\n\n📥 **Download URL (Support All Player)** :- {uhh["source"]}\n\n📤 **Download URL (Support Only MX Player)** :- {uhh["download"]}\n\n💎 **Uploader User ID** :- `{uhh["from"]}`\n\n💠 **Uploader User Name** :- `@{uhh["display_name"]}`\n\n📹 **Video Width** :- `{uhh["width"]}`\n\n🎞 **Video Height** :- {uhh["height"]}\n\n📦 **Video Duration** :- `{uhh["duration"]}s`\n\n📊 **Video Size** :- `{uhh["size"]}kb`'
            return text
        except ValueError:
            textx = f"The Content is Deleted."
            return textx


