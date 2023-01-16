from flask import Blueprint

employee_blueprint = Blueprint('employee', __name__)

@employee_blueprint.route('/upload-timesheet/')
def upload_timesheet():
    """
    Data transfer contract:
    {
        "employeeId": "",
        "clientId":"",
        "file":"",
        "date": "",
    }
    """
    pass

@employee_blueprint.route('/generate-timesheet/<employee_id>/<period>')
def generate_timesheet(employee_id, period):
    """
    Employee ID and period for which to generate are provided in the request URL
    """
    pass

@employee_blueprint.route('/billed-time/<employee_id>/<period>/<format>')
def get_billed_time():
    """
    Employee ID, period, and format of the required output (Weekly, Monthly, Annual)
    is provided in the URL parameters.
    """
    pass

@employee_blueprint.route('/admin-request-leave/')
def submit_leave_request():
    """
    Data transfer contract:
    {
        "employeeId": "",
        "startDate": "",
        "endDate": "",
        "reason": ""
    }
    """
    pass

@employee_blueprint.route('/admin-request-loan/')
def submit_loan_request():
    """
    Data transfer contract:
    {
        "employeeId": "",
        "amount": "",
        "purpose": "",
    }
    """
    pass

@employee_blueprint.route('/my-details/<employee_id>')
def get_personal_information():
    """
    Employee ID should be provided as a URL parameter.
    """
    pass