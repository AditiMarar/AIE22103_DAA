def calculate_sunny_population(towns, populations, locations, clouds, cloud_locations, cloud_ranges):
    max_population = sum(populations)
    
    for i in range(clouds):
        cloud_start = cloud_locations[i] - cloud_ranges[i]
        cloud_end = cloud_locations[i] + cloud_ranges[i]
        
        sunny_population = sum([populations[j] for j in range(towns) if locations[j] < cloud_start or locations[j] > cloud_end])
        
        max_population = max(max_population, sunny_population)
    
    return max_population

# Input processing
towns = int(input())
populations = list(map(int, input().split()))
locations = list(map(int, input().split()))
clouds = int(input())
cloud_locations = list(map(int, input().split()))
cloud_ranges = list(map(int, input().split()))

# Calculate the maximum number of people in a sunny town by removing exactly one cloud
result = calculate_sunny_population(towns, populations, locations, clouds, cloud_locations, cloud_ranges)
print(result)
