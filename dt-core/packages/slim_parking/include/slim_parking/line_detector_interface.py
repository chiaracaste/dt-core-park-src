from abc import ABCMeta, abstractmethod
import numpy as np

__all__ = [
    'LineDetectorInterface',
]


class LineDetectorInterface(object):

    __metaclass__ = ABCMeta

    # These are not used yet

    LOST = 'lost'
    GOOD = 'good'
    STRUGGLING = 'struggling'

    POSSIBLE_STATUSES = [LOST, GOOD, STRUGGLING]

    ESTIMATE_DATATYPE = np.dtype([('phi', 'float64'),
                                  ('d', 'float64')])

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def predict(self, dt, v, w):
        pass

   # @abstractmethod
    #def parking_detected(self):
     #   """ Returns true or false """

    @abstractmethod
    def update(self, segment_list):
        """
            segment list: a list of Segment objects
        """

    @abstractmethod
    def getStatus(self):
        """ Returns one of the statuses above """

    @abstractmethod
    def getEstimate(self):
        """ Returns a numpy array of datatype ESTIMATE_DATATYPE """
