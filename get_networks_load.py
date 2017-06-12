from random import uniform
import time as ping
import matplotlib.pyplot as plt
from all_api_methods import get_nets
import save_graph
from variable_load import split_on_equal_parts, split_on_difference_parts
from thread_upgrade import ThreadWithReturnValue
from urls import BASE_URL, LAT_ALL_NETWORKS, LONG_ALL_NETWORKS

LAT_MAX = 48.425550
LAT_MIN = 48.425850
LONG_MAX = 35.02400
LONG_MIN = 35.02100
TIME_LOAD_DURATION = 10


def threadStart(number, ping_arr):
    for i in range(number):
        ping.sleep(ping_arr[i])
        threads[i] = ThreadWithReturnValue(target=get_nets, args=[req_list[i]])
        threads[i].start()


def threadEnd(number):
    arr = list()
    for i in range(number):
        arr.append(threads[i].join())
    return arr


def generate_list_of_urls(number, lat_minim, lat_maxim, long_minim, long_maxim):
    list_of_urls = list()
    i = 0
    while i < number:
        lat_rand = uniform(lat_minim, lat_maxim)
        long_rand = uniform(long_minim, long_maxim)
        req_url = BASE_URL + LAT_ALL_NETWORKS + \
                  str(lat_rand) + LONG_ALL_NETWORKS + str(long_rand)
        list_of_urls.append(req_url)
        i = i + 1
    return list_of_urls


if __name__ == '__main__':
    thread_count = 10
    max_thread_count = 20
    users_number = list()
    average_load_list = list()
    max_load_list = list()
    min_load_list = list()
    while thread_count <= max_thread_count:
        req_list = generate_list_of_urls(thread_count, LAT_MIN, LAT_MAX,
                                         LONG_MIN, LONG_MAX)
        ping_arr = split_on_difference_parts(TIME_LOAD_DURATION, thread_count)
        results = [None] * thread_count
        threads = [None] * thread_count
        threadStart(thread_count, ping_arr)
        thr = threadEnd(thread_count)
        print(thr)
        average_load = (sum(thr)/len(thr))
        min_load = min(thr)
        min_load_list.append(min_load)
        max_load = max(thr)
        max_load_list.append(max_load)
        users_number.append(thread_count)
        thread_count = thread_count+10
        average_load_list.append(average_load)
    print(average_load_list)
    print(min_load_list)
    print(max_load_list)
    print(users_number)
    fig = plt.figure()
    graph_avg = plt.plot(users_number, average_load_list, color='blue')
    graph_avg = plt.plot(users_number, max_load_list, color='magenta')
    graph_avg = plt.plot(users_number, min_load_list, color='green')
    plt.show()
    save_graph.save(name=fig)