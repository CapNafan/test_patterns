import os

from dotenv import load_dotenv

load_dotenv()


class Credentials:

    if os.environ["STAGE"] == "prod":
        LOGIN = os.getenv("PROD_LOGIN")
        PASSWORD = os.getenv("PROD_PASSWORD")

    elif os.environ["STAGE"] == "release":
        LOGIN = os.getenv("RELEASE_LOGIN")
        PASSWORD = os.getenv("RELEASE_PASSWORD")
