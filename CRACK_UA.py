import os, sys

os.system('git pull')

try:

    __import__("User_Agent_A").main()

except Exception as e:

    exit(str(e))
