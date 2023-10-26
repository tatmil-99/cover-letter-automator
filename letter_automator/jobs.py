class Job:
    """Represents jobs applied to"""

    applications = {}
    total = 0

    def __init__(self, company, position, date):
        self.company = company.lower()
        self.position = position.lower()
        self.date = date
        Job.total += 1

    # Need to list all applications to specific company (as tuple)?
    # use built-in getattr() method?
    @classmethod
    def get_job(cls, company, position=None, print_obj=False):
        for number in cls.applications:
            job = cls.applications[number]

            if company.lower() == job.company:
                if print_obj:
                    print(f"Found: {job}")
                    print(f"Company: {job.company}")
                    print(f"Position: {job.position}")
                    return
                elif position and position.lower() == job.position:
                    return number
                else:
                    return job

        print(f"Could not find job in storage.")

    @classmethod
    def store(cls, job):
        cls.applications[cls.total] = job
        print(cls.applications)

    @classmethod
    def delete(cls, number):
        del cls.applications[number]
        print("Deleting job")
        cls.total -= 1
