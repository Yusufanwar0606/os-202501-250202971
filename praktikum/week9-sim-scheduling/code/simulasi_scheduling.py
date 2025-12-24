import pandas as pd

# Dataset proses
processes = [
    {"Process": "P1", "Arrival": 0, "Burst": 6},
    {"Process": "P2", "Arrival": 1, "Burst": 8},
    {"Process": "P3", "Arrival": 2, "Burst": 7},
    {"Process": "P4", "Arrival": 3, "Burst": 3},
]

# -------------------------------
# Algoritma FCFS
# -------------------------------
def fcfs(processes):
    processes = sorted(processes, key=lambda x: x["Arrival"])
    time = 0
    results = []
    for p in processes:
        start = max(time, p["Arrival"])
        finish = start + p["Burst"]
        turnaround = finish - p["Arrival"]
        waiting = turnaround - p["Burst"]
        results.append({
            "Process": p["Process"],
            "Arrival": p["Arrival"],
            "Burst": p["Burst"],
            "Start": start,
            "Finish": finish,
            "Waiting": waiting,
            "Turnaround": turnaround
        })
        time = finish
    return results

# -------------------------------
# Algoritma SJF (Non-preemptive)
# -------------------------------
def sjf(processes):
    processes = sorted(processes, key=lambda x: x["Arrival"])
    time = 0
    results = []
    ready_queue = []
    done = set()

    while len(results) < len(processes):
        # Tambahkan proses yang sudah tiba ke ready queue
        for p in processes:
            if p["Arrival"] <= time and p["Process"] not in done:
                ready_queue.append(p)
                done.add(p["Process"])

        if ready_queue:
            # Pilih proses dengan burst terkecil
            ready_queue.sort(key=lambda x: x["Burst"])
            p = ready_queue.pop(0)
            start = max(time, p["Arrival"])
            finish = start + p["Burst"]
            turnaround = finish - p["Arrival"]
            waiting = turnaround - p["Burst"]
            results.append({
                "Process": p["Process"],
                "Arrival": p["Arrival"],
                "Burst": p["Burst"],
                "Start": start,
                "Finish": finish,
                "Waiting": waiting,
                "Turnaround": turnaround
            })
            time = finish
        else:
            time += 1  # jika tidak ada proses siap, waktu maju

    return results

# -------------------------------
# Eksekusi & Output
# -------------------------------
def print_table(results, title):
    df = pd.DataFrame(results)
    print(f"\n=== {title} ===")
    print(df.to_string(index=False))
    print(f"Rata-rata Waiting Time: {df['Waiting'].mean():.2f}")
    print(f"Rata-rata Turnaround Time: {df['Turnaround'].mean():.2f}")

if __name__ == "__main__":
    fcfs_results = fcfs(processes)
    sjf_results = sjf(processes)

    print_table(fcfs_results, "FCFS Scheduling")
    print_table(sjf_results, "SJF Scheduling (Non-preemptive)")
