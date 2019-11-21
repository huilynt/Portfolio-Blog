import os
import unittest
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestLogin(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login_empty(self):
        driver = self.driver
        driver.get('http://localhost:8000/admin/login/?next=/admin/')
        assert "Log in | Django site admin" in driver.title
        username = driver.find_element_by_name("username")
        username.send_keys(Keys.RETURN)
        assert "Log in | Django site admin" in driver.page_source

    def test_login_wrong_username(self):
        driver = self.driver
        driver.get('http://localhost:8000/admin/login/?next=/admin/')
        assert "Log in | Django site admin" in driver.title
        username = driver.find_element_by_name("username")
        username.send_keys("huilin")
        password = driver.find_element_by_name("password")
        password.send_keys("wrong")
        password.send_keys(Keys.RETURN)
        assert "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive." in driver.page_source
        
    def test_login_wrong_password(self):
        driver = self.driver
        driver.get('http://localhost:8000/admin/login/?next=/admin/')
        assert "Log in | Django site admin" in driver.title
        username = driver.find_element_by_name("username")
        username.send_keys("wrong")
        password = driver.find_element_by_name("password")
        password.send_keys("001234AB")
        password.send_keys(Keys.RETURN)
        assert "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive." in driver.page_source
        
    def test_login_correct_username_password(self):
        driver = self.driver
        driver.get('http://localhost:8000/admin/login/?next=/admin/')
        assert "Log in | Django site admin" in driver.title
        username = driver.find_element_by_name("username")
        username.send_keys("huilin")
        password = driver.find_element_by_name("password")
        password.send_keys("001234AB")
        password.send_keys(Keys.RETURN)
        current_url = driver.current_url
        assert current_url == 'http://localhost:8000/admin/'

    def tearDown(self):
            self.driver.close()
