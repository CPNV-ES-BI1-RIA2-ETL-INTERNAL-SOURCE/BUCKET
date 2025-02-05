class CloudProvider:
    def connect(self) -> None:
        pass

    def disconnect(self) -> None:
        pass

    def load(self, data: str) -> str:
        pass