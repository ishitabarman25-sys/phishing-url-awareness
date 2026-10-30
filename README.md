# Phishing URL Awareness

## Project Overview

Phishing URL Awareness is a Python-based cybersecurity project designed to analyze URLs and identify potentially suspicious characteristics.

The program examines user-provided URLs and displays warning signs that may indicate a phishing attempt. It is intended to promote awareness about suspicious links and encourage safe browsing practices.

## Features

- Accepts URLs from the user through the terminal.
- Detects IP-address-based hostnames.
- Identifies the use of HTTP.
- Displays warning signs for suspicious URLs.
- Provides a warning message to users.
- Supports repeated URL testing.
- Allows the user to exit the program using `q`.

## Technologies Used

- Python
- Visual Studio Code
- Git
- GitHub

## Project Structure

```text
phishing-url-awareness/
├── phishing_checker.py
├── requirements.txt
├── README.md
├── tests/
│   └── test_samples.md
└── screenshots/
    ├── test_ip_address_url.png
    ├── test_safe_url.png
    └── test_suspicious_url.png
```

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd phishing-url-awareness
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## How to Run

Execute the following command in the terminal:

```bash
python phishing_checker.py
```

Enter a URL when prompted.

To exit the program, enter:

```text
q
```

## Testing

The program was tested using different URL patterns.

| Test Case | Expected Behavior | Actual Result |
|---|---|---|
| IP address URL | Detect IP-based hostname and HTTP | 2 warning signs detected |
| Suspicious-looking URL | Detect applicable warning signs | 1 warning sign detected |
| Familiar HTTPS website | Display no listed warning signs | 0 warning signs detected |

Detailed test cases are available in `tests/test_samples.md`.

## Screenshots

Screenshots demonstrating the program's execution and test results are available in the `screenshots` directory.

## Disclaimer

This project is developed for educational and cybersecurity awareness purposes.

The program identifies selected URL characteristics that may indicate suspicious activity. It does not guarantee that a website is safe or malicious.

Users should exercise caution when opening unfamiliar links and should never enter sensitive information on untrusted websites.

## Author

Developed as a Python cybersecurity awareness project.