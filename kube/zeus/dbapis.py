class DBAPI:
    def __init__(
        self,
    ) -> None:
        pass
        # QA: Do we want to maintain any states for DB at ZeusServer?

    async def insert_job() -> None:
        pass

    async def update_job() -> None:
        """User might want to terminate a job. Update a job status from Running to Completed."""
        pass

    async def insert_trial() -> None:
        """Insert to Trials table when a trial is created."""
        # Trials saves the same contents of train_json
        pass

    async def update_trial() -> None:
        """Update a trial in Trials table when it is completed."""
        pass

    async def insert_power() -> None:
        """Insert to Power table after each profile window."""
        # Power saves the same contents of power_json
        pass
