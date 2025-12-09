
def predict_sign(keypoints: list) -> str:
    """
    Dummy prediction service.
    Later you will replace this with a real AI model.
    """
    # For now, we just simulate a prediction
    if not keypoints:
        return "unknown"

    # TODO: replace this with real ML logic
    return "book"
