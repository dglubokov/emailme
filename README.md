# Emailme

Simple email sending command line utility for sending emails from the command line using AWS SES.

## Quick Installtion (Bad Way)

```bash
sudo pip install -e . --break-system-packages
```

## Usage Example

```bash
sleep 30 && emailme send --subject "Test Email" --body "sleep 30"
```
