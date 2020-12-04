import dropbox
import io


class FileUploader:
    def __init__(self, access_token):
        self.access_token = access_token
        self.dbx = dropbox.Dropbox(self.access_token)

    def __del__(self):
        self.dbx.close()

    def upload_image(self, image_binary, filename):
        try:
            meta = self.dbx.files_upload(image_binary.read(), filename, mode=dropbox.files.WriteMode("overwrite"))
            link = self.dbx.sharing_create_shared_link(filename)
            return link.url
        except dropbox.exceptions.ApiError:
            print("!E!", "Failed to dropbox")


def main():
    access_token = '****'
    fu = FileUploader(access_token)
    # filename = "/text.txt"
    # binary_data = io.BytesIO(b"tekstukas")
    # binary_data.seek(0)
    # fu.upload_image(binary_data, filename)
    return fu


if __name__ == '__main__':
    main()