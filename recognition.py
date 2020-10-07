from picamera import PiCamera
import time
import boto3

directory = 'captured'

P=PiCamera()
P.resolution= (800,600)
P.start_preview()
collectionId='bharti-patel'

rek_client=boto3.client('rekognition',
                        aws_access_key_id='AKIAV4O3GGAWH2JG35OA',
                        aws_secret_access_key='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',
                        region_name='us-east-1',)# add the region here

if __name__ == "__main__":

        time.sleep(2)
        
        milli = int(round(time.time() * 1000))
        image = '{}/image_{}.jpg'.format(directory,milli)
        P.capture(image)
        print('captured '+image)
        with open(image, 'rb') as image:
            try:
                match_response = rek_client.search_faces_by_image(CollectionId=collectionId, Image={'Bytes': image.read()}, MaxFaces=1, FaceMatchThreshold=85)
                if match_response['FaceMatches']:
                    print('Hello, ',match_response['FaceMatches'][0]['Face']['ExternalImageId'])
                    print('Similarity: ',match_response['FaceMatches'][0]['Similarity'])
                    print('Confidence: ',match_response['FaceMatches'][0]['Face']['Confidence'])
    
                else:
                    print('No faces matched')
            except:
                print('No face detected')
            

        time.sleep(1)       
