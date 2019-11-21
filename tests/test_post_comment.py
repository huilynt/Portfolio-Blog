import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

def test_all_empty():
    driver.get('http://localhost:8000/blog/3/')
    assert "Patch" in driver.page_source
    original_page = driver.page_source
    name = driver.find_element_by_name("author")
    name.send_keys(Keys.RETURN)
    assert original_page == driver.page_source

def test_name_only():
    driver.get('http://localhost:8000/blog/3/')
    assert "Patch" in driver.page_source
    original_page = driver.page_source
    name = driver.find_element_by_name("author")
    name.send_keys("Hui Lin")
    name.send_keys(Keys.RETURN)
    assert original_page == driver.page_source
    
def test_comment_only():
    driver.get('http://localhost:8000/blog/3/')
    assert "Patch" in driver.page_source
    original_page = driver.page_source
    comment = driver.find_element_by_name("body")
    comment.send_keys("This is a comment!")
    comment.send_keys(Keys.RETURN)
    assert original_page == driver.page_source

def test_name_comment_input():
    driver.get('http://localhost:8000/blog/3/')
    assert "Patch" in driver.page_source
    original_page = driver.page_source
    name = driver.find_element_by_name("author")
    comment = driver.find_element_by_name("body")
    submit_btn = driver.find_element_by_xpath("//button[@type='submit']")
    name.send_keys("Hui Lin")
    comment.send_keys("This is a comment!")
    submit_btn.click()
    assert "Hui Lin" in driver.page_source and "This is a comment!" in driver.page_source
    driver.close()
