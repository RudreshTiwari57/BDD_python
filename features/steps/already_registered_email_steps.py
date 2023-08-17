
from selenium import webdriver
from features.pageobject.already_registered_email_page import Already_registerd_mail
from behave import *
from utilities.logutil import Logger
import logging

log = Logger(__name__,logging.INFO)

@given(u'you are on the home page')
def step_impl(context):
    context.ARE_email = Already_registerd_mail()
    context.driver = context.ARE_email.get("CHROME")
    log.logger.info("You are on home page")

@given(u'nagivate to login page')
def step_impl(context):
    context.ARE_email.nagavite()
    log.logger.info("You nagivate to login page")


@then(u'verify user is on login page')
def step_impl(context):
    context.ARE_email.verify_loginpage()
    log.logger.info("verify user is on login page")


@when(u'user click on register account radio button')
def step_impl(context):
    context.ARE_email.click_radiobutton()
    log.logger.info("user click on register account radio button")


@when(u'clicks on continue button')
def step_impl(context):
    context.ARE_email.click_continue()
    log.logger.info("clicks on continue button")


@then(u'verify user is on registration page')
def step_impl(context):
    context.ARE_email.verify_registration()
    log.logger.info("verify user is on registration page")


@when(u'user enters first name "{firstname}"')
def step_impl(context,firstname):
    context.ARE_email.enter_firstname(firstname)
    log.logger.info("user enters first name")

@when(u'user enters last name "{lastname}"')
def step_impl(context,lastname):
    context.ARE_email.enter_lastname(lastname)
    log.logger.info("user enters last name")

@when(u'user enters Email "{email}"')
def step_impl(context,email):
    context.ARE_email.enter_email(email)
    log.logger.info("user enters Email")


@when(u'user enters telephone "{telephone}"')
def step_impl(context,telephone):
    context.ARE_email.enter_telephone(telephone)
    log.logger.info("user enters telephone")


@when(u'user enters fax "{fax}"')
def step_impl(context,fax):
    context.ARE_email.enter_fax(fax)
    log.logger.info("user enters fax")


@when(u'user enters company "{company}"')
def step_impl(context,company):
    context.ARE_email.enter_comapnyname(company)
    log.logger.info("user enters first name")


@when(u'user enters first address "{first_addresss}"')
def step_impl(context,first_addresss):
    context.ARE_email.enter_address_1(first_addresss)
    log.logger.info("user enters first address")



@when(u'user enters second address  "{second_address}"')
def step_impl(context,second_address):
    context.ARE_email.enter_address_2(second_address)
    log.logger.info("user enters second address")


@when(u'user enters city "{city}"')
def step_impl(context,city):
    context.ARE_email.enter_city(city)
    log.logger.info("user enters city")


@when(u'user selects country "{country}"')
def step_impl(context,country):
    context.ARE_email.select_country(country)
    log.logger.info("user selects country ")

@when(u'user selects state "{state}"')
def step_impl(context,state):
    context.ARE_email.select_state(state)
    log.logger.info("user selects state")

@when(u'user enters ZIP code "{zipcode}"')
def step_impl(context,zipcode):
    context.ARE_email.enter_zip_code(zipcode)
    log.logger.info("user enters ZIP code")

@when(u'user enters login name "{loginname}"')
def step_impl(context,loginname):
    context.ARE_email.enter_loginname(loginname)
    log.logger.info("user enters login name")

@when(u'user enters password "{password}"')
def step_impl(context,password):
    context.ARE_email.enter_password(password)
    log.logger.info("user enters password")


@when(u'user enters confirm password "{confirmpassword}"')
def step_impl(context,confirmpassword):
    context.ARE_email.enter_confirmpassword(confirmpassword)
    log.logger.info("user enters confirm password")


@when(u'user checks the check box')
def step_impl(context):
    context.ARE_email.click_policyagrement()
    log.logger.info("user checks the check box")

@then(u'verify user check the check box')
def step_impl(context):
    context.ARE_email.verify_checkbox()
    log.logger.info("verify user check the check box")

@then(u'click on continue button')
def step_impl(context):
    context.ARE_email.click_registration_continue()
    log.logger.info("click on continue button")

@then(u'verify user gets mail already registered error message')
def step_impl(context):
    context.ARE_email.verify_registration_error()
    log.logger.info("user gets mail already registered error message")

