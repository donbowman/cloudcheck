from .base import BaseCloudProvider


class CenturyLink(BaseCloudProvider):
    provider_type = "hosting"

    domains = [
    ]
    def __init__(self, j):
        super(CenturyLink, self).__init__(j)
        ranges = {"205.169.39.0/24"}
        self.update_ranges(ranges)

