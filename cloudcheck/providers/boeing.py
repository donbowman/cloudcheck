from .base import BaseCloudProvider


class Boeing(BaseCloudProvider):
    provider_type = "corp"

    domains = [
    ]
    def __init__(self, j):
        super(Boeing, self).__init__(j)
        ranges = {"130.76.128.0/19", "130.76.0.0/19", " 130.76.160.0/19"}
        self.update_ranges(ranges)

