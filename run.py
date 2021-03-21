import datetime, os
from edinet import fetch
from edinet import file_io
from setting import OUTPUT_DIR, TARGET_DOC_TYPES

if __name__ == "__main__":
    date = datetime.date(2020, 6, 25)
    str_date = date.strftime("%Y-%m-%d")

    os.makedirs(os.path.join(OUTPUT_DIR, str_date), exist_ok=True)
    for doc_type in TARGET_DOC_TYPES:
        os.makedirs(os.path.join(OUTPUT_DIR, str_date, doc_type), exist_ok=True)
    
    list_df = fetch.fetch_list(date)
    if len(list_df) > 0:
        for i in range(len(list_df)):
            doc_type = list_df.iloc[i]["docTypeCode"]
            if doc_type in TARGET_DOC_TYPES:
                doc_id = list_df.iloc[i]["docID"]
                filer_name = list_df.iloc[i]["filerName"]
                res = fetch.fetch_document(doc_id)
                file_io.save_document(res, doc_id, date, doc_type)
                print(f"DONE: {filer_name}-{doc_type}")