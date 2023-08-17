from behave import *
from features.pageobject.unavilable_loginname_page import Unavilable_loginname

from utilities.logutil import Logger
import logging

log = Logger(__name__,logging.INFO)
@then(u'user should get unavaliable loginname error')
def step_impl(context):
    context.unavilable_loginname = Unavilable_loginname(context.driver)
    context.unavilable_loginname.verify_unavilable_loginname_error_message()
    log.logger.info("user should get unavaliable loginname error")
