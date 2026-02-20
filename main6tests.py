import main6functions
import time
import matplotlib.pyplot as plt

### TESTING ###

#array testing sizes
sizes = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]

#number of trials done
sample_size = 100000

#k values tested
#k_values = [48, 52, 56, 60, 64, 68, 72, 76, 80]
#k_values = [48, 64]
k_values = [48]

#Insertion sort testing
insertion_sort_times = []

for i in range(len(sizes)):
    c_time = 0
    for _ in range(sample_size):
        array = main6functions.generate_array(sizes[i])

        start_time = time.perf_counter()
        main6functions.main6_insertion_sort(array)
        end_time = time.perf_counter()

        c_time += end_time - start_time

    insertion_sort_times.append(c_time / sample_size)




#Merge sort testing

merge_sort_times = []
for i in range(len(sizes)):
    c_time = 0
    for _ in range(sample_size):
        array = main6functions.generate_array(sizes[i])

        start_time = time.perf_counter()
        main6functions.main6_merge_sort(array)
        end_time = time.perf_counter()

        c_time += end_time - start_time

    merge_sort_times.append(c_time / sample_size)

#Tim sort testing

#first test speeds of different k values
#at each k value, how long does it take (on average) to sort an array of size n
tim_sort_times_dict = {}
for k in k_values:
    time_sort_times_at_k = []
    for i in range(len(sizes)):
        c_time = 0
        for _ in range(sample_size):
            array = main6functions.generate_array(sizes[i])

            start_time = time.perf_counter()
            main6functions.main6_tim_sort(array, k)
            end_time = time.perf_counter()

            c_time += end_time - start_time

        time_sort_times_at_k.append(c_time / sample_size)
    tim_sort_times_dict[k] = time_sort_times_at_k
    print("done: " + str(k) + '\n')

print(tim_sort_times_dict)

#plot tim k values
for k in k_values:
    plt.plot(sizes, tim_sort_times_dict[k], label = str(k))
plt.plot(sizes, insertion_sort_times, label="Insertion Sort")
plt.plot(sizes, merge_sort_times, label="Merge Sort")
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Algorithm Runtime")
plt.legend()
plt.show()

#find lowest time
k_value_times = []
for k in k_values:
    total = 0
    for value in tim_sort_times_dict[k]:
        total += value
    k_value_times.append(total)

for i in range(len(k_values)):
    min_index = 0
    min = 99999999999999999999
    if k_value_times[i] < min:
        min = k_value_times[i]
        min_index = i

print("min_index: " + str(min_index))




## Graph insertion sort
"""
plt.plot(sizes, insertion_sort_times, label="Insertion Sort")
plt.plot(sizes, merge_sort_times, label="Merge Sort")
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Algorithm Runtime")
plt.legend()
plt.show()
"""