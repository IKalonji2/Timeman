from flask import Flask, request, json, jsonify
from flask_cors import CORS

from modules.routes.admin_routes import admin_blueprint
from modules.routes.manager_routes import manager_blueprint
from modules.routes.employee_routes import employee_blueprint
from modules.routes.reporting_routes import reporting_blueprint

app = Flask(__name__)

app.register_blueprint(admin_blueprint, url_prefix='/admin')
app.register_blueprint(manager_blueprint, url_prefix='/manager')
app.register_blueprint(employee_blueprint, url_prefix='/employee')
app.register_blueprint(reporting_blueprint, url_prefix='/reporting')

if __name__== "__main__":
    app.run()