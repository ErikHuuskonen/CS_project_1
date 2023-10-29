# University of Helsinki's Cyber Security Base 2023 - Project 1

This is the project 1 for the University of Helsinki's Cyber Security Base 2023 course. The purpose of this Django project is to practice identifying OWASP vulnerabilities and other software vulnerabilities and to correct them. This application is created purely for this purpose and is not maintained at all.

## Download the Project

1. Navigate to the GitHub repository where your Django project is located.
2. Click the "Code" button and copy the URL.
3. Open your command line or terminal and type:

```bash
git clone [copied URL]
```

For example:

```bash
git clone https://github.com/username/project_name.git
```

## Navigate to the Project Folder

```bash
cd project_name
```

## Create a Virtual Environment (recommended)

### For Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### For Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```

## Install Required Dependencies

Make sure you have a `requirements.txt` file in your repository that contains all the necessary packages.

```bash
pip install -r requirements.txt
```

## Run Migrations

```bash
python manage.py migrate
```

## Start the Development Server

```bash
python manage.py runserver
```

Once the server is running, navigate to http://127.0.0.1:8000/ in your browser to see your project in action.

## Stop the Development Server

Press `Ctrl + C` in your command line or terminal.

## Exit the Virtual Environment (if you used one)

```bash
deactivate
```
Please ensure to replace placeholders like [copied URL], username, and project_name with your actual values before saving and publishing.
