from .base import BaseCloudProvider


class HostRoyale(BaseCloudProvider):
    domains = [
    ]
    asns = [
        203020, 207990
    ]
    provider_type = "cloud"
