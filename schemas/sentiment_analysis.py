from pydantic import BaseModel, constr
from typing import Optional, Union

# Request Data Validation 
class Sentence(BaseModel):
    class Config:
        orm_mode = True
        error_msg_templates = {
            'value_error.email': 'email address is not valid.',
        }
    text: str

#Response Data Validation
class Analysis(BaseModel):
    class Config:
        orm_mode = True
    sentiment: constr(regex=r'(positive|negative|neutral)')
    score : Optional[float]