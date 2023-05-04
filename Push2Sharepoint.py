from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file_creation_information import FileCreationInformation
import os
import sys

# Set Login Info
username = sys.argv[1]
password = sys.argv[2]
fileName = sys.argv[3]
fullurl = sys.argv[4]
targetsubfolder = sys.argv[5]

# Define the base target folder as the current working directory
targetfolder = os.getcwd() + "/"

if len(targetsubfolder) != 0:
    targetfolder = targetfolder + targetsubfolder

ctx_auth = AuthenticationContext(url=fullurl)
if ctx_auth.acquire_token_for_user(username=username,
                                   password=password):
    ctx = ClientContext(fullurl, ctx_auth)
    libraryRoot = ctx.web.get_folder_by_server_relative_url(targetfolder)

    info = FileCreationInformation()

    with open(fileName, 'rb') as content_file:
        info.content = content = content_file.read()
    print(os.path.basename(fileName))
    info.url = os.path.basename(fileName)
    info.overwrite = True
    upload_file = libraryRoot.files.add(info)

    ctx.execute_query()
