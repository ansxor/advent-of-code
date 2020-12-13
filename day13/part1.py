file = open('input.txt', 'r')

earliest_timestamp = int(file.readline())

ids = [int(x.strip()) for x in file.readline().split(',') if x != 'x']
leave_times = [x * ((earliest_timestamp // x) + 1) for x in ids]

index = leave_times.index(min(leave_times))

solution = (leave_times[index] - earliest_timestamp) * ids[index]

print(solution)
