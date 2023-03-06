from os import getenv
from utils.close import exit_app

try: from dotenv import load_dotenv
except ImportError: exit_app(f"Module not found: python-dotenv")

def get_env(key):
    load_dotenv()
    env = getenv(key)
    if env: return env
    else: exit_app(f"Env not found: {key}")