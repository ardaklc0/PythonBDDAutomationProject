# Build and Run Instructions

## Prerequisites
- Python 3.x installed
- Chrome or Firefox browser installed

## Setup

1.  **Create a Virtual Environment** (Recommended)
    ```bash
    python -m venv venv
    ```

2.  **Activate the Virtual Environment**
    - Windows:
      ```powershell
      .\venv\Scripts\Activate.ps1
      ```
    - macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Running Tests

### Run Behave Features
To run BDD scenarios using Behave:
```bash
behave
```
To run with a specific browser (using userdata):
```bash
behave -D browser=firefox
```
