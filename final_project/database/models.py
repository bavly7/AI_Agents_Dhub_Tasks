from pydantic import BaseModel, Field
from typing import Optional, List, TypedDict

class Lead(BaseModel):
    company_name: str
    url: str
    email: Optional[str] = None
    is_qualified: Optional[bool] = None
    email_sent: bool = False
    reason: Optional[str] = None

class Qualifier(BaseModel):
    is_qualified: bool = Field(description="True if the website lacks an AI Chatbot and fits our target, False otherwise.")
    extracted_email: Optional[str] = Field(default=None, description="The contact email extracted from the website.")
    reason: str = Field(default="", description="A short explanation of why the company is qualified or not.")

class Closer(BaseModel):
    subject: str = Field(description="The subject line of the sales email.")
    body: str = Field(description="The personalized email body trying to sell the AI Chatbot services.")

class AgentState(TypedDict):
    search_query: str
    leads: List[dict]
    qualified_leads: List[dict]
    emails_sent: int