from pyasic.miners._backends import CGMiner  # noqa - Ignore access to _module
from pyasic.miners._types import S19j  # noqa - Ignore access to _module


class CGMinerS19j(CGMiner, S19j):
    def __init__(self, ip: str) -> None:
        super().__init__(ip)
        self.ip = ip

    async def get_hostname(self) -> str:
        return "?"