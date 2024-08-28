import os
from pathlib import Path
from split_settings.tools import include

include(
    "base.py",
    "local.py",
    "prod.py",
)