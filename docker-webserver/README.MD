# Docker Webserver

Simple Docker Example

- Sets up an Nginx webvserver container with a static
- Sets up a JMeter container that
    - Downloads and installs JMeter
    - Copies a JMX file
    - Executes the file

Docker-compose is used to set up and configure the congtainers, and mount volumes so JMeter results are
 accessible on the host machine