import os, sys

os.system('git pull')

try:

    __import__("CRACK_UA").main()

except Exception as e:

    exit(str(e))
