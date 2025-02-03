from pydantic import BaseModel, Field

class Topicsummary(BaseModel):
    topic: str = Field(..., description="The topics that discussed in the pdf or given text")
    code_example: str = Field(..., description="A code example related to the topic")
    
    
