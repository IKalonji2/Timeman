# Welcome to Timeman Documentation

For full documentation visit [timeman.org](https://www.timeman.org).

## About Timeman

Timeman is a modern and efficient time and invoice management tool build by Timeman systems. The project allows contractors and employees within the company to easily capture timesheets, generate payslips, client billing invoices and analytics.

## Project layout

    Timeman (Main directory)

        timeman-app # Angular frontend application

        timeman_api # Python (Flask) backend api

        timeman_docs # MKDocs project documentation builder

## Getting started

### Project installation

Clone the repository

    $git clone https://github.com/IKalonji2/Timeman.git
    $cd Timeman

Build the timeman_api Flask project

    $cd timeman_api # change directory

    $pip install -r requirements.txt # install required packages

    $docker build -t <give-the-image-a-name> . # build a docker image for the backend api

    $docker run -p 8080:8080 <name-you-gave-your-image>

Build the timeman_app Angular project

    $cd timeman-app # change directory

    $npm install # install required packages

    $docker build -t <give-the-image-a-name> . # build a docker image for the backend api

    $docker run -p 9090:9090 <name-you-gave-your-image>

The project should now be running Docker containers locally

### Updating configurations

By default the Docker images running from the above step are all local. To test against live deployed environments e.g live database in the Development staging, Integration staging and Production environments, you would be required to update the configuration files.

#### Angular app (timeman-app) configuration updates

Locate the environments folder in the project root:

    environments # environments folder
        
        environments.production.ts

        environments.integration.ts

        environments.development.ts

        environments.local.ts

Open the respective environment file where you would like to make updates and update the properties according to your requirement.

Example:

    environment = {
        prod: true,
        environ: "prod",
        mainUrl: "https://backend.timeman.org/",
        loginRequired: false, # change the value if needed.
    }

#### Flask app (timeman_api) configuration updates

Locate the configuration.json file in the project root:

    timeman_api/

        some_module/

        another_module/

        main.py

        configuration.json

Open the file and update the properties according to your requirement.

Example:

    {
        "DB_connection_string": "https://backend.timeman.org/",
        "DB_user": "Some User",
        "DB_user_password": "db password", # change the value if needed.
    }

Now you can proceed to run the application/s with your updated configuration.

## Documentation Usage

The Timeman documentation is continuously updated based on the Development environment and is the single source of truth with regards to the current application layout, functionality, and project breakdown and any changes being developed. If you're ever in doubt, consult these documentation, if you have not found the answer you were looking for, please raise a ticket below with details of the information require:

[Log Documentation Request](https://documentation.timeman.org/request-update)

Requests should be verbose and detailed enough for the Docs team to understand, be clear and concise! 

Example:

    {
        type: "MoreDetailRequired",
        application: "timeman-app",
        drilldown: {
            module: "name of the module", 
            submodule: "sub1/sub2" # if submodules are nested, separate with "/"
            component: "name of the component" # Component is only applicable to the Angular app, skip if logging to timeman_api
            file:["file1","file2"] 
        },
        requirement: "Here you will provide details of your documentation requirement/update/missing docs etc."
    }

Acceptable request type options: 

* MissingInfo
* MoreDetailRequired
* UpdateDocs
* OutdatedInfo
* IncorrectInfo
* Misc # This option should only be used as a matter of last resort, if your request type does not fall into the above options












