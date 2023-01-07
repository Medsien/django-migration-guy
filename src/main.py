import json
import os

for key, val in sorted(dict(os.environ).items()):
    print(f"{key} = {val}")

print("files:", os.listdir("."))
