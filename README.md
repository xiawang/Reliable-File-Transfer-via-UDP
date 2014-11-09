Reliable-File-Transfer-via-UDP
==============================

Harvey Mudd College / USC Computer Network Project-1

Author: Chris Brown / Xiaotian Wang

The project is using Python socket library to program a UDP utility of reliable file transfer.


Environment being tested
==============================

The testing environment is somewhat rediculous:

| Link Speed  | RTT        | Loss rate   | Throughput                       |
| ----------- | ---------- | ----------- | -------------------------------  |
| 100Mbp/s    | 10 ms      | 1%          |  186 KB                          |
| 100Mbp/s    | 200 ms     | 20%         |  being tested                    |


Things being improved
==============================

1. ACK via UDP (TCP before)
2. ACK with bit map (list before)
