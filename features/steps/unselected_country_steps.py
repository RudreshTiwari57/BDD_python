import time
from behave import *
from features.pageobject.unselected_country_page import Unselected_country
from utilities.logutil import Logger
import logging

log = Logger(__name__,logging.INFO)

@then(u'verify user gets unselected city error message')
def step_impl(context):
    context.unselected_country = Unselected_country(context.driver)
    context.unselected_country.verify_unselected_country_error_message()
    log.logger.info("verify user gets unselected city error message")

