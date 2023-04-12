# Push2SharePoint GitHub Action

This GitHub Action uploads a file to SharePoint using the Office 365 REST API. It is perfect for situations where you need to automatically upload generated files, reports, or artifacts to a SharePoint document library.

## Prerequisites

Before using this GitHub Action, you must have:

- A SharePoint Online site with a document library you want to upload files to.
- A user account with permission to upload files to the desired document library.

## Inputs

| Name             | Description                                          | Required |
| ---------------- | ---------------------------------------------------- | -------- |
| `username`       | The username of the SharePoint account.              | Yes      |
| `password`       | The password of the SharePoint account.              | Yes      |
| `file_name`      | The name of the file to upload.                      | Yes      |
| `full_url`       | The full URL of the SharePoint site.                 | Yes      |
| `target_subfolder` | The subfolder in the document library where the file should be uploaded. | Yes |

## Usage

To use this action in your workflow, add the following step to your `.github/workflows/main.yml` file:

```yaml
steps:
  - name: Upload file to SharePoint
    uses: sjultra/Push2Sharepoint@v1.0.0
    with:
      username: ${{ secrets.SHAREPOINT_USERNAME }}
      password: ${{ secrets.SHAREPOINT_PASSWORD }}
      file_name: 'your-file-name.ext'
      full_url: 'https://your-domain.sharepoint.com/sites/your-site-name'
      target_subfolder: 'Shared Documents/your-target-folder'
 ```
Replace the placeholders with your actual information, and make sure to store your SharePoint credentials as encrypted secrets in your repository.

## License
This GitHub Action is released under the [MIT License](./LICENSE).

