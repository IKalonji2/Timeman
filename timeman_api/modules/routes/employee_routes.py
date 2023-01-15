from flask import Blueprint

employee_blueprint = Blueprint('employee', __name__)

@employee_blueprint.route('/upload-timesheet/')
def upload_timesheet():
    """do waht you need to do"""
    pass

@employee_blueprint.route('/generate-timesheet/')
def generate_timesheet():
    """do waht you need to do"""
    pass

@employee_blueprint.route('/billed-time/')
def get_billed_time():
    """do waht you need to do"""
    pass

@employee_blueprint.route('/admin-request/')
def submit_admin_request():
    """do waht you need to do"""
    pass

@employee_blueprint.route('/my-details/')
def get_personal_information():
    """do waht you need to do"""
    pass