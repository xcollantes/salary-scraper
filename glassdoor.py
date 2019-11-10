# Lint as: python3
"""Glassdoor.com scraper."""

__author__ = 'Xavier Collantes'

import requests
import bs4


class Glassdoor:
  def __init__(self, jobTitle, city):
    self.url = 'https://www.glassdoor.com/Salaries/mountain-view-software-engineer-salary-SRCH_IL.0,13_IC1147431_KO14,31.htm'
    self.title = jobTitle
    self.city = city

  def getPage(self):
    """GET Request target page marked by self.url.

    Returns:
      Webpage as a bs4 object.

    Raises:
      Timeout: Page took too long to load.
      HTTPError: Bad response.
      ConnectionError: DNS, refused connection errors.
    """
    try:
      response = requests.get(self.url)
      return response

    except requests.exceptions.Timeout as errTimeout:
      return "Page took too long: " + errTimeout
    except requests.exceptions.HTTPError as errHttp:
      return "HTTP Error: " + errHttp
    except requests.exceptions.ConnectionError as errConn:
      return "ConnectionError: " + errConn


