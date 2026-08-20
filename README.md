# cici-web

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/deploy?template=https://github.com/cicirailway/cici-web)

A simple web application built with Python and Flask.

## Features

- Clean and responsive user interface
- Easy to deploy on Railway

## Tech Stack

- Python 3.9+
- Flask
- Other dependencies listed in `requirements.txt`

## Local Development

### Prerequisites

- Python 3.9 or higher
- pip

### Setup

1. Clone the repository:

```bash
git clone https://github.com/cicirailway/cici-web.git
cd cici-web
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application locally:

```bash
python app.py
```

The application will be available at `http://localhost:5000`.

---

## Deploy to Railway

[Railway](https://railway.app/) provides a simple and fast way to deploy web applications. Follow the steps below to deploy this project.

### 1. Fork or Use the Repository

Make sure you have a copy of this repository. You can fork it or use the original source.

**Source Repository**: `https://github.com/cicirailway/cici-web`

### 2. Create a New Project on Railway

- Log in to your [Railway](https://railway.app/) account.
- Click **New Project**.
- Select **Deploy from GitHub repo**.
- Choose the repository (`cicirailway/cici-web` or your forked version).

### 3. Configure Deployment Settings

Railway will automatically detect the Python project, but you need to set the following build and start commands:

#### Build Command

```bash
pip install -r requirements.txt
```

#### Start Command

```bash
python app.py
```

You can set these in the Railway dashboard under the **Settings** tab of your service, or by adding a `railway.json` file in the root of your project:

```json
{
  "build": {
    "builder": "NIXPACKS",
    "buildCommand": "pip install -r requirements.txt"
  },
  "deploy": {
    "startCommand": "python app.py",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### 4. Configure Networking

- Under the **Networking** section of your service, enable **Public Networking**.
- Railway will automatically generate a domain for your service (e.g., `cici-web.up.railway.app`).
- The application listens on **port 5000** (default Flask port). Railway will map external requests to this internal port.

### 5. Deploy

Railway will automatically trigger a deployment when you push changes to the repository. You can also manually deploy via the **Deploy** button in the dashboard.

Once deployed, your application will be accessible at the generated domain.

---

## Environment Variables (if any)

If your application requires environment variables (e.g., API keys, database URLs), add them in the Railway dashboard under the **Variables** tab.

---

## Project Structure

```
cici-web/
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── templates/           # HTML templates (if any)
└── README.md            # This file
```
