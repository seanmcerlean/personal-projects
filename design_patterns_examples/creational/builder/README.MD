Builds a complex object using a stepwise approach

# Uses

* Common input with many possible representations
* Anywhere objects can't be built in a single step or the final object is mutable
* Practical Examples:
  - Building an arbirary HTML or GUI forms
  - Test data - i need a user with details X, Y, Z...
  - String Builder, query builders (may be no director)

# Advantages

* Avoids telescoping constructors - more parameters with various combinations that lead to explosive growth of constructors
* Can be used for objects that contain data that cannot be easily edited
* Allows finer control over object construction - single builder can make multiple objects
* Avoids having an object in an incomplete state if you have an empty constructor and getters / setters directly

# Disadvantages

Requires a separate concrete builder for each type of product

# Why is the Director Needed

Due to the responsibility principle.
The Builder class is responsible for creating the part. How the part is created might change e.g. HTML4 -> HTML5
The Director class is responsible for assembling parts into a particuar product, which may change.
If the Director was not there, the client would need to understand how the object is built.

It is possible to use Builder without a director

# Alternatives in Python

Named parameters and default paramter values reduce the problem of telescoping constructors in Python
Note that there are no truly immutable objects in Python, it's only by convention