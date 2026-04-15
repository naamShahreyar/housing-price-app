from pydantic import BaseModel, Field
from typing import Annotated


class HouseInput(BaseModel):
    MedInc: Annotated[float, Field(..., description="Median income in block group", examples=[3.5])]
    HouseAge: Annotated[float, Field(..., description="Age of house", examples=[25.0])]
    AveRooms: Annotated[float, Field(..., description="Average number of rooms per household", examples=[5.0])]
    AveBedrms: Annotated[float, Field(..., description="Average number of bedrooms per household", examples=[1.0])]
    Population: Annotated[float, Field(..., description="Population in block group", examples=[1000.0])]
    AveOccup: Annotated[float, Field(..., description="Average number of household members", examples=[3.0])]
    Latitude: Annotated[float, Field(..., description="Latitude of block group", examples=[37.88])]
    Longitude: Annotated[float, Field(..., description="Longitude of block group", examples=[-122.23])]


class PredictionOutput(BaseModel):
    prediction: float