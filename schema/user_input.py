from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal

# Define request body schema
class UserInput(BaseModel):
    Age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the Patient")]
    Diabetes: Annotated[bool, Field(..., description="Is the Patient Diabetic or not")]
    BloodPressureProblems: Annotated[bool, Field(..., description="Does Patient have BP problems?")]
    AnyTransplants: Annotated[bool, Field(..., description="Has Patient undergone any transplants?")]
    AnyChronicDiseases: Annotated[bool, Field(..., description="Does Patient have chronic diseases?")]
    Height: Annotated[float, Field(..., description="Height of the Patient (in meters)")]
    Weight: Annotated[float, Field(..., description="Weight of the Patient (in kg)")]
    KnownAllergies: Annotated[bool, Field(..., description="Does Patient have any allergies?")]
    HistoryOfCancerInFamily: Annotated[bool, Field(..., description="Family history of cancer?")]
    NumberOfMajorSurgeries: Annotated[
        Literal[0, 1, 2, 3], Field(..., description="Number of major surgeries Patient had")
    ]

    # Computed fields
    @computed_field
    @property
    def bmi(self) -> float:
        return self.Weight / (self.Height**2)
