import pdfplumber

"""
useful functions called by this package
"""

def get_empty_table() -> dict:
    """
    :return: an empty table dict
    """
    return {
        "order": [],
        "id": [],
        "name": [],
        "institution": [],
        "principal": [],
        "founds": [],
        "period": [],
        "title": "",
        "project": ""
    }

