from django.test import TestCase
from django.test import Client
from django.urls import reverse

from .views import *

from unittest.mock import Mock

# Create your tests here.

def test_home_index():
        mock = Mock()
        print('HI',home_index(mock))


##class TestView(TestCase):
##    
##    def test_home_index(self):
##        mock = Mock()
##        print('HI',home_index(mock))
##    
##    def test_view_return(self):
##        client = Client()
##        response = client.get('/home')
##        hi = response
##        print(response)
