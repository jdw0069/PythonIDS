import nmap_ids
import ettercap_ids
import multiprocessing

<<<<<<< HEAD

t1 = multiprocessing.Process(
    target=nmap_ids.xmas_signature_detection, kwargs={'interface': 'eth0', 'continous': True})
t2 = multiprocessing.Process(
    target=nmap_ids.ack_signature_detection, kwargs={'interface': 'eth0', 'continous': True})
t3 = multiprocessing.Process(
    target=nmap_ids.syn_signature_detection, kwargs={'interface': 'eth0', 'continous': True})
t4 = multiprocessing.Process(
    target=ettercap_ids.heuristic_detection, kwargs={'interface': 'eth0', 'continous': True})
t5 = multiprocessing.Process(
    target=ettercap_ids.behavioral_detection, kwargs={'interface': 'eth0', 'continous': True})



# starting thread 1
t1.start()
# starting thread 2
t2.start()
# starting thread 3
t3.start()
# starting thread 4
t4.start()
# starting thread 5
t5.start()

# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()
# wait until thread 3 is completely executed
t3.join()
# wait until thread 4 is completely executed
t4.join()
# wait until thread 5 is completely executed
t5.join()

# both threads completely executed
print("Done!")
=======
"""
Main IDS Driver

Author: Jordan Sosnowski
Date: Dec 6, 2019
"""


def main():
    """
    Uses multi threading to run each IDS attack sniffer.

    NOTE: definitely not the most optimal solution. But due to our implementation
    for our IDS our code is segregated for each for loop. To then run them at the same time
    we would either need to re-write the code or run the sniffers all at once.

    """
    t1 = multiprocessing.Process(
        target=nmap_ids.xmas_signature_detection, kwargs={'interface': 'eth0', 'continuous': True})
    t2 = multiprocessing.Process(
        target=nmap_ids.ack_signature_detection, kwargs={'interface': 'eth0', 'continuous': True})
    t3 = multiprocessing.Process(
        target=nmap_ids.syn_signature_detection, kwargs={'interface': 'eth0', 'continuous': True})

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
    # starting thread 2
    t3.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
    # wait until thread 2 is completely executed
    t3.join()

    # both threads completely executed
    print("Done!")


if __name__ is "__main__":
    main()
>>>>>>> cc28a1d8d673347bb94f43acc453976cb26de2ae
