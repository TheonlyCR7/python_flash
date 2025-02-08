# tests/test_ui.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_user_login_ui(driver):
    # 打开登录页面
    driver.get("http://localhost:5000/login")
    assert "登录" in driver.title

    # 输入用户名和密码
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    username_input.send_keys("test@example.com")
    password_input.send_keys("password123")

    # 点击登录按钮
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # 检查是否登录成功
    assert "登录成功" in driver.page_source
