import subprocess

from emailme.aws_client import get_client, load_aws_config
from emailme.config import get_config

HOSTNAME = subprocess.check_output(["hostname"]).strip().decode("utf-8")
DEFAULT_SUBJECT = f"[{HOSTNAME}] Email Notification"
DEFAULT_BODY = "This is an email notification from {HOSTNAME}."


def run(args):
    # Set default values if not provided
    subject = args.subject or DEFAULT_SUBJECT
    body = args.body or DEFAULT_BODY

    if subject == DEFAULT_SUBJECT:
        print(f"Using default subject: {subject}")
    else:
        # Add hostname to the subject
        subject = f"[{HOSTNAME}] {subject}"
    if body == DEFAULT_BODY:
        print(f"Using default body: {body}")
    else:
        # Add hostname to the body
        body = (
            f"{body}\n\n"
            f"---\n"
            f"Notification sent by {HOSTNAME}.\n"
            f"This message is auto-generated. Please do not reply."
        )

    # Get AWS Client
    client = get_client()
    aws_config = load_aws_config()

    # Get the configuration
    config = get_config()

    try:
        client.send_email(
            Destination={
                "ToAddresses": [config.recipient],
            },
            Message={
                "Body": {
                    "Html": {
                        "Charset": "UTF-8",
                        "Data": body.replace("\n", "<br>"),
                    },
                    "Text": {
                        "Charset": "UTF-8",
                        "Data": body,
                    },
                },
                "Subject": {
                    "Charset": "UTF-8",
                    "Data": subject,
                },
            },
            Source=aws_config.sender,
        )
        print(f"Email sent to {config.recipient}")
    except Exception as e:
        print(f"An error occurred while sending the email. Please check the provided details and retry.\nError: {e}")
        exit(1)
