import argparse

from emailme.tasks import configure, send, aws

def main():
    parser = argparse.ArgumentParser(prog="emailme", description="Send an email using AWS SES")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # AWS parser
    aws_parser = subparsers.add_parser("aws", help="Setup AWS options")
    aws_parser.set_defaults(func=aws.run)

    # Configure parser
    config_parser = subparsers.add_parser("configure", help="Setup `emailme` configuration")
    config_parser.set_defaults(func=configure.run)

    # Send parser
    send_parser = subparsers.add_parser("send", help="Send an email")
    send_parser.add_argument("--subject", "-s", help="Email subject")
    send_parser.add_argument("--body", "-b", help="Email body")
    send_parser.set_defaults(func=send.run)

    # Parse the arguments
    args = parser.parse_args()

    # Run the function
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
