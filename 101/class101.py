import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

    
        f=open(file_from,'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BKD4ie2BnDrEULj4di3P4E5-OOqseE5XSExiKtR5MsgOta-wObkfr8Nll6WW-B-bxUtR3I4J0N4-BuuqqX_nwK5OwwiiHNCGBzgZxs6Vs7nXnmYPx_t-j2ENlh9lQIycHyrALdk'
    transferData = TransferData(access_token)

    file_from = input('enter the file path to transfer:-')
    file_to =input("enter the full path to upload to dropbox:- ")
     # The full path to upload the file to, including the file name
     # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()
