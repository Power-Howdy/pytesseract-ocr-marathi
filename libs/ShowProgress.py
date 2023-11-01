import time

total_iterations = 100
for iteration in range(total_iterations):
    progress = iteration + 1
    print(f"Progress: {progress}/{total_iterations}", end='\r')
    time.sleep(0.1)  # Simulate some work
    
print("Progress: Done!")