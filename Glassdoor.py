# Lint as: python3
"""Glassdoor.com scraper."""

__author__ = 'Xavier Collantes'

import requests
from bs4 import BeautifulSoup4 as Soup

class Glassdoor:
  def __init__(self, jobTitle, city):
    self.url = 'https://www.glassdoor.com/Salaries/mountain-view-software-engineer-salary-SRCH_IL.0,13_IC1147431_KO14,31.htm'
    self.title = jobTitle
    self.city = city

