import cv2
import time
import random
import dropbox
#to start time
start_time=time.time()

def take_snapshot():
    #randomly take images
    number=random.randint(0,100)

    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()


        img_name="img"+str(number)+".jpg"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name   
    print("Snapshot Taken!")

    videoCaptureObject.release()
    cv2.destroyAllWindows()


def upload_file(img_name):
    access_token = 'sl.BLNkIJTcTZ2hwD1SD0J4Fl0k0-sfa9TP5XYHo5UIKGKB91h2KUU5N64q8QrToUegkiiDS7FzlhRmGSneHZ98dhu7y9Aca1ggJETJXgVutag-d95EKhpVoD6U_TaseiqfZfKrUkM'
    file=img_name
    file_from=file
    file_to='/test_dropbox/'+(img_name)
    
    dbx=dropbox.Dropbox(access_token)


    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file has been uploaded !!!")


def main():
    while(True):
        if((time.time()-start_time)>=60):
            name=take_snapshot()
            upload_file(name)

            
main()