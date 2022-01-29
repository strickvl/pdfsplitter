# AUTOGENERATED! DO NOT EDIT! File to edit: 02_scraper.ipynb (unless otherwise specified).

__all__ = ['add_scheme_and_domain', 'get_pdf_links', 'download_pdf_files']

# Cell
import json
import os
import datetime
from pathlib import Path
from typing import Any

import pandas as pd
import numpy as np
import fitz

from rich import print
from rich.console import Console
from rich.table import Table

# Cell
import os
import requests
import re
from urllib.parse import urlparse

from bs4 import BeautifulSoup

# Cell
def add_scheme_and_domain(partial_url, main_source):
    """
    Given a partial url and a domain, return a full url.
    """
    scheme = urlparse(main_source).scheme
    hostname = urlparse(main_source).netloc
    base_url = scheme + "://" + hostname

    if partial_url[0] == "/":
        return base_url + partial_url
    else:
        return partial_url

# Cell
def get_pdf_links(url):
    """
    Given a url, return a list of all pdf links on the page.
    """
    # Get the html of the page
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    # Find all the links on the page
    links = soup.find_all("a")
    # Find all the pdf links
    pdf_links = []
    for link in links:
        if link.get("href") is not None:
            if re.search(".pdf$", link.get("href")):
                pdf_links.append(add_scheme_and_domain(link.get("href"), url))
    return pdf_links

# Cell
def download_pdf_files(pdf_links, destination="."):
    """
    Given a list of pdf links, download all the pdfs.
    """
    # create the destimation directory if it doesn't exist
    if not os.path.exists(destination):
        os.makedirs(destination)
    for link in pdf_links:
        r = requests.get(link)
        with open(destination + "/" + link.split("/")[-1], "wb") as f:
            f.write(r.content)