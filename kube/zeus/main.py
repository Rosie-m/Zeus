from typing import Union, List
from fastapi import Depends, FastAPI
from pydantic import BaseModel, validator
from uuid import uuid4, UUID
from models import JobSpec, JobPhase, JobInfo, TrialResult, TrialInfo, TrialInfoList, ProfilingResult, ProfilingInfo, ProfilingRecord, TrainingPhase
from server import ZeusServer, get_global_zeus_server

app = FastAPI()

@app.post("/jobs/register")
async def register_job(
    job: JobSpec,
    zeus_server: ZeusServer = Depends(get_global_zeus_server),
) -> None:
    """Endpoint for users to register a new job."""
    # job_dict = job.dict()
    # job_id = uuid4()
    # job_dict.update({"job_id": job_id})
    # zeus_server.register_job(job_dict)
    pass


@app.get("/jobs", response_model=List[JobInfo])
async def get_job_info(
    zeus_server: ZeusServer = Depends(get_global_zeus_server),
) -> List[JobInfo]:
    """Endpoint for users to query the jobs submitted."""
    # TODO: add filtering conditions
    return [JobInfo(uuid4(), "luoxim", JobSpec(), JobPhase.Running)]

@app.post("/jobs/terminate")
async def terminate_job(
    job_id: UUID,
    zeus_server: ZeusServer = Depends(get_global_zeus_server),
) -> None:
    """Endpoint for users to terminate a job."""
    # zeus_server.terminate_job(job_id)


@app.post("/trials/report_trial_result")
async def report_trial_result(
    job_id: UUID,
    rec_i: int,
    trial_i: int,
    trial_result: TrialResult,
    zeus_server: ZeusServer = Depends(get_global_zeus_server),
):
    """Endpoint for trials (PytorchJob) to report results (energy, time, cost, num_epochs, reached) at exit."""
    # PytorchJob reports the training results at the end.
    # The result will be send from here to the AsyncTask
    # (running at ZeusServer) w/ a channel.
    # zeus_server.report_trial_result(job_id, rec_i, trial_i, trial_result)

@app.get("/trials", response_model=List[TrialInfo])
async def get_trial_info(
    job_id: UUID,
    rec_i: Union[int, None] = None,
    trial_i: Union[int, None] = None,
    zeus_server: ZeusServer = Depends(get_global_zeus_server),
) -> List[TrialInfo]:
    """Endpoint for users to query trials."""
    # Return 400 when found invalid parameters
    # zeus_server.get_trial_info(job_id, rec_i, trial_i)


@app.post("/trials/report_profiling_result")
async def report_profiling_result(
    job_id: UUID,
    batch_size: int,
    profiling_result: ProfilingResult,
    rec_i: int,
    trial_i: int,
    zeus_server: ZeusServer = Depends(get_global_zeus_server),
) -> None:
    """Endpoint for trials (PytorchJob) to report power results when profiling is done."""
    # zeus_server.report_profiling_result(job_id, batch_size, profiling_result, rec_i, trial_i)


@app.get("/profiling", response_model=ProfilingInfo)
async def get_profiling_info(
    job_id: UUID,
    zeus_server: ZeusServer = Depends(get_global_zeus_server),
) -> ProfilingInfo:
    """Endpoint for users to get profiling results for a job."""
    # return await zeus_server.get_profiling_info(job_id)
    return ProfilingInfo(
        uuid4(),
        {
            32: ProfilingResult(
                ProfilingRecord(
                    TrainingPhase.Train,
                    300000,
                    ProfilingValueType.Power,
                    131.93493277891338,
                )
            ),
        }
    )

 
