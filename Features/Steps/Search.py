from behave import *
from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import  time

@given(u'I got nevigated to home page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")
    time.sleep(3)


@when(u'I enter the valid product in the search box')
def step_impl(context):
    context.driver.find_element(By.NAME,"search").send_keys("HP")
    time.sleep(3)

@when(u'I click on search button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
    time.sleep(3)

@then(u'Valid product should be displayed')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
    time.sleep(5)
    context.driver.quit()

@when(u'I enter the invalid product in the search box')
def step_impl(context):
    print("hi")

@then(u'Proper message should be displayed in search results')
def step_impl(context):
    print("hi")