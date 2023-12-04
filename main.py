import os
import warnings
import random
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText
from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time

nltk.download('punkt')
nltk.download('stopwords')

SCIENCE_RESPONSES = {
    "physics": [
        "Physics is the science that studies matter, its motion and behavior through space and time.",
        "Physics involves understanding the fundamental laws of the universe and applying them to solve complex problems."
    ],
    "biology": [
        "Biology is the natural science that studies life and living organisms.",
        "Biology covers a broad range of topics, from molecular biology to the study of ecosystems."
    ],
    "chemistry": [
        "Chemistry is the science of matter and the changes it undergoes.",
        "Chemistry deals with the composition and properties of substances and their interactions."
    ],
    "astronomy": [
        "Astronomy is the study of celestial objects and phenomena beyond Earth's atmosphere.",
        "Astronomers explore galaxies, stars, planets, and cosmic events using telescopes and other technologies."
    ],
    "geology": [
        "Geology is the study of the Earth, its materials, and the processes acting upon them.",
        "Geologists examine rocks, fossils, and Earth's landscapes to understand its history and future."
    ],
    "ecology": [
        "Ecology is the branch of biology that deals with the relations of organisms to one another and to their physical surroundings.",
        "Ecologists study ecosystems, biodiversity, and the impacts of environmental changes."
    ],
    "genetics": [
        "Genetics is the study of genes, genetic variation, and heredity in living organisms.",
        "It's a key part of biology that helps explain how traits are passed from parents to offspring."
    ],
    "meteorology": [
        "Meteorology is the science dealing with the atmosphere and weather.",
        "Meteorologists study weather patterns, storms, and climate changes."
    ],
}

def get_response(query):
    tokens = word_tokenize(query.lower())
    tokens = [word for word in tokens if word not in stopwords.words('english')]

    for word in tokens:
        if word in SCIENCE_RESPONSES:
            return random.choice(SCIENCE_RESPONSES[word])

    return "I'm not sure how to answer that. Can you ask something else about science?"

############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # TODO Add code here
    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    for text in request.text:
        # TODO Add code here
        response = get_response(text)
        output.append(response)

    return SimpleText(dict(text=output))
