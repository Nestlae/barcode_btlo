#i recommend you to search how's code working
import cv2
from pyzbar.pyzbar import decode
barcode_world = []

for i in range(1,9375):
    image = cv2.imread('pathTo/Barcode_World/barcode_images/'+str(i)+'.png')
    detectedBarcodes = decode(image)
    for barcode in detectedBarcodes:
        barcode_world += barcode.data

barcode_world_conChar = "".join(map(chr, barcode_world))
print(barcode_world_conChar)
        
#take a while and convert ascii to text, then you got it.