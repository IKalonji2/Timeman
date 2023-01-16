from flask import Blueprint

manager_blueprint = Blueprint('manager', __name__)

@manager_blueprint.route('/review-overtime-request/')
def review_overtime_request():
    """
    Data transfer contract:
    {
        "employeeId": "",
        "overtimeDate": "",
        "status": "",
        "reason": ""
    }
    """
    pass

@manager_blueprint.route('/review-timesheet/')
def review_timesheet():
    """
    Data transfer contract:
    {
        "timesheetId": "",
        "status": "",
    }
    """
    pass

@manager_blueprint.route('/review-quote/')
def review_quote():
    """
    Data transfer contract:
    {
        "quoteId": "",
        "status": "",
    }
    """
    pass

@manager_blueprint.route('/create-invoice/<quote_id>')
def create_invoice(quote_id):
    """
    Quote ID to be provided in the URL params to generate an invoice from the 
    quote details contained in the Database.
    """
    pass

@manager_blueprint.route('/review-leave-request/')
def review_leave_request():
    """
    Data transfer contract:
    {
        "leaveApplicationId": "",
        "status": "",
    }
    """
    pass

@manager_blueprint.route('/review-loan-request/')
def review_loan_request():
    """
    Data transfer contract:
    {
        "loan_id": "",
        "status": "",
    }
    """
    pass

@manager_blueprint.route('/download-invoice/<invoice_id>')
def download_invoice(invoice_id):
    """
    Invoice ID to be provided in the URL params, PDF will be generated,
    and linked in the response.
    """
    pass

@manager_blueprint.route('/download-quote/<quote_id>')
def download_quote(quote_id):
    """
    Quote ID to be provided in the URL params, PDF will be generated,
    and linked in the response.
    """
    pass

