CREATE TABLE clients (
  client_id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  tax_details VARCHAR(255) NOT NULL,
  contact_details VARCHAR(255) NOT NULL
);

CREATE TABLE employees (
  employee_id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  role VARCHAR(255) NOT NULL
);

CREATE TABLE purchase_orders (
  purchase_order_id SERIAL PRIMARY KEY,
  client_id INTEGER REFERENCES clients(client_id),
  employee_id INTEGER REFERENCES employees(employee_id),
  description VARCHAR(255) NOT NULL,
  amount NUMERIC(10,2) NOT NULL,
  date DATE NOT NULL
);

CREATE TABLE timesheets (
  timesheet_id SERIAL PRIMARY KEY,
  purchase_order_id INTEGER REFERENCES purchase_orders(purchase_order_id),
  employee_id INTEGER REFERENCES employees(employee_id),
  date DATE NOT NULL,
  billable_hours INTEGER NOT NULL,
  non_billable_hours INTEGER NOT NULL,
  status VARCHAR(255) NOT NULL
);

CREATE TABLE invoices (
  invoice_id SERIAL PRIMARY KEY,
  purchase_order_id INTEGER REFERENCES purchase_orders(purchase_order_id),
  quote_id INTEGER REFERENCES quotes(quote_id),
  date DATE NOT NULL,
  amount NUMERIC(10,2) NOT NULL,
  status VARCHAR(255) NOT NULL
);

CREATE TABLE quotes (
  quote_id SERIAL PRIMARY KEY,
  purchase_order_id INTEGER REFERENCES purchase_orders(purchase_order_id),
  date DATE NOT NULL,
  amount NUMERIC(10,2) NOT NULL,
  status VARCHAR(255) NOT NULL
);

CREATE TABLE leave_applications (
  leave_application_id SERIAL PRIMARY KEY,
  employee_id INTEGER REFERENCES employees(employee_id),
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  reason VARCHAR(255) NOT NULL,
  status VARCHAR(255) NOT NULL
);

CREATE TABLE loans (
  loan_id SERIAL PRIMARY KEY,
  employee_id INTEGER REFERENCES employees(employee_id),
  amount NUMERIC(10,2) NOT NULL,
  purpose VARCHAR(255) NOT NULL,
  status VARCHAR(255) NOT NULL
);

CREATE TABLE personal_information (
  personal_information_id SERIAL PRIMARY KEY,
  employee_id INTEGER REFERENCES employees(employee_id),
  banking_details VARCHAR(255) NOT NULL,
  domicile VARCHAR(255) NOT NULL,
  next_of_kin VARCHAR(255) NOT NULL
);