# check_env.py
import os
print("DATABASE_URL value:", repr(os.environ.get('DATABASE_URL')))
print("SECRET_KEY value:", repr(os.environ.get('SECRET_KEY')))