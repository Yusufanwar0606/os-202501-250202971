import time
import os

def stress_test():
    print("--- Memulai Stress Test ---")
    print(f"PID: {os.getpid()}")
    
    # Simulasi Penggunaan Memori (Alokasi list besar)
    try:
        print("Mengalokasikan memori...")
        memory_hog = []
        for i in range(1, 11):
            # Menambah sekitar 50MB setiap iterasi
            memory_hog.append(' ' * (50 * 1024 * 1024)) 
            print(f"Alokasi ke-{i}: ~{i * 50} MB digunakan.")
            time.sleep(1)
            
        # Simulasi Penggunaan CPU (Perhitungan berat)
        print("Memulai beban CPU (10 detik)...")
        end_time = time.time() + 10
        while time.time() < end_time:
            _ = 1000 * 1000  # Operasi CPU
            
        print("Test selesai dengan sukses!")
        
    except MemoryError:
        print("\n[ERROR] Memory Limit Terlampaui! (OOM)")
    except Exception as e:
        print(f"\n[ERROR] Terjadi kesalahan: {e}")

if __name__ == "__main__":
    stress_test()