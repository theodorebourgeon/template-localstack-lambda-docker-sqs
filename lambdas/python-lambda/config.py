import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from dotenv import load_dotenv

load_dotenv()


def config(secret_name):
    if secret_name in os.environ:
        return os.getenv(secret_name)
    else:
        raise Exception("This environment variable is missing : " + secret_name)
