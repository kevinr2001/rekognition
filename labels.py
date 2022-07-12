import boto3
from pprint import pprint
import image_helpers

client = boto3.client('rekognition')

imgurl = 'https://www.switchbacktravel.com/sites/default/files/Colorado%20Outdoors%20%28m%29.jpg'

imgbytes = image_helpers.get_image_from_url(imgurl)

rekresp = client.detect_labels(Image={'Bytes': imgbytes},
                               MinConfidence=90, MaxLabels=5)

#pprint(rekresp)
print("Here's what I see in the image: ")
for label in rekresp['Labels']:
    print(label['Name'])