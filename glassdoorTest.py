# Lint as: python3
"""Test glassdoor.py"""

from unittest import TestCase
from unittest.mock import Mock
from glassdoor import Glassdoor
import requests


class GlassdoorTest(unittest.TestCase):
  def setUp(self):
    pass


  def testRequest(self):
    requestMock = Mock(spec=requests)



if __name__ == '__main__':
  unittest.main()
