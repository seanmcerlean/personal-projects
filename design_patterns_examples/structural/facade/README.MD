Wrap a complicated subsystem with a simpler interface or provide a unified interface to a set of interfaces.
Encapsulates or hideds an orginal system

# Uses

* Public facing API calling into microservices
* Standard interfaces to ports

# Pros

* API User does not have to understand the full subsystem; can get up to speed faster

# Cons

* May limit flexibility - not all functionality of the subsystem will be available to the client

# Notes

* Creates a new interface - compare other patterns that use or extend an old one
* Real life example - a customer service representative on the phone could be considered a facade
* Very useful if you only use a subset of the underlying system
* Stateless facades are often implemented as a singleton