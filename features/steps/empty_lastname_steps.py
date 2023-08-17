from behave import *
from features.pageobject.empty_lastname_page import Empty_lastname

from utilities.logutil import Logger
import logging

log = Logger(__name__,logging.INFO)
@then(u'verify user gets enter last name error')
def step_impl(context):
    context.empty_lastname = Empty_lastname(context.driver)
    context.empty_lastname.verify_last_error_message()
    log.logger.info("verify user gets enter last name error")


