import os

# --------------------
# Version
# --------------------
VERSION = "v1"

# --------------------
# Endpoint
# --------------------
LIST_ENDPOINT = f"https://disclosure.edinet-fsa.go.jp/api/{VERSION}/documents.json"
DOCUMENT_ENDPOINT = f"https://disclosure.edinet-fsa.go.jp/api/{VERSION}/documents/"

# --------------------
# Directory
# --------------------
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(ROOT_DIR, "outputs")

# --------------------
# Constant
# --------------------
TARGET_DOC_TYPES = [
    "120", # 有価証券報告書
    "140", # 四半期報告書
    "160"  # 半期報告書
]