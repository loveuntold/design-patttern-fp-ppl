from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class Pengunjung(Observer):
    def update(self, message):
        print(f"[Pengunjung] Notifikasi: {message}")

class Anggota(Observer):
    def update(self, message):
        print(f"[Anggota] Notifikasi: {message}")

class Pegawai(Observer):
    def update(self, message):
        print(f"[Pegawai] Notifikasi: {message}")

class Admin(Observer):
    def update(self, message):
        print(f"[Admin] Notifikasi: {message}")
