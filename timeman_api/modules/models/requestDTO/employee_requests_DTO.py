from dataclasses import dataclass

@dataclass
class timesheet_upload_request():
    employee_number: str
    timesheet_csv: None