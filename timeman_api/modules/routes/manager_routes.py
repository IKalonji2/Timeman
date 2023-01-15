from flask import Blueprint

manager_blueprint = Blueprint('manager', __name__)

@manager_blueprint.route('/review-overtime-request/')
def review_overtime_request():
    """do waht you need to do"""
    pass

@manager_blueprint.route('/review-timesheet/')
def review_timesheet():
    """do waht you need to do"""
    pass

@manager_blueprint.route('/review-quote/')
def review_quote():
    """do waht you need to do"""
    pass

@manager_blueprint.route('/create-invoice/')
def create_invoice():
    """do waht you need to do"""
    pass

@manager_blueprint.route('/review-leave-request/')
def review_leave_request():
    """do waht you need to do"""
    pass

@manager_blueprint.route('/review-loan-request/')
def review_loan_request():
    """do waht you need to do"""
    pass

@manager_blueprint.route('/download-invoice/')
def download_invoice():
    """do waht you need to do"""
    pass

@manager_blueprint.route('/download-quote/')
def download_quote():
    """do waht you need to do"""
    pass

