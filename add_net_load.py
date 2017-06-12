from random import uniform
import time as ping
import matplotlib.pyplot as plt
from all_api_methods import add_net
import save_graph
from variable_load import split_on_equal_parts, split_on_difference_parts
from thread_upgrade import ThreadWithReturnValue
from urls import BASE_URL, ADD_NET_URL


LAT_MAX = 48.425550
LAT_MIN = 48.425850
LONG_MAX = 35.02400
LONG_MIN = 35.02100
TIME_LOAD_DURATION = 10


def threadStart(number, ping_arr):
    for i in range(number):
        ping.sleep(ping_arr[i])
        threads[i] = ThreadWithReturnValue(target=add_net,
                                           args=[BASE_URL + ADD_NET_URL,
                                                 data_list[i]])
        threads[i].start()


def threadEnd(number):
    arr = list()
    for i in range(number):
        arr.append(threads[i].join())
    return arr


def generate_list_of_data(start_index, number, lat_minim, lat_maxim, long_minim,
                          long_maxim):
    list_of_data = list()
    ssid = 'Test_ssid_name'
    password = 'Test_password_name'
    bssid = 'Test_password_bssid'
    i = 0
    while i < number:
        req_data = {'latitude':str(uniform(lat_minim, lat_maxim)),
                    'longitude':str(uniform(long_minim, long_maxim)),
                    'ssid':ssid+str(start_index+i),
                    'password':password+str(start_index+i),
                    'bssid':bssid+str(start_index+i)}
        list_of_data.append(req_data)
        i = i+1
    return list_of_data


if __name__ == '__main__':
    file_name = './text/add_net.txt'
    start = int()
    with open(file_name, 'r') as opened_file:
        start = int(opened_file.read())
    thread_count = 10
    users_number = list()
    average_load_list = list()
    max_load_list = list()
    min_load_list = list()
    while thread_count <= 10:
        data_list = generate_list_of_data(start, thread_count, LAT_MIN, LAT_MAX,
                                         LONG_MIN, LONG_MAX)
        ping_arr = [0] * thread_count
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
        start = start + thread_count
        thread_count = thread_count+10
        average_load_list.append(average_load)
    with open(file_name, 'w') as opened_file:
        opened_file.write(str(start))
    print(average_load_list)
    print(min_load_list)
    print(max_load_list)
    print(users_number)
    fig = plt.figure()
    graph_avg = plt.plot(users_number, average_load_list, color='blue')
    graph_avg = plt.plot(users_number, max_load_list, color='magenta')
    graph_avg = plt.plot(users_number, min_load_list, color='green')
    plt.show()