from behave import *
from features.pageobject.succesfull_login_page import Succesfull_login

from utilities.logutil import Logger
import logging

log = Logger(__name__,logging.INFO)
@then(u'verify successfull registration of the user')
def step_impl(context):
    context.successfull_login = Succesfull_login(context.driver)
    context.successfull_login.verify_missmatch_password_error_message()
    log.logger.info("verify successfull registration of the user")
