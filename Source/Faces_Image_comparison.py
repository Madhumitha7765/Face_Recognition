import cv2
import face_recognition

# function for Comparing faces of input images and encoding
def compare(imgServer,imgTest):

    # Finding face location inside image using HOG method
    faceLoc = face_recognition.face_locations(imgServer)[0]
    # print(faceLoc)
    # encoding images
    encodeServer = face_recognition.face_encodings(imgServer)[0]
    # forming square with cv2 using neural networks result
    cv2.rectangle(imgServer, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)
    faceLocTest = face_recognition.face_locations(imgTest)[0]
    encodeTest = face_recognition.face_encodings(imgTest)[0]
    cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

    # compare encoded images
    # if images match result is true
    results = face_recognition.compare_faces([encodeServer], encodeTest)
    # compute face distances
    faceDis = face_recognition.face_distance([encodeServer], encodeTest)
    print(results, faceDis)
    # inserting text inside output
    cv2.putText(imgTest, f'{results} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Server Image', imgServer)
    cv2.imshow('Test Image', imgTest)
    cv2.waitKey(0)


if __name__ == "__main__":
    # loading and importing images
    imgServer = face_recognition.load_image_file('ImagesBasic/Bill gates.jpg')
    # Images converted from bgr to rgb images
    imgServer = cv2.cvtColor(imgServer, cv2.COLOR_BGR2RGB)
    #imgTest = face_recognition.load_image_file('ImagesBasic/Bill gates1.jpg')
    imgTest = face_recognition.load_image_file('ImagesBasic/Elon Musk2.jpg')
    imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
    # imgTest = cv2.resize(imgTest, (600, 600))
    # imgServer = cv2.resize(imgServer, (600, 600))

    # function call to compare both images
    compare(imgServer,imgTest)