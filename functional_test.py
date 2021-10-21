from selenium import webdriver

browser = webdriver.Edge('E:\\Ki 1 nam 3\\Tester\\Prak3\\edgedriver_win64\\msedgedriver.exe')
browser.get('http://localhost:8000')

assert 'successfully' in browser.title