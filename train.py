import boto3

s3_client = boto3.client(
    's3',
    aws_access_key_id='AKIAV4O3GGAWH2JG35OA',
    aws_secret_access_key='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'
    
)

collectionId='xyz-abc'

rek_client=boto3.client('rekognition',
                            aws_access_key_id='AKIAV4O3GGAWH2JG35OA',
                            aws_secret_access_key='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',
                            region_name='us-east-1')


bucket = 'dhaval-dadhaniya'
all_objects = s3_client.list_objects(Bucket = bucket )



list_response=rek_client.list_collections(MaxResults=2)

if collectionId in list_response['CollectionIds']:


    rek_client.delete_collection(CollectionId=collectionId)


rek_client.create_collection(CollectionId=collectionId)



for content in all_objects['Contents']:
    collection_name,collection_image =content['Key'].split('/')
    if collection_image:
        label = collection_name
        print('indexing: ',label)
        image = content['Key']    
        index_response=rek_client.index_faces(CollectionId=collectionId,
                                Image={'S3Object':{'Bucket':bucket,'Name':image}},
                                ExternalImageId=label,
                                MaxFaces=1,
                                QualityFilter="AUTO",
                                DetectionAttributes=['ALL'])
        print('FaceId: ',index_response['FaceRecords'][0]['Face']['FaceId'])
