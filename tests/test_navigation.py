import os
import unittest
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestNavigation(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_click_header(self):
        driver = self.driver
        driver.get('http://localhost:8000/blog/')
        assert "Blog" in driver.page_source
        header = driver.find_element_by_link_text("Hui Lin's Portfolio")
        header.click()
        current_url = driver.current_url
        assert 'http://localhost:8000/home/' == current_url

    def test_click_home(self):
        driver = self.driver
        driver.get('http://localhost:8000/blog/')
        assert "Blog" in driver.page_source
        home = driver.find_element_by_link_text("Home")
        home.click()
        current_url = driver.current_url
        assert 'http://localhost:8000/home/' == current_url

    def test_click_blog(self):
        driver = self.driver
        driver.get('http://localhost:8000/home/')
        assert "Resume" in driver.page_source
        blog = driver.find_element_by_link_text("Blog")
        blog.click()
        current_url = driver.current_url
        assert 'http://localhost:8000/blog/' == current_url

    def test_click_post(self):
        driver = self.driver
        driver = self.driver
        driver.get('http://localhost:8000/blog/')
        assert "Blog" in driver.page_source
        post = driver.find_element_by_link_text("Patch")
        post.click()
        current_url = driver.current_url
        assert 'http://localhost:8000/blog/3/' == current_url

    def test_click_category(self):
        driver = self.driver
        driver = self.driver
        driver.get('http://localhost:8000/blog/')
        assert "Blog" in driver.page_source
        category = driver.find_element_by_link_text("Projects")
        category.click()
        current_url = driver.current_url
        assert 'http://localhost:8000/blog/Projects/' == current_url

    def tearDown(self):
        self.driver.close()
