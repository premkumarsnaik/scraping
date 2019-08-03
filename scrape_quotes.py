from selenium import webdriver

from pages.qotes_page import QuotesPage

chrome = webdriver.Chrome(executable_path = r"C:\Users\dell\Desktop\Everything\programming\python\chromedriver")
chrome.get('http://quotes.toscrape.com/search.aspx')
page = QuotesPage(chrome)

author_name = input('enter author name : ')
page.select_author(author_name)
