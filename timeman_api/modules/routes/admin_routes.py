from flask import Blueprint

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/create-client/')
def create_client():
    """
    Data transfer contract:
    {
        "entity": "",
        "address":"",
        "taxRef":"",
        "contactNumber": "",
        "correspondent": "",
        "correspondentEmail": "",
        "clientEmailGeneral": ""
    }
    """
    pass

@admin_blueprint.route('/create-employee/')
def create_employee():
    """
    Data transfer contract:
    {
        "employeeName": "",
        "idNumber":"",
        "taxRef":"",
        "contactNumber": "",
        "emailAddr": "",
        "nextOfKin": "",
        "nextOfKindContactNumber": "",
        "nextOfKinEmail": "",
        "Domicili":""
    }
    """
    pass

@admin_blueprint.route('/capture-po/')
def capture_purchase_order():
    """
    Data transfer contract:
    {
        "employeeId": [""],
        "clientId":"",
        "amount":"",
        "description": "",
        "date": "",
    }
    """
    pass

@admin_blueprint.route('/capture-adhoc-po/')
def capture_adhoc_purchase_order():
    """
    Data transfer contract:
    {
        "employeeId": "",
        "clientId":"",
        "amount":"",
        "description": "",
        "reason":""
        "date": "",
    }
    """
    pass