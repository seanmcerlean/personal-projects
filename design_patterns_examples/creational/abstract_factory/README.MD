Provide an interface for creating families of related or dependent objects without specifying their concrete classes

"Factory of Factories"

# Uses

* Dependency injection
* Most referenced practical use appears to be separating out GUI implementations e.g Factory for Windows GUI widgets, MAC OS GUI widgets etc

# Advantages

* Isolates object creation from use
* Exchanging product families does not break code
* Promotes consistency among products

# Disadvantages

* Extending thr abstract interface (e.g. for a new product) implies all concrete classes much change