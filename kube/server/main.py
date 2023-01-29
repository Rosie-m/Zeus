from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4, UUID

app = FastAPI()

class JobSpec(BaseModel):
    seed: int = 1
    b_0: int = 1024
    b_min: int = 8
    b_max: int = 4096
    eta_knob: float = 0.5
    beta_knob: float = 2.0
    target_metric: float = 0.50

@app.post("/register/")
async def register_job(job: JobSpec):
    job_dict = job.dict()
    job_id = uuid4()
    job_dict.update({"job_id": job_id})
    return job_dict

# TODO: Query JobInfo from DBServer and reply; response_model=JobInfo
@app.get("/job/{job_id}")
async def query_job(job_id: UUID):
    return job_id

@app.post("/trial/report_metric/")
async def report_trial_metric():