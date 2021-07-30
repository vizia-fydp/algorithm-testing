import easyocr
import time

# need to run only once to load model into memory
start = time.time()
reader = easyocr.Reader(['en'])
end = time.time()
time_ms = (end - start) * 1000
print("{} ms to load model into memory".format(time_ms))

start = time.time()
# result = reader.readtext('img/kindle.jpg')
result = reader.readtext('img/kindle.jpg', detail = 0)
end = time.time()
time_ms = (end - start) * 1000
print("{} ms to run OCR".format(time_ms))

print("OCR Results:")
print(result)