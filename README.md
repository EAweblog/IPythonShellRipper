# IPythonShellRipper
Upload all the files in the current working directory of an IPython Shell to catbox.moe for download

# Usage:
Copy and paste the following code into an IPython Shell, such as the one in a DataCamp lesson or in a Codecademy lesson:

```
exec(__import__('requests').get('https://raw.githubusercontent.com/EAweblog/IPythonShellRipper/refs/heads/main/script.py').text)
```
