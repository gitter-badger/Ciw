from __future__ import division

class DataRecord:
    """
    A class for a data record
    """
    def __init__(self, arrival_date, service_time, service_start_date, exit_date, node, destination, customer_class, queue_size_at_arrival, queue_size_at_departure):
        """
        An example of a data record instance.
        """
        if exit_date < arrival_date:
            raise ValueError('Arrival date should preceed exit date')

        if service_time < 0:
            raise ValueError('Service time should be positive')

        self.arrival_date = arrival_date
        self.service_time = service_time
        self.service_start_date = service_start_date
        self.exit_date = exit_date
        self.customer_class = customer_class
        self.queue_size_at_arrival = queue_size_at_arrival
        self.queue_size_at_departure = queue_size_at_departure

        self.service_end_date = service_start_date + service_time
        self.wait = service_start_date - arrival_date
        self.blocked = exit_date - self.service_end_date
        self.node = node
        self.destination = destination
