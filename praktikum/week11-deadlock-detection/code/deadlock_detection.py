import os
import csv

def jalankan_deteksi():
    nama_file = 'dataset_deadlock.csv'
    
    if not os.path.exists(nama_file):
        print(f"Error: File '{nama_file}' tidak ditemukan di folder yang sama.")
        return

    adj = {}
    semua_node = set()

    try:
        with open(nama_file, mode='r') as f:
            reader = csv.DictReader(f)
            for baris in reader:
                p = baris['Proses'].strip()
                alloc = baris['Allocation'].strip()
                req = baris['Request'].strip()

                if alloc not in adj: adj[alloc] = []
                adj[alloc].append(p)

                if p not in adj: adj[p] = []
                adj[p].append(req)

                semua_node.update([p, alloc, req])
    except KeyError:
        print("Error: Header CSV harus 'Proses', 'Allocation', 'Request'")
        return

    visited = set()
    stack = set()
    deadlock_proses = set()

    def cari_siklus(node, path_skrg):
        visited.add(node)
        stack.add(node)
        path_skrg.append(node)

        for tetangga in adj.get(node, []):
            if tetangga not in visited:
                if cari_siklus(tetangga, path_skrg):
                    return True
            elif tetangga in stack:
                idx = path_skrg.index(tetangga)
                untuk_ditandai = path_skrg[idx:]
                for n in untuk_ditandai:
                    if n.startswith('P'): 
                        deadlock_proses.add(n)
                return True

        stack.remove(node)
        path_skrg.pop()
        return False

    ada_deadlock = False
    for n in list(semua_node):
        if n not in visited:
            if cari_siklus(n, []):
                ada_deadlock = True

    print("\n" + "="*35)
    print("   LAPORAN DETEKSI DEADLOCK")
    print("="*35)
    
    if ada_deadlock:
        print(f"STATUS   : [!] TERDETEKSI DEADLOCK")
        print(f"PROSES   : {', '.join(sorted(deadlock_proses))}")
        print("-" * 35)
        print("Analisis: Terjadi 'Circular Wait'.")
        print("Proses di atas saling menunggu tanpa henti.")
    else:
        print("STATUS   : [+] SISTEM AMAN")
        print("Analisis: Tidak ditemukan siklus alokasi.")
    
    print("="*35 + "\n")

if __name__ == "__main__":
    jalankan_deteksi()