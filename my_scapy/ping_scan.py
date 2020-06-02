#!/usr/bin/env python3

from scapy.all import *

def icmp_ping(destination):
    # regular ICMP ping
    ans, unans = sr(IP(dst=destination)/ICMP())
    return ans

def tcp_ping(destination, dport):
    ans, unans = sr(IP(dst=destination)/TCP(dport=dport,flags="S"))
    return ans

def udp_ping(destination):
    ans, unans = sr(IP(dst=destination)/UDP(dport=0))
    return ans

def answer_summary(ans):
    for send, recv in ans:
        print(recv.sprintf("%IP.src% is alive"))


def main():
    print("** ICMP Ping **")
    ans = icmp_ping("192.168.200.2-3")
    answer_summary(ans)
    print("** TCP Ping ***")
    ans = tcp_ping("192.168.200.2", 22)
    answer_summary(ans)
    print("** UDP Ping ***")
    ans = udp_ping("192.168.200.2-3")
    answer_summary(ans)


if __name__ == "__main__":
    main()
