from typing import List


class CloudProvider:
    def connect(self) -> None:
        pass

    def disconnect(self) -> None:
        pass

    def load(self, data: bytes, destination: str) -> str:
        pass

    def list(self, recurse: bool) -> List[str]:
        pass
