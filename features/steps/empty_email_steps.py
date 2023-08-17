from behave import *
from features.pageobject.empty_email_page import Empty_email
from utilities.logutil import Logger
import logging

log = Logger(__name__,logging.INFO)

@then(u'verify user get enter email error message error')
def step_impl(context):
    context.empty_email = Empty_email(context.driver)
    context.empty_email.verify_email_error_message()
    log.logger.info("verify user get enter email error message error")
