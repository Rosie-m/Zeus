
from __future__ import annotations

import asyncio

GLOBAL_ZEUS_SERVER: ZeusServer | None = None

class ZeusServer:
    """A singleton class that manages training jobs."""

    def __init__(
        self
    ) -> None:
        """Initialize the server."""
        # Initialize BSO

        # Initialize JobLauncher?

        # Ensure DBServer is ready?
        pass

    # async def register_job(
    #     self,
    #     job: JobSpec,
    # ) -> None:
    #     """Register a user-submitted job."""
    #     # TODO: Append the job to Jobs table by POST to DBServer
    #     await DBAPI.insert_job(job_dict)

    #     # Run the job
    #     await self.run_job(job)

    async def report_trial_result(
        self,
        result: TrialResult,
    ) -> None:
        """Update the completed Trial record in Trials table."""


    async def run_job(
        self,
        job: JobSpec,
    ) -> None:
        """Run one user-submitted job."""
        # Keep a reference to the `asyncio.Task`s, to avoid a task disappearing mid-execution.
        # background_recurrences = set()
        # for rec_i in range(num_recurrences):

        #     # Create an `asyncio.Task` to run the recurrence
        #     recurrence = asyncio.create_task(run_recurrence(job, rec_i))

        #     # Record the recurrence `Task`
        #     background_recurrences.add(recurrence)

        #     # Wait for time trigger or drift detection trigger
        #     await time_for_next_recurrence()

        

        

    
    async def run_recurrence(
        self,
        job: JobSpec,
        rec_i: int,
    ) -> None:
        """Run one recurrence for a job."""
        # for trial_i in range(max_retries):
        #     bs = bso.predict(job)

        #     await create_trial(job, rec_i, trial_i)
        #     await DB.insert_trial(job, rec_i, trial_i)

        #     # Wait for trial to complete
            
        #     await DBAPI.update_trial()
        #     # Provide feedback to the BSO.
        #     bso.observe(job, bs, cost, reached)

        #     # Reached the target metric. Go to next recurrence.
        #     if reached:
        #         break


def get_global_zeus_server() -> ZeusServer:
    """Fetch the global singleton `ZeusServer`."""
    return GLOBAL_ZEUS_SERVER