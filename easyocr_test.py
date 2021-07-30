import cv2
import easyocr
import time


def preprocess_img(filename):
    # Read image into memory
    img = cv2.imread(filename)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Resize image
    scale_percent = 20
    width = int(gray.shape[1] * scale_percent / 100)
    height = int(gray.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)

    return resized
    # cv2.imwrite('gray_resized.jpg', resized)


def ocr(img):
    # need to run only once to load model into memory
    start = time.time()
    reader = easyocr.Reader(['en'])
    end = time.time()
    time_ms = (end - start)
    print("{} s to load model into memory".format(time_ms))

    start = time.time()
    # result = reader.readtext('img/kindle.jpg')
    result = reader.readtext(img, detail = 0)
    end = time.time()
    time_ms = (end - start)
    print("{} s to run OCR".format(time_ms))

    print("OCR Results:")
    print(result)


if __name__ == "__main__":
    ocr(preprocess_img('img/kindle.jpg'))
    # preprocess_img('img/kindle.jpg')

