# STT Stock Data Service
The stt (Stock Trading Tools) stock data service is dedicated to downloading and retrieving stock data.

This program involves a REST API interface for accessing stock data. It is intended
to rely on a separate service for getting the indicators, since it can be done via
a GPU or high end CPU, and that might necessitate a different language to be done
quickly.

Consult the docs/interface.md for how to interface with it.
