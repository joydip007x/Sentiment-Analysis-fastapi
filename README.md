
 # Sentiment Analysis 
 ##### **USING**  : Python, Fastapi, Pydantic, Transformer
 ##### S/A model : https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest 
<hr>
 A Backend build on Python & Fastapi with a RESTful API endpoint for sentiment analysis. <br>
 The API will accept text input, validate with Pydantic and return the sentiment analysis result using a pre-trained machine learning model.


# Installation 

Make sure `python version >=3.9`.<br>
Clone this repo, open in terminal and
>Run :
```python
python -m venv .venv 
```
>In Terminal, Run the following commands : 

 In **Linux**: `source .venv/bin/activate` 

 In **Windows**: `.venv\Scripts\activate` 

>Then install the required dependencies and start app
 ```
 pip install  -r requirements.txt 
 uvicorn main:app
 ```
# What's in it ?

- Minimal Static FrontEnd : `http://127.0.0.1:8000/`
  - Write an Sentence and Get Sentiment-Analyses instantly
- Request is validated 
- Response is validated
- Added Extra Query  Sentiment Percentage Match
- Exception Handling included

  

<details  open>
<summary > API Routes </summary>
<p align="center"  >  

- *GET* REQUEST - `http://127.0.0.1:8000/hello` 
  - Request Payload - Empty
  - Expected Response - "Hello World"
- *POST* REQUEST `http://127.0.0.1:8000/analyze`
  - Request Payload - **JSON** : {"text": "STRING"}
  - Expected Response - **JSON** : {"sentiment":"positive/negative/neutral"}
  -  To get a Response with Sentence Sentiment and **Score**
   add `?withScore=True` <br>
  i.e. - *POST* REQUEST `http://127.0.0.1:8000/analyze?withScore=True`
  - **With Score** Expected Response - **JSON** : `{"sentiment":"positive/negative/neutral", "score": float}`
  
  
  
 </p>
</details>
