from behave import *
from features.pageobject.empty_zipcode_page import Empty_zipcode
from utilities.logutil import Logger
import logging

log = Logger(__name__,logging.INFO)

@then(u'verify gets enter zipcode error message')
def step_impl(context):
    context.zipcode = Empty_zipcode(context.driver)
    context.zipcode.verify_zipcode_error_message()
    log.logger.info("verify gets enter zipcode error message")
