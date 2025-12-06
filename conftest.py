from selenium import webdriver
import pytest
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    #Vamos al incognito
    options = Options()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options = options)
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver, usuario, password):
    LoginPage(driver).abrir_pagina().login_completo(usuario, password)
    return driver

@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"

@pytest.fixture
def header_request():
    return {"x-api-key": "reqres-free-v1"}