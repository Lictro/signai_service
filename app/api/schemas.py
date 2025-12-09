from pydantic import BaseModel
from typing import List

class KeypointsInput(BaseModel):
    keypoints: List[List[float]]
