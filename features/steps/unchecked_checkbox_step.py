import time

from behave import *
from features.pageobject.uncheck_checkbox_page import Unchecked_checkbox
from utilities.logutil import Logger
import logging

log = Logger(__name__,logging.INFO)

@then(u'verify user should get agree privay policy error')
def step_impl(context):
    context.unchecked_checkbox = Unchecked_checkbox(context.driver)
    context.unchecked_checkbox.verify_uncheckeb_checkbox_error_message()
    log.logger.info("verify user should get agree privay policy error")

