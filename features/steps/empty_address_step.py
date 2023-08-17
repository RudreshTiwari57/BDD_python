from behave import *
from features.pageobject.empty_address_page import Empty_address
from utilities.logutil import Logger
import logging

log = Logger(__name__,logging.INFO)
@then(u'verify user gets empty address error message')
def step_impl(context):
    context.emty_address = Empty_address(context.driver)
    context.emty_address.verify_address_error_message()
    log.logger.info("verify user gets empty address error message")


