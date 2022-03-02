import requests
from typing import List
from bs4 import BeautifulSoup as soupa

from ...filesystem import helper as fs
from ... import definitions as DD

def get_main_page(persist: bool = True, debug: bool = False) -> requests.Response:
    response = requests.get(DD.URL_HGC_DATA_EXCHANGE)
    if persist:
        fs.save_finding(response.content, DD.FILENAME_DATA_EXCHANGE_HTML)
    if debug:
        print(response.content)
    return response


def get_xsd_urls(persist: bool = True, debug: bool = False) -> List[str]:
    main_page = get_main_page(False)
    soup = soupa(main_page.text, features="html.parser")
    a_tags = soup.find_all('a', text="XSD")
    xsd_urls = [a.attrs["href"] for a in a_tags]

    joined = "\n".join(xsd_urls)
    if persist:
        fs.save_finding(joined, DD.FILENAME_XSD_URLS)
    if debug:
        print(joined)

    return xsd_urls


def get_xsds(persist: bool = True, debug: bool = False) -> None:
    xsd_urls = get_xsd_urls(False)
    url_genexpr = (DD.URL_HGC_BASE + url for url in xsd_urls)
    for url in url_genexpr:
        response = requests.get(url)
        filename = url.split('/')[-1]

        if persist:
            fs.save_xsd(response.content, filename)            
        if debug:
            print(response.text)
