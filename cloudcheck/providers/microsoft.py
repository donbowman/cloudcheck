from .base import BaseCloudProvider


class Microsoft(BaseCloudProvider):
    provider_type = "corp"
    asns = [
    8075
    ]
    static_ranges = [
        "40.80.0.0/12",
        "40.125.0.0/17",
        "40.74.0.0/15",
        "40.112.0.0/13",
        "40.96.0.0/12",
        "40.76.0.0/14",
        "40.124.0.0/16",
        "40.120.0.0/14",
        "4.192.0.0/12",
        "52.224.0.0/11",
        "20.36.0.0/14",
        "20.40.0.0/13",
        "20.33.0.0/16",
        "20.128.0.0/16",
        "20.48.0.0/12",
        "20.64.0.0/10",
        "20.34.0.0/15",
        "20.0.0.0/11",
        "104.208.0.0/13",
        "4.240.0.0/12"
    ]
    domains = [
    ]

    ips_url = "https://endpoints.office.com/endpoints/Worldwide?ClientRequestId=b10c5ed1-bad1-445f-b386-b919946339a7"

    def parse_response(self, response):
        ranges = set()

        for range in self.static_ranges:
            ranges.add(range)
        for para in response.json():
            for range in para.get('ips', []):
                ranges.add(range)
            for url in para.get('urls', []):
                self.domains.append(url)
        return ranges
