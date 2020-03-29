This is an app of resources.

For this phase we implement all of the following tasks:

1. Register as a system administrator.
2. Register as a person in need of resources.
3. Register as a person that supplies resources.
4. Add a request for a given resource
5. Announce the availability of a resource.
6. Reserve or purchase a resource. Free resources are reserved. Otherwise, they are
purchased.
7. Browse resources being requested
8. Browse resources available
9. See detail of resources, including location on a Google Map
10. Keyword search resources being requested, with sorting by resource name
11. Keyword search resources available, with sorting by resource name
12. Show dashboard page with daily statistics on
a. Resources in need
b. Resources available
c. Matching between need and availability
13. Show dashboard page with trending statics (7 day period) on
a. Resources in need
b. Resources available
c. Matching between need and availability
14. Show dashboard page with trending statics (8 Senate Regions in PR) on
a. Resources in need
b. Resources available
c. Matching between need and availability

This is  a working site. However, this system is not the full fledged system, but rather an initial
version with the following capabilities:
a. Each task can be performed through the REST API.
b. The actions in API calls will trigger a call to the appropriate controller.
c. The controller will respond with a JSON result that is “hard-wired”.
