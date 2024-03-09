# Deploying Flask Application on Azure Web Apps

This repository contains a simple Flask application that can be deployed on Azure Web Apps. The application consists of a single endpoint that returns "Hello, Azure Web Apps!" when accessed.

## Application Setup

### Installation

To run the application locally, follow these steps:

1. Clone this repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd <project_directory>
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

### Running Locally

To run the application locally, execute the following command:

- For Flask:

    ```bash
    python app.py
    ```

This will start a development server, and you can access the application at `http://localhost:8000`.

## Azure Web App Deployment

### Prerequisites

Before deploying the application to Azure Web Apps, ensure you have the following:

- An Azure account
- Azure CLI installed on your machine ([Install Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli))

### Deployment Steps

1. Login to your Azure account using Azure CLI:

    ```bash
    az login
    ```

2. Create a resource group:

    ```bash
    az group create --name <resource_group_name> --location <location>
    ```

3. Create an Azure Web App:

    ```bash
    az webapp up --name <app_name> --resource-group <resource_group_name> --plan <app_service_plan_name> --sku <sku> --location <location>
    ```

4. Deploy the application to Azure Web App:

    ```bash
    git push azure master
    ```

## Accessing the Deployed Application

Once deployed, you can access the application at the URL provided by Azure Web Apps.

## Repository Structure

- `app.py`: Contains the Flask/FastAPI application code.
- `requirements.txt`: Lists the dependencies required by the application.

## Testing

To test the deployed application, simply access the URL of the Azure Web App in your web browser or use tools like cURL or Postman to make requests to the endpoint.

```bash
curl <azure_web_app_url>
```

You should receive a response "Hello, Azure Web Apps!" indicating that the application is running successfully.

## Contributors

- Soham Deshmukh(https://github.com/som-d)

Feel free to contribute to this project by creating issues or submitting pull requests.

For any questions or issues, please contact sohamdeshmukh611@gmail.com

Happy coding!
