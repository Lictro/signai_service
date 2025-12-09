from fastapi import APIRouter
from app.api.schemas import KeypointsInput
from app.services.predict_service import predict_sign

router = APIRouter()

@router.post("/predict")
def predict(data: KeypointsInput):
    prediction = predict_sign(data.keypoints)
    return {"prediction": prediction}
