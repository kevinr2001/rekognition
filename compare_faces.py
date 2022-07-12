import boto3
from pprint import pprint

client = boto3.client('rekognition')


def compare_faces(source_file, target_file):
    client = boto3.client('rekognition')

    image_source = open(source_file, 'rb')
    image_target = open(target_file, 'rb')

    response = client.compare_faces(SimilarityThreshold=80,
                                    SourceImage={'Bytes': image_source.read()},
                                    TargetImage={'Bytes': image_target.read()})

    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])
        pprint('The face at ' + str(position['Left']) + ' ' + str(position['Top']) + ' matches with ' + similarity +
               '% confidence')

    image_source.close()
    image_target.close()
    return len(response['FaceMatches'])


def main():
    source_file = './img/4x1.jpg'
    target_file = './img/Grad.jpg'
    face_matches = compare_faces(source_file, target_file)
    pprint("Face matches: " + str(face_matches))


if __name__ == "__main__":
    main()
