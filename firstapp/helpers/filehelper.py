from django.conf import settings
from django.core.files.storage import FileSystemStorage


class HelperFileUpload():
    def __init__(self, settings):
        self.path_r = settings.MEDIA_ROOT + settings['path']
        self.path_u = settings.MEDIA_URL + settings['path']
        self.file = settings['file']
        self.file_name = settings['file'].name
        self.ch_f = settings['change_file']
        self.ch_n = settings['change_name']
        self.FSS = FileSystemStorage(self.path_root, self.path_url)


    def upload_one(self):
        if self.ch_f:
            if fs.exists(self.path_r + self.file_name):
                self.FSS.delete(self.path_r + self.file_name)
        save = self.FSS.save(self.file_name, self.file)
        return self.FSS.url(save)

    def upload_many(self):
        print('Это мы создали объект FileHelperUpload из MyHelper')

    def search_file():
        pass
