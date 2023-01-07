import json
import os

print(json.dumps(sorted(dict(os.environ)), indent=2))

print("files:", os.listdir("."))
