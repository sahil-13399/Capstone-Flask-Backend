import os
from google.cloud import vision
import cv2

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./static/My First Project-02ae9b15e59c.json"
print('Credendtials from environ: {}'.format(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))


def CloudVisionTextExtractor(handwritings):
    # convert image from numpy to bytes for submittion to Google Cloud Vision
    _, encoded_image = cv2.imencode('.png', handwritings)
    content = encoded_image.tobytes()
    image = vision.Image(content=content)
    
    # feed handwriting image segment to the Google Cloud Vision API
    client = vision.ImageAnnotatorClient()
    response = client.document_text_detection(image=image)
    
    return response

def getTextFromVisionResponse(response):
    texts = []
    for page in response.full_text_annotation.pages:
        for i, block in enumerate(page.blocks):  
            for paragraph in block.paragraphs:       
                for word in paragraph.words:
                    word_text = ''.join([symbol.text for symbol in word.symbols])
                    texts.append(word_text)

    return ' '.join(texts)


def handwrittenParser(path):
    image = cv2.imread(path)
    response = CloudVisionTextExtractor(image)
    handwrittenText = getTextFromVisionResponse(response)
    listOfWords = list(map(lambda word:str(word).lower(),handwrittenText.split(" ")))
    hits = 0
    list2 = ['bury','anxious','cartoon','gentle','cat','hello','diamond','quick','juice','wise']
    for word in list2:
        if word in listOfWords:
            hits += 1
    misses = 10 - hits
    accuracy = hits/10
    return hits,misses,accuracy
