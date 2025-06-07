from system import LibrarySystem
from observer import Pengunjung, Anggota, Pegawai, Admin

def main():
    system = LibrarySystem()

    pengunjung = Pengunjung()
    anggota = Anggota()
    pegawai = Pegawai()
    admin = Admin()

    system.add_observer(pengunjung)
    system.add_observer(anggota)
    system.add_observer(pegawai)
    system.add_observer(admin)

    system.add_book("National Geographic - Supercomputer")
    system.generate_report("Bulanan Peminjaman")

if __name__ == "__main__":
    main()
