# Job Search Automation System

## Overview
This project automates the process of searching for jobs and sending daily updates via email. It allows users to configure email settings and API keys to customize their job search experience.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/xhuang1998-blip/Job-Searching-2026.git
   cd Job-Searching-2026
   ```

2. **Install Dependencies**:
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration Steps
1. **Set Up Email Configuration**:
   - Open the `config.py` file.
   - Update the following variables with your email settings:
     ```python
     EMAIL_ADDRESS = 'your_email@example.com'
     EMAIL_PASSWORD = 'your_password'
     ```

2. **Set Up API Keys**:
   - In `config.py`, set your API keys for job platforms:
     ```python
     JOB_API_KEY = 'your_api_key'
     ```

## Daily Job Posting Emails
Once configured, the system will automatically search for job postings daily. 
- **Email Notifications**: You will receive an email with the latest job postings each day at 9 AM. Make sure your `EMAIL_ADDRESS` and `EMAIL_PASSWORD` are correctly configured to receive these emails.

### Important Notes:
- Ensure that your email provider allows less secure apps (if required) to send emails.
- If you encounter any issues, check the configuration files and validate your API keys and email credentials.

## Contributing
If you would like to contribute, feel free to open a pull request or raise an issue.

## License
This project is licensed under the MIT License.