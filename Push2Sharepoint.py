import os
import argparse
import logging

from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.system_object_type import FileSystemObjectType

# Setting up the logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')

# Argument parsing
parser = argparse.ArgumentParser(description='Upload files to SharePoint')
parser.add_argument('--username', required=True, help='SharePoint username')
parser.add_argument('--password', required=True, help='SharePoint password')
parser.add_argument('--site_url', required=True, help='SharePoint site URL')
parser.add_argument('--folder_name', required=True, help='SharePoint folder name')
parser.add_argument('--documents', required=True, nargs='+', help='Documents to upload')

args = parser.parse_args()


# Work of https://github.com/SebastianP98 
# class to connect to SharePoint, create folder and subfolders in SharePoint,
#to upload the list of files received in self.documents to the self.folder_name(SharePoint folder)
class SharePointFileManager:
    def __init__(self, username, password, site_url):
        self.username = username
        self.password = password
        self.site_url = site_url
        self.folder_name = ""
        self.documents = []
        self.all_folders_and_files = []
        self.context = self._get_client_context()

    #function to connect to SharePoint
    def _get_client_context(self):
        auth_ctx = AuthenticationContext(self.site_url)
        auth_ctx.acquire_token_for_user(self.username, self.password)
        return ClientContext(self.site_url, auth_ctx)
    
    #function to retrieve all Folders and Subfolders from SharePoint
    def get_all_folders_and_files(self):
        doc_lib = self.context.web.lists.get_by_title("Documents")
        items = doc_lib.items.select(["FileSystemObjectType"]).expand(["File","Folder"]).get_all().execute_query()
        for item in items:  # type: ListItem
            if item.file_system_object_type == FileSystemObjectType.Folder:
                self.all_folders_and_files.append(item.folder.serverRelativeUrl)
            if item.file_system_object_type == FileSystemObjectType.File:
                self.all_folders_and_files.append(item.file.serverRelativeUrl)

    #function to create SharePoint folder and subfolder if not existing
    def create_folder_if_not_exists(self):
        logging.info(f"Path to verify if exists: {self.folder_name}\n")
        folder_parts = self.folder_name.split('/')
        current_folder_url = ""

        # Check and create each folder in the path if it doesn't exist
        for folder_part in folder_parts:
            if current_folder_url == "":
                current_folder_url += folder_part
            else:
                current_folder_url += '/' + folder_part
            logging.info(f"Verifying if folder {current_folder_url} exists.")
            if not any(current_folder_url in item for item in  self.all_folders_and_files):
                logging.info(f"Folder doesn't exist.")
                logging.info(f"Creating folder: {current_folder_url}")
                self.context.web.folders.add(current_folder_url).execute_query()
            

    #Function to upload docx documents that are not present in SharePoint.
    def upload_documents_not_present(self):
        for document in self.documents:
            local_path = os.path.basename(document)
            logging.info("Verify if document {} exists in SharePoint".format(local_path))
            if not any(local_path in item for item in  self.all_folders_and_files):
                logging.info("Document {} does not exists in SharePoint".format(document))
                logging.info(f"Uploading file {local_path} to {self.folder_name}")
                remote_path = f"{self.folder_name}/{local_path}"

                with open(document, 'rb') as content_file:
                    file_content = content_file.read()

                dir, name = os.path.split(remote_path)
                self.context.web.get_folder_by_server_relative_url(dir).upload_file(name, file_content).execute_query()

    # Function to upload document even if the document exists.
    def upload_documents(self):
        for document in self.documents:
            local_path = os.path.basename(document)
            logging.info(f"Uploading file {local_path} to {self.folder_name}")
            remote_path = f"{self.folder_name}/{local_path}"

            with open(document, 'rb') as content_file:
                file_content = content_file.read()

            dir, name = os.path.split(remote_path)
            self.context.web.get_folder_by_server_relative_url(dir).upload_file(name, file_content).execute_query()

    #Function that will be called in Main.py in order to create folder and upload documents
    def execute(self, folder_name, existing_documents_list, documents=[]):
        self.folder_name = folder_name
        logging.info("Inside SharePoint class\n\n")
        self.get_all_folders_and_files()
        self.create_folder_if_not_exists()
        if existing_documents_list:
            self.documents = existing_documents_list
            self.upload_documents_not_present()
        if documents:
            self.documents = documents
            self.upload_documents()
        logging.info("All documents uploaded.\n\n")

if __name__ == '__main__':
    # Initialize the SharePointFileManager class
    sp = SharePointFileManager(args.username, args.password, args.site_url)
    documents=args.documents.split(",")
    # Execute the file uploading
    sp.execute(args.folder_name, documents)
