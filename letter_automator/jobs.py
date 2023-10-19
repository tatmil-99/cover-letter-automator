class Job:
    """Represents jobs applied to"""

    applications = {}
    total = 0

    def __init__(self, company, position, date):
        self.company = company.lower()
        self.position = position.lower()
        self.date = date
        Job.total += 1

    def update_company(self, company):
        old_company = self.company
        self.company = company.lower()
        new_company = self.company
        Job.update_key(new_company, old_company)

    def update_position(self, position):
        self.position = position.lower()

    # Need to list all applications to specific company (as tuple)?
    @classmethod
    def get_job(cls, job, print_obj=False):
        try:
            job_stored = cls.applications[job.lower()]
        except KeyError:
            print(f"Could not find job: {job}.")
        else:
            if print_obj:
                print(f"Found: {job_stored}")
                print(f"Company: {job_stored.company}")
                print(f"Position: {job_stored.position}")
            else:
                return job_stored

    @classmethod
    def update_key(cls, new, old):
        cls.applications[new] = cls.applications.pop(old)
        # print(cls.applications)

    @classmethod
    def store(cls, job):
        cls.applications[job.company] = job
        print(cls.applications)

    @classmethod
    def delete_job(cls, job):
        try:
            del cls.applications[job]
            print(f"Deleting job: {job}")
            Job.total -= 1
        except KeyError:
            print(f"Could not find job: {job}.")
