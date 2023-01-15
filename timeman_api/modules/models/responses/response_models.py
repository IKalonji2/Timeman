from dataclasses import dataclass

@dataclass
class timesheet_upload_response_success():
    employee_number: str
    result: str
    