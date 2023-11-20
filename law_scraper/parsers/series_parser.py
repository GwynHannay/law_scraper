from bs4 import BeautifulSoup

def get_table(page):
    soup = BeautifulSoup(page, "html.parser")