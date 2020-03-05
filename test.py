import os

class VerifyPhoto:
    #initialization
    def __init__(self):
        self.no_photos = False

    #Access Photo Album
    def getphotos(self):
        try:
            album = os.listdir('/Users/vinutha/Documents/wallpapers/')
            path = '/Users/vinutha/Documents/wallpapers/Sunset.jpg'
            if os.path.isfile(path):
                print('File exists in the directory')
            # print('Files can be read')
            print('Directory exists!')
            self.no_photos = False
        except FileNotFoundError:
            print('File does not exist')
            self.no_photos = False
        except IOError:
            print('Path is incorrect')
            self.no_photos = True


def main():
    photo = VerifyPhoto()
    photo.getphotos()

    if photo.no_photos:
        print("Sorry. There are no photos in the Album")
    else:
        print("Hooray! There are so many photos in Album")


if __name__ == '__main__':
    main()
