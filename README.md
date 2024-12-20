# Emailme

**Emailme** is a simple command-line utility for sending emails via AWS SES (Amazon Simple Email Service). Designed for simplicity, it enables both admins and users to configure and send emails effortlessly.

---

## Features

- **Easy Setup:** Configure once and start sending emails instantly.
- **AWS SES Integration:** Leverages AWS SES for reliable email delivery.
- **User-Friendly Commands:** Intuitive CLI for quick operations.
- **Customizable for Admins and Users:** Separate configurations for admins (sender) and users (recipients).

---

## Installation

### Method 1: **Quick (Not Recommended)**

This method uses system-level installations, which might break dependencies.

```bash
cd emailme
sudo pip install -r requirements.txt --break-system-packages
sudo pip install -e . --break-system-packages
```

### Method 2: **Recommended**

The recommended way ensures a safer and more robust setup. *(Details coming soon!)*

---

## Configuration

### For Admins
Admins set up sender email and AWS credentials. These settings are stored securely in `/etc/emailme/aws.toml`.

Run the following command and provide the required details:

```bash
sudo emailme aws
```

### For Users
Users should configure their email as the recipient with:

```bash
emailme configure
```

---

## Usage

Here’s how you can send an email using **emailme**:

### Send an Email After a Delay
Example: Wait for 30 seconds, then send an email with a subject and body.

```bash
sleep 30 && emailme send --subject "Test Email" --body "sleep 30"
```

### General Syntax
```bash
emailme send --subject "<SUBJECT>" --body "<BODY>"
```

---

### Notes

- Ensure you have AWS SES credentials with the required permissions.
