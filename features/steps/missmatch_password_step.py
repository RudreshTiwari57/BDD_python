from behave import *
from features.pageobject.missmatch_password_page import Empty_missmatch_password

from utilities.logutil import Logger
import logging

log = Logger(__name__,logging.INFO)
@then(u'verify user get password mismatch error')
def step_impl(context):
    context.missmatch_password = Empty_missmatch_password(context.driver)
    context.missmatch_password.verify_missmatch_password_error_message()
    log.logger.info("verify user get password mismatch error")
