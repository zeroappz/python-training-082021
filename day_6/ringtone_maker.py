# bit rate - 128kbps, 320kpbs ---->
# audio - splitted in to two channels
class AudioMaker():
    def audio_cutter(self, path):
        try:
            file = open(path, "rb").read()  # 4-40mb (\b'0xdsaf') ---> 300s
            mp3 = list(file)  # [\b'0xdsaf', \b'0xdsaf'......]
            bitrate = int(input("Enter the bit rate: "))
            # transferring data finto two channels
            size_mbps = bitrate * (15/2048)
            per_sec_size = ((size_mbps/60)*10**6)   # 100kb
            start_length = int(input("Where to start: "))
            end_length = int(input("Where to end: "))
            # 30th sec * 100kb ==> 3000kb
            starting_size = int(per_sec_size * start_length)
            # 60th sec * 100kb ==> 6000kb
            ending_size = int(per_sec_size * end_length)
            create_new_file = open("new_file.mp3", "wb")        # 30s
            create_new_file.write(bytes(mp3[starting_size:ending_size]))
        except Exception as obj:
            print(obj)


def main():
    ilayaraja = AudioMaker()
    ilayaraja.audio_cutter("ilayaraja.mp3")

    yuvan = AudioMaker()
    yuvan.audio_cutter("yuvan_song.mp3")


if __name__ == "__main__":
    main()


# [] --> slicing ---> file open() and process & write()
# file management --->

# video, audio
# File ----> bytestream, characteream ---> instance ---> file access ---> write
# c procedure
# mode, file path ----> read, write, delte, seek, process, update

# mode: w, r, a
# binary mode: wb, rb, ab


# write() - it will check wether the file is available or what
# available - rewite
# if not - it will create a file and then write

# try:
#     obj = open(
#         "C:\\Users\\pravi\\OneDrive\\Documents\\python-training-082021\\doc.txt", "rt").read()

#     print(obj)

#     create_new_file = open(
#         "C:\\Users\\pravi\\OneDrive\\Documents\\python-training-082021\\doc.txt", "w")

#     create_new_file.write('''fdnsfsld  dskdnk  sdsnkdn  ''')
# except:
#     print("File not found...")

# finally:
#     # obj.close()
#     # create_new_file.close()
#     pass
'''
'''
# delete delete a file
# import os

# os.makedirs("test")

# if os.path.exists("email.txt"):
#     os.remove("email.txt")
# else:
#     print("file not found...")


'''
os.makedirs('folder name') - create a folder
os.rmdir('folder name')
os.remove("file.txt")

'''
# prequisites ----> MP3 file, (flv, .mpeg)
# os access
# process ---> file access - convert - slicing - write as a new file
