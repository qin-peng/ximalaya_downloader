from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
# run Chrome in headless mode
# (without any graphical user interface)
options.headless = True
# https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.desired_capabilities.html
capabilities = webdriver.DesiredCapabilities.CHROME.copy()
capabilities["goog:loggingPrefs"] = {"performance": "ALL"}


DRIVER_PATH = '/usr/local/bin/chromedriver'
#driver = webdriver.Chrome(executable_path = DRIVER_PATH, desired_capabilities = capabilities)
#driver = webdriver.Chrome(options=options, desired_capabilities = capabilities, executable_path = DRIVER_PATH)
#driver.get('https://passport.ximalaya.com/page/web/login')
# https://chromedriver.chromium.org/logging/performance-log
# ChromeDriver supports performance logging,
# from which you can get events of domains "Timeline", "Network", and "Page",
# as well as trace data for specified trace categories.
# https://www.rkengler.com/how-to-capture-network-traffic-when-scraping-with-selenium-and-python/



# give enough time to login
#time.sleep(100)
# The driver.page_source will return the full page HTML code
#print(driver.page_source)
#driver.get('https://www.ximalaya.com/youshengshu/12868137/')
#logs = driver.get_log("performance")
#list_to_file(logs, 'logs.txt')
#driver.quit()


#driver.get('https://www.ximalaya.com/youshengshu/12868137/')

#album_url = 'https://www.ximalaya.com/youshengshu/12868137/'  # 美国的故事
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0',
#                   'Connection': 'keep-alive'}
# 获得专辑中的节目列表
# Get audio list from given album
#session = requests.session()
#response = session.get(album_url, headers = headers)
#soup = BeautifulSoup(response.content, 'html.parser')