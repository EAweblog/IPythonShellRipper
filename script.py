import os
import zipfile
import time
import requests

def zip_files():
    output_zip = f"{time.time()}.zip"
    cwd = os.getcwd()
    with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(cwd):
            for fn in files:
                if fn == output_zip: continue
                fp = os.path.join(root, fn)
                zipf.write(fp, os.path.relpath(fp, cwd))
    print(f"All contents of {cwd} have been zipped into {output_zip}.")
    return output_zip

def upload_to_catbox(fp):
    url = "https://catbox.moe/user/api.php"
    data = {"reqtype": "fileupload"}
    with open(fp, "rb") as file:
        response = requests.post(url, data=data, files={"fileToUpload": file})
    if response.status_code == 200:
        print("File uploaded to catbox.moe successfully!")
        print("Download link:")
        print(response.text.strip())
    else:
        print(f"Failed to upload to catbox.moe. Status code: {response.status_code}")

def main():
    output_zip = zip_files()
    upload_to_catbox(output_zip)

main()
