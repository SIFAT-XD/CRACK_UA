import os, sys

os.system('git pull')

try:

    __import__("user_again").main()

except Exception as e:

    exit(str(e))
