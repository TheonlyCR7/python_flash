def test_login_success(selenium_driver):
    driver = selenium_driver
    driver.get('http://localhost:5000')

    # 打开登录模态框
    driver.find_element(By.CSS_SELECTOR, '.login a').click()

    # 填写表单
    driver.find_element(By.ID, 'username').send_keys('test@example.com')
    driver.find_element(By.ID, 'password').send_keys('validPass123')
    driver.find_element(By.ID, 'auth-code').send_keys('mocked_vcode')

    # 提交
    driver.find_element(By.CSS_SELECTOR, '.login-button').click()

    # 验证跳转
    WebDriverWait(driver, 5).until(
        EC.url_contains('/personal')
    )
    assert '个人中心' in driver.page_source