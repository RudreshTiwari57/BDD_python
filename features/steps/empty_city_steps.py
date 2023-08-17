from behave import *
from features.pageobject.empty_city_page import Empty_city
from utilities.logutil import Logger
import logging

log = Logger(__name__,logging.INFO)
@then(u'verify user gets empy city error message')
def step_impl(context):
    context.empty_city = Empty_city(context.driver)
    context.empty_city.verify_empty_city_error_message()
    log.logger.info("verify user gets empy city error message")
