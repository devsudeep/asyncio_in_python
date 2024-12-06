
### AsyncIO
For I/O-bound workloads, there are exactly (only!) two reasons to use async-based concurrency over thread-based concurrency:

Asyncio offers a safer alternative to preemptive multitasking (i.e., using threads), thereby avoiding the bugs, race conditions, and other nondeterministic dangers that frequently occur in nontrivial threaded applications.

Asyncio offers a simple way to support many thousands of simultaneous socket connections, including being able to handle many long-lived connections for newer technologies like WebSockets, or MQTT for Internet of Things (IoT) applications.

