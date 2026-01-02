def simulate_fifo(pages, capacity):
    memory = []
    page_faults = 0
    print(f"\nSimulasi FIFO ({capacity} Frames):")
    
    for page in pages:
        if page not in memory:
            if len(memory) >= capacity:
                memory.pop(0)  
            memory.append(page)
            page_faults += 1
            status = "MISS (Fault)"
        else:
            status = "HIT"
        print(f"Page {page} -> Memory: {memory} | {status}")
    
    return page_faults

def simulate_lru(pages, capacity):
    memory = []
    page_faults = 0
    print(f"\nSimulasi LRU ({capacity} Frames):")
    
    for page in pages:
        if page not in memory:
            if len(memory) >= capacity:
                memory.pop(0) 
            memory.append(page)
            page_faults += 1
            status = "MISS (Fault)"
        else:
            
            memory.remove(page)
            memory.append(page)
            status = "HIT"
        print(f"Page {page} -> Memory: {memory} | {status}")
        
    return page_faults


reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frames = 3

fifo_faults = simulate_fifo(reference_string, frames)
lru_faults = simulate_lru(reference_string, frames)

print("\n" + "="*30)
print(f"Total Page Fault FIFO: {fifo_faults}")
print(f"Total Page Fault LRU:  {lru_faults}")