import os
import unittest
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestCreatePost(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8000/admin/login/?next=/admin/')
        username = self.driver.find_element_by_name("username")
        username.send_keys("huilin")
        password = self.driver.find_element_by_name("password")
        password.send_keys("001234AB")
        password.send_keys(Keys.RETURN)
        current_url = self.driver.current_url

    def test_post_all_empty(self):
        driver = self.driver
        driver.get('http://localhost:8000/admin/blog/post/add/')
        assert "Add post | Django site admin" in driver.title
        save_btn = driver.find_element_by_name("_save")
        save_btn.click()
        assert "Please correct the errors below" in driver.page_source

    def test_post_all_input(self):
        driver = self.driver
        driver.get('http://localhost:8000/admin/blog/post/add/')
        assert "Add post | Django site admin" in driver.title
        title = driver.find_element_by_name("title")
        title.send_keys("Title")
        body = driver.find_element_by_name("body")
        body.send_keys("Body")
        categories = driver.find_element_by_xpath("//select[@name='categories']/option[@value='1']")
        categories.click()
        save_btn = driver.find_element_by_name("_save")
        save_btn.click()
        assert 'http://localhost:8000/admin/blog/post/' == driver.current_url
        assert 'The post' in driver.page_source
        assert "was added successfully." in driver.page_source


    def tearDown(self):
            self.driver.close()
