Clones objects form a protypical instance. A registry keeps track of the cloneable instances.

# Uses

* Saving resources when object initilaisation is expensive e.g. object creation requires some sort of I/O
* Simplifying code where object initialisation is complex
* Where classes to be instantiated are decided at runtime (more important for statically typed languages)
* Potential Uses:
    - Data that needs processed prior to other uses
    - Constructor sets up a DB

# Advantages

* Can reduce subclassing - just get a prebuilt object with suitable values instead
* Can easily iterate over a list of protypes - harder to iterate over methods or classes (depending on language)
* Client can create duplicates without knowing anything about how to create them - they can simply ask the registry for
  a copy of the prototype
* Cloning tends to be less expensive than creating a new object from scratch; this is not really releavnt to python and
  applies more to C#, Java and other lower level languages

# Disadvantages

* Requires initialization - prototypes will need to be created