from selenium.webdriver import Chrome
    
def before_scenario(context, scenario):
	chromedrive = '/usr/local/bin/chromedriver'
    context.driver = Chrome(chromedrive)
    
def after_scenario(context, scenario):    
    context.driver.quit()