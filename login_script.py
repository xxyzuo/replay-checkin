from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# 配置浏览器驱动（无头模式适合 GitHub Actions）
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 无界面运行
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

# 打开目标网站
driver.get('https://www.casino.org/replaypoker/')

# 等待登录按钮并点击（假设网站有类似的按钮）
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, 'Log in to Replay Poker'))
)
login_button.click()

# 等待用户名和密码输入框
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'username'))
)
password = driver.find_element(By.NAME, 'password')

# 从环境变量中读取用户名和密码（通过 GitHub Secrets 设置）
username.send_keys(os.getenv('USERNAME'))
password.send_keys(os.getenv('PASSWORD'))

# 点击登录按钮
login_submit = driver.find_element(By.XPATH, '//button[text()="Log in"]')
login_submit.click()

# 等待登录成功并领取奖励（具体操作需根据网站调整）
# 示例：点击“领取奖励”按钮
reward_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'claim-reward'))
)
reward_button.click()

# 关闭浏览器
driver.quit()
