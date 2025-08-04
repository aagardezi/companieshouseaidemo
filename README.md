# Companies House AI Demo

This is a Streamlit application that uses Google's Gemini Pro model via Vertex AI to interact with the UK Companies House API. It allows users to ask questions in natural language about companies, and the application uses Gemini's function calling capabilities to retrieve information from the Companies House API.

## Features

-   Chat-based interface powered by Streamlit.
-   Natural language understanding via Google's Gemini Pro model.
-   Function calling to interact with the Companies House API to:
    -   Search for companies.
    -   Get company profiles.
    -   Get company officers.
    -   Get company filing history.

## Prerequisites

Before you begin, ensure you have the following:

-   Python 3.12 or later.
-   [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) (`gcloud` CLI) installed and configured.
-   A Google Cloud Platform project with billing enabled.
-   The **Vertex AI API** enabled in your GCP project.
-   A **Companies House Developer API Key**.

## Getting a Companies House API Key

1.  Navigate to the Companies House developer portal.
2.  Click on **Register** and create an account if you don't have one.
3.  Once logged in, go to **Your applications**.
4.  Click **Register an application**.
5.  Fill in the application details. For local development, you can use `http://localhost` for the website URL.
6.  Once the application is created, you will see your API key. Copy it, as you will need it for the setup.

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/aagardezi/companieshouseaidemo.git
cd companieshouseaidemo
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
# On Windows, use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up authentication

-   **Companies House API Key**: Set the API key as an environment variable. Replace `YOUR_COMPANIES_HOUSE_API_KEY` with the key you obtained.

    ```bash
    # For Linux/macOS
    export COMPANIES_HOUSE_API_KEY="YOUR_COMPANIES_HOUSE_API_KEY"

    # For Windows (Command Prompt)
    set COMPANIES_HOUSE_API_KEY="YOUR_COMPANIES_HOUSE_API_KEY"
    ```

-   **Google Cloud**: Authenticate the `gcloud` CLI. This will allow the application to use your GCP credentials for Vertex AI.

    ```bash
    gcloud auth application-default login
    ```
    This command will open a browser window for you to log in to your Google account.

### 5. Run the Streamlit application

```bash
streamlit run main.py
```

The application should now be running and accessible at `http://localhost:8501`.

## Deploying to Google Cloud Run

This application is containerized and can be deployed as a serverless application on Google Cloud Run.

### 1. Set up your GCP environment

Make sure you have the `gcloud` CLI installed and authenticated. Set your project ID and region variables.

```bash
export PROJECT_ID="your-gcp-project-id"
export REGION="us-central1" # Or your preferred region

gcloud config set project $PROJECT_ID
gcloud config set run/region $REGION
```

### 2. Enable required Google Cloud APIs

```bash
gcloud services enable run.googleapis.com cloudbuild.googleapis.com aiplatform.googleapis.com
```

### 3. Deploy to Cloud Run

The following command uses Cloud Build to build the Docker image from the `Dockerfile` and then deploys it to Cloud Run.

You must provide the Companies House API key as an environment variable during deployment.

```bash
gcloud run deploy companieshouse-ai-demo \
  --source . \
  --platform managed \
  --allow-unauthenticated \
  --set-env-vars="COMPANIES_HOUSE_API_KEY=YOUR_COMPANIES_HOUSE_API_KEY"
```

-   Replace `companieshouse-ai-demo` with your desired service name.
-   Replace `YOUR_COMPANIES_HOUSE_API_KEY` with your actual key.
-   The `--allow-unauthenticated` flag makes the service publicly accessible. Remove this flag if you want to control access using IAM.

After the deployment is complete, `gcloud` will provide you with the URL to access your application.