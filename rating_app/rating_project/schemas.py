from pydantic import BaseModel,Field

class Rating(BaseModel):
   name    : str 
   rate    : int = Field(None,ge=1,le=5)
   
   model_config = {
        "from_attributes": True
    }
