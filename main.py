from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from routers import (sentiment_analysis) 

app= FastAPI()

#Importing Routes
app.include_router(sentiment_analysis.router, prefix='')

#Load StaticPages
app.mount(path='/', app=StaticFiles(directory="static",html = True), name="static")

#Exception Handling
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request):
    if request.url.path=='/analyze':
             return JSONResponse(content=jsonable_encoder({"details":" Provide a Valid Text for analysis"}), 
                                 status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return JSONResponse(content=jsonable_encoder({"detail": "BAD REQUEST"}), status_code=status.HTTP_400_BAD_REQUEST)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000 )


