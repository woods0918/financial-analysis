import datetime, json, os, requests
import pandas as pd
from typing import Optional

from setting import LIST_ENDPOINT, DOCUMENT_ENDPOINT, OUTPUT_DIR

def fetch_list(date: datetime.date, type_no: int=2) -> Optional[pd.DataFrame]:
    str_date = date.strftime("%Y-%m-%d")
    response = requests.get(url=LIST_ENDPOINT, params={"date": str_date, "type": type_no})
    content = json.loads(response.content)
    if response.status_code == 200:
        results = content["results"]
        if len(results) > 0:
            key = results[0].keys()
            values = [dic.values() for dic in results]
            df = pd.DataFrame(values, columns=key)
            df = _list_cleansing(df)
            return df
        else:
            print(f"{str_date} has no documents")
    else:
        print(f"{str_date} Access Error: \n status : {response.status_code}")
    
def fetch_document(doc_id: str, type_no: int=1) -> Optional[requests.models.Response]:
    response = requests.get(url=DOCUMENT_ENDPOINT+doc_id, params={"type": type_no}, stream = True)
    if response.status_code == 200:
        return response

def _list_cleansing(df: pd.DataFrame) -> pd.DataFrame:
    df["filerName"] = [
        filer_name.replace("\u3000", " ") if type(filer_name) is str else filer_name for filer_name in df["filerName"]
    ]
    return df