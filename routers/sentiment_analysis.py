from fastapi import APIRouter
from schemas.sentiment_analysis import Sentence,Analysis
from analyser.sentiment_analyser  import sentiment_analyser

router = APIRouter()

# Basic get-HelloWorld
@router.get('/hello')
async def hello():
    return {"Hello World"}


# POST request to Analyze  text from requestBody
# returns : positive/negative/neutral in JSON 
#           response is Validated  
@router.post('/analyze',response_model=Analysis, response_model_exclude_none=True)
async def analyze(data:Sentence,withScore: bool = False):
    sentences = [data.text]
    pred=sentiment_analyser(sentences)
    label=pred[0].get('label')
    score=pred[0].get('score')
   
    response={"sentiment":label}
    if withScore:
        response['score']="{:.2f}".format(score*100)
    return response