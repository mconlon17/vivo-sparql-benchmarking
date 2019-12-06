# vivo-sparql-benchmarking
Preliminary work to time VIVO SPARQL reads and writes.  TDB, SDB, other.

The basic idea:

* Generate sample data of various sizes.  For this we will use [the VIVO Sample Data Generator](http://github.com/mconlon17/vivo-sample-data-generator.git) which can generate realistic VIVO triples at scale.
* Test write performance by adding triple collections of various sizes
* Test read performance by running collections of SPARQL queries
* Test load performance by loading triple collections of various sizes through VIVO's firsttime mechanism.
* Compare test result timing for TDB, SDB, and potentially other VIVO triple stores.
