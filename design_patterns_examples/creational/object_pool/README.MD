Avoid create new objects by asking a pool for one that has already been instantiated

# Uses

* Used where the cost of creatig and destroying objects repatedly is high
* Potential Uses:
    - Pools of connections - databases, sockets etc

# Advantages

* Can improve performance where
    - Cost of object creation is high
    - Object use is high
    - Number of objects used at one time is low OR
      objects are used for a short amount of time

# Disadvantages

* Requires initialization - pool objects will need created
    - Could be done lazily when required
* Requires more care on behalf of the programmer with regards to
    - Object state
        - Stale state could cause the object to behave differently
        - Information leak - data could be leaked if not cleared properly
    - Parallelism
        -Appropriate synchronisation will need used if pool is shared by multiple threads
* May not be efficient in many cicumstances
    - If a pool is not neeede dor the cost of creation is not high, may be more inefficient
    - May impact GC in some languages

# Options when all objects are in use

* Return and error or exception for the client to handle
* Allocate a new object
    - Normally a high watermark would be used to stop unbounded growth
* Block until an object becomes free
    - WIll degrade performance

# Notes

* Object pools are often singletons, to ensure all reusable objects are managed by the same policy