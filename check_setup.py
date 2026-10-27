"""Setup check for the AI Ticket Triage project.

Run after installing the requirements:

    python check_setup.py

It confirms your Python version and that every library we need is installed.
"""

import sys

print("Python version:", sys.version.split()[0])
print()

libraries = ["pandas", "sklearn", "datasets", "fastapi", "matplotlib"]
all_ok = True

for lib in libraries:
    try:
        module = __import__(lib)
        version = getattr(module, "__version__", "")
        print(f"OK       {lib} {version}")
    except ImportError:
        all_ok = False
        print(f"MISSING  {lib}  ->  run: pip install -r requirements.txt")

print()
if all_ok:
    print("Setup works. You are ready for Step 2 (download the dataset).")
else:
    print("Some libraries are missing - install them, then run this check again.")
