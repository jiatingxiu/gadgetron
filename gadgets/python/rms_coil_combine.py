import numpy as np
from gadgetron import Gadget

class RMSCoilCombine(Gadget):

    def process_config(self, cfg):
        print "RMS Coil Combine, Config ignored"

    def process(self, h, im):
        combined_image = np.sqrt(np.sum(np.square(np.abs(im)),axis=0))
        h.channels = 1
        return self._gadget_reference.return_image(h,combined_image.astype('complex64'))
