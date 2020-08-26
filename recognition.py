from tkinter import messagebox
from datetime import datetime
import cv2
import mainPage
import random
import userinfos
import classifier
import loginPage
import encrypt
sozluk={}
def draw_recognize(img,classfier,scale,neigh,color,username,clf,password):
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    features=classfier.detectMultiScale(gray_img,scale,neigh)
    check=False
    coords=[]
    for(x,y,w,h) in features:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        id, check = clf.predict(gray_img[y:y+h,x:x+w])
        if str(id) in userinfos.usr.keys():
            if id==userinfos.usr[username] and password==userinfos.usr[str(id)]:
                cv2.putText(img,username,(x-10,y-4),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),1,cv2.LINE_AA)
                check=True
        coords=[x,y,w,h]
    return coords,img,check
def draw_detect(img,classfier,scale,neigh,color):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classfier.detectMultiScale(gray_img, scale, neigh)
    coords = []
    for(x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        coords = [x, y, w, h]
    return coords, img
def generate_dataset(img,id,img_id):
    cv2.imwrite("data/user."+str(id)+"."+str(img_id)+".jpg", img)

def recognize(img,clf,faceCascade,username,password):
    coords=draw_recognize(img,faceCascade,1.1,10,(0,0,255),username,clf,password)
    return img,coords[2]

def detect(img,faceCascade,img_id,username,user_id):
    i=0
    coords,img=draw_detect(img,faceCascade,1.1,10,(0,0,255))
    if len(coords)==4:
        roi_img=img[coords[1]:coords[1]+coords[3],coords[0]:coords[0]+coords[2]]
        sozluk[username]=user_id
        generate_dataset(roi_img,user_id,img_id)
        i=1
    return img,i

def login(username,password):
    userinfos.usr = userinfos.readUsers()
    if username not in userinfos.usr:
        messagebox.showinfo("Hata", "Kullanıcı adı bulunamadı.")
        return
    if password!=userinfos.usr[str(userinfos.usr[username])]:
        messagebox.showinfo("Hata", "Kullanıcı adı/şifre hatalı")
        return
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.read("classifier.yml")
    video = cv2.VideoCapture(1)
    img_id=0
    start_time = datetime.now()
    while True:
        _, frame= video.read()
        img_id=img_id+1
        flip = cv2.flip(frame, 1)
        result=recognize(flip,clf,faceCascade,username,password)
        frame=result[0]
        check=result[1]
        cv2.imshow("Camera ",frame)
        key = cv2.waitKey(1)
        if key == ord('q') or check==True:
            break
        timer=datetime.now() - start_time
        if timer.total_seconds() >= 5:
            messagebox.showinfo("Hata", "Yüz, kullanıcı ile eşleşmiyor.")
            video.release()
            cv2.waitKey(1)
            cv2.destroyAllWindows()
            for i in range(1, 5):
                cv2.waitKey(1)
            return
    video.release()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    for i in range(1, 5):
        cv2.waitKey(1)
    mainPage.root.destroy()
    loginPage.openLoginPage(username)
def register(username,password):
    if username in userinfos.usr.keys():
        print("KULLANICI KAYITLI")
        return
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')
    video = cv2.VideoCapture(1)
    img_id=0
    check=0
    user_id = random.randint(100000, 9999999)
    while True:
        _, frame= video.read()
        flip = cv2.flip(frame, 1)
        result=detect(flip,faceCascade,img_id,username,user_id)
        frame=result[0]
        check=check+result[1]
        img_id=img_id+1
        cv2.imshow("Camera ",frame)
        key = cv2.waitKey(1)
        if key == ord('q') or check==5:
            break
    userinfos.usr[user_id]=password
    userinfos.usr[username]=user_id
    userinfos.writeUsers(userinfos.usr)
    classifier.train("data")
    video.release()
    cv2.destroyAllWindows()
    encrypt.create_key(username)
    messagebox.showinfo("Başarılı", "Yeni kullanıcı başarıyla oluşturuldu.")




