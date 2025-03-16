import os


class Links:
    STAGE = os.environ["STAGE"]
    HOST = f"https://{STAGE}.opensource-socialnetwork.org"
    LOGIN = f"{HOST}/login"
    HOME = f"{HOST}/home"