def fifo_page_replacement(pages, capacity):
    memory = []
    page_faults = 0
    for page in pages:
        if page not in memory:
            if len(memory) >= capacity:
                memory.pop(0)
            memory.append(page)
            page_faults += 1
    return page_faults

def lru_page_replacement(pages, capacity):
    memory = []
    page_faults = 0
    for page in pages:
        if page not in memory:
            if len(memory) >= capacity:
                memory.pop(0)
            memory.append(page)
            page_faults += 1
        else:
            memory.remove(page)
            memory.append(page)
    return page_faults


reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
frames = 3

print(f"--- Hasil Simulasi Yusuf Anwar (NIM: 250202971) ---")
print(f"Reference String: {reference_string}")
print(f"Jumlah Frame    : {frames}")
print(f"-" * 45)
print(f"FIFO Page Faults: {fifo_page_replacement(reference_string, frames)}")
print(f"LRU Page Faults : {lru_page_replacement(reference_string, frames)}")
print(f"-" * 45)