from behave import *
from features.pageobject.empty_firstname_page import Empty_firstname

from utilities.logutil import Logger
import logging

log = Logger(__name__,logging.INFO)

@then(u'verify user gets enter user name error')
def step_impl(context):
    context.firstname = Empty_firstname(context.driver)
    context.firstname.verify_firstname_error_message()
    log.logger.info("verify user gets enter user name error")
