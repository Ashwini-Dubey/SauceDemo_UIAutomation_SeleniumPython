# End-to-End Testing Project with Selenium and Pytest

## Overview
This project is an end-to-end testing framework for a web application using Selenium and Pytest. It employs a page object model to encapsulate web elements and operations within classes for better maintainability and readability. The framework can be extended for various tests and configurations.

## Prerequisites
- Python (3.8+)
- Selenium WebDriver
- Pytest
- WebDriver for the chosen browser (Chrome, Firefox, Safari)

## Setup
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   

2. **Set up a virtual environment (optional):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Run Tests:** You can run the tests using pytest. You can specify the browser name through the CLI using --browser_name option.
    ```bash
    pytest --browser_name <browser_name>

5. **Test Reports:** You can run the tests using pytest. You can specify the --html=reports.html through the CLI for the HTML reports.
    ```bash
    pytest --browser_name <browser_name> --html=report.html
