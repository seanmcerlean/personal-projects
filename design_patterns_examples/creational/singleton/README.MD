Class with only one instance

# Uses

Most commonly cited example is a logger.
All functions need to use it, passing it as a dependency would be excessive

# Advantages

Instance control - ensures that all objects access the same instance

# Disadvantages

Singletons are global state
Hide dependencies
Tight coupling
Hard to test - may be difficult to mock, may require ordering

# Advantages over global variables

Can be certain of the number of instances
Can be more easily refactored to be a non singleton

# Advantages over static class

Singletons are stored on heap, static methods on the stack
Can implement interfaces or derive form base classes
Static classes allow only static methods