from fastapi import APIRouter
from fastapi.responses import JSONResponse
from hezar.models import Model
from pydantic import BaseModel

from ..logger import LOGGER

# ------------------------------ Initialization -------------------------------
router = APIRouter()


# ------------------------------ Models -------------------------------
class NLPayload(BaseModel):
    text: str


MODEL = Model.load("hezarai/bert-fa-sentiment-dksf")


# ------------------------------- Routers -------------------------------
@router.post(
    "/nlp-inference",
    status_code=200,
    tags=["ml"],
)
async def nlp_inference(
    payload: NLPayload,
):
    """NLP domain inference API"""
    try:
        results = MODEL.predict(payload.text)
        return {"res": results}

    except Exception as err:
        LOGGER.critical("Unknown error in inference!", exc_info=err)
        return JSONResponse(status_code=500, content={"msg": "Error in inference."})
