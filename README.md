
```markdown
# Pinterest Automation

## Overview

This project automates interactions with Pinterest using Selenium WebDriver. It includes functionality for checking UI elements, performing login and search operations, and managing messages. The automation script is designed to run in a headless Chrome browser.

## Features

- **UI Element Visibility:** Verify the presence of key UI elements such as logos, buttons, and links.
- **Login Functionality:** Test login with various scenarios including valid and invalid credentials.
- **Search Operation:** Perform searches on Pinterest and validate results.
- **Message Management:** Check for new SMS notifications, read the last message, and send SMS.
- **Screenshots:** Capture screenshots for certain actions and errors.

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Hasiburshanto/pinterest-automation.git
   cd pinterest-automation
   ```

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Credentials**

   Ensure your `config/credentials.py` file contains your Pinterest credentials:

   ```python
   EMAIL = "your_email@example.com"
   PASSWORD = "your_password"
   ```

## Running Tests

To run the tests using pytest:

```bash
pytest tests/test_pinterest.py
```

## Notes

- **Headless Mode:** The script runs Chrome in headless mode for faster execution without opening a browser window.
- **Screenshots:** Screenshots are saved in the current working directory, including `new_sms_notifications.png`, `conversations.png`, and `image.png`.

## Troubleshooting

- Ensure that your `chromedriver` is up to date. The `webdriver_manager` library automatically handles this, but you can manually check for updates if necessary.
- Verify that your credentials are correct and that Pinterest is accessible.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, please reach out to [Hasibur Rahman](mailto:hasibshanto260@gmail.com).
```
