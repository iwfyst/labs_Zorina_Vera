## сборка компа
from dataclasses import dataclass


@dataclass(frozen=True)
class Computer:
    cpu: str
    ram_gb: int
    gpu: str
    storage: tuple[str, ...]


class ComputerBuilder:
    def __init__(self, cpu: str, ram_gb: int):
        self.cpu = cpu
        self.ram_gb = ram_gb
        self.gpu = "Встроенная графика"
        self.storage: list[str] = []

    def set_gpu(self, gpu: str) -> "ComputerBuilder":
        self.gpu = gpu
        return self

    def add_storage(self, drive: str) -> "ComputerBuilder":
        self.storage.append(drive)
        return self

    def build(self) -> Computer:
        return Computer(
            cpu=self.cpu,
            ram_gb=self.ram_gb,
            gpu=self.gpu,
            storage=tuple(self.storage),
        )


def build_gaming_pc(builder: ComputerBuilder) -> Computer:
    return (
        builder
        .set_gpu("NVIDIA RTX 4080")
        .add_storage("NVMe SSD 1TB")
        .add_storage("SATA SSD 2TB")
        .build()
    )


if __name__ == "__main__":
    office_pc = (
        ComputerBuilder(cpu="Intel Core i5", ram_gb=16)
        .add_storage("NVMe SSD 512GB")
        .build()
    )
    print("Офисный ПК:", office_pc)

    gaming_pc = build_gaming_pc(ComputerBuilder(cpu="AMD Ryzen 7", ram_gb=32))
    print("Игровой ПК:", gaming_pc)
