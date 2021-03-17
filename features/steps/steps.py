from selenium import webdriver
import selenium
import os
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys

chromedriver = '/usr/local/bin/chromedriver'
browser = webdriver.Chrome(chromedriver)

@given('I go to "{url}"')
def step(context,url):
	browser.get(url)


@when('we visit google')
def step(context):
   browser.get('http://www.google.com')

@then('it should have a title "{title}"')
def step(context, title):
   assert browser.title == title

@when('I click "{button}"')
def step(context,button):
	browser.find_element_by_css_selector(button).click()

@then('I book a ticket from "{from_code}" to "{to_code}"')
def step(context,from_code, to_code):
	field = browser.find_element_by_css_selector("#input-button__departure").click()
	sleep(float(3))
	browser.find_element_by_css_selector("#input-button__departure.input-button__input").clear()
	from_ = browser.find_element_by_css_selector("#input-button__departure.input-button__input")
	from_.send_keys(from_code)
	sleep(float(5))
	to_ = browser.find_element_by_css_selector('div.input-button__content[data-ref=input-button__destination] > input#input-button__destination.input-button__input').click()
	to_ = browser.find_element_by_css_selector('input#input-button__destination')
	sleep(float(5))
	to_.send_keys(to_code)
	sleep(float(5))
	browser.find_element_by_css_selector("span[data-ref=airport-item__name]").click()

	

@then('I choose the date "{date}"')
def step(context, date):
	browser.find_element_by_css_selector("div.flight-widget-controls__calendar.ng-tns-c76-4.ng-trigger.ng-trigger-datesContainerInitialRender").click()
	sleep(float(2))
	browser.find_element_by_css_selector("[data-id='"+date+"']").click()
	sleep(float(3))
	

@then('I choose {adults} adults and {child} child')
def step(context, adults, child):
	browser.find_element_by_css_selector("[data-ref='input-button__passengers']").click()
	sleep(float(5))
	if int(adults) >= 2:
		browser.find_element_by_css_selector("[data-ref='counter.counter__increment']").click()
		sleep(float(5))

@then('I click "{css}"')
def step(context,css):
	browser.find_element_by_css_selector(css).click()

@given('I am in itinerary page')
def step(context):
	# assert browser.title == "Ryanair"
	pass	

@then('I click on an option')
def step(context):
	sleep(float(5))
	browser.find_element_by_css_selector("div.card-price").click()
	sleep(float(5))	
	browser.find_element_by_css_selector("[data-e2e='fare-card--standard']").click()
	sleep(float(5))	

@then('I click on login later')
def step(context):
	browser.find_element_by_css_selector(".login-touchpoint__expansion-bar").click() 
	sleep(float(5))	
	# pass	

@when('I write first passenger "{first_name}" and "{last_name}" and "{title}"')
def step(context, first_name, last_name, title):
	fname = browser.find_element_by_css_selector("input[name='formState.passengers.ADT-0.name']")
	fname.send_keys(first_name)
	lname = browser.find_element_by_css_selector("input[name='formState.passengers.ADT-0.surname']")
	lname.send_keys(last_name)
	browser.find_element_by_css_selector("button.dropdown__toggle").click()
	browser.find_element_by_css_selector(title).click()
	sleep(float(5))	

@when('I write secnd passenger "{first_name}" and "{last_name}" and "{title}"')
def step(context, first_name, last_name, title):
	fname = browser.find_element_by_css_selector("[name='formState.passengers.ADT-1.name']")
	fname.send_keys(first_name)
	lname = browser.find_element_by_css_selector("[name='formState.passengers.ADT-1.surname']")
	lname.send_keys(last_name)
	sleep(float(5))
	browser.find_element_by_css_selector("button.dropdown__toggle").click()
	browser.find_element_by_css_selector(title).click()
	sleep(float(10))	
	# pass

@then('I select seat in row {number}')
def step(context, number):
	browser.find_element_by_css_selector(".seatmap__seatrow--"+number+" > button.seatmap__seat--priority")
	pass	

@then('I close the browser')
def step(context):
	browser.quit()

@then('I wait {sec}')
def step(context,sec):
	sleep(float(sec))
