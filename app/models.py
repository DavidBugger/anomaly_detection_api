from pydantic import BaseModel, Field
from typing import List

class LoginFeatures(BaseModel):
    UsernameEncoded: int = Field(..., description="Encoded username")
    EventID_Encoded: float = Field(..., description="Encoded event ID")
    IPInteger: float = Field(..., description="Integer representation of the IP address")
    LogonCount: float = Field(..., description="Number of times the user has logged on")
    Hour: float = Field(..., description="Hour of the login attempt")
    TimeDiff: float = Field(..., description="Time difference between login attempts")

    def preprocess(self) -> List[float]:
        """Preprocesses the data by normalizing or transforming if needed."""
        # Add custom preprocessing logic if necessary.
        # For simplicity, we'll assume that the data is already in a suitable format for prediction.
        return [
            self.UsernameEncoded,
            self.EventID_Encoded,
            self.IPInteger,
            self.LogonCount,
            self.Hour,
            self.TimeDiff
        ]
