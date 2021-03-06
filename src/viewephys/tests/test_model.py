from viewephys.raster import ProbeData
import numpy as np
import pandas as pd
from brainbox.tests.test_metrics import multiple_spike_trains
from neuropixel import trace_header


def test_model_dataclass():
    # TODO: make a meta-data file fixture to create the bin file for the test
    # this test won't run on a machine without the bin file below
    st, sa, sc = multiple_spike_trains()
    spikes = dict(times=st, clusters=sc, amps=sa)
    clusters = dict(channels=np.random.randint(0, 384, np.max(sc)))
    channels = trace_header(version=1)

    ProbeData(spikes=spikes, clusters=clusters, channels=channels, ap_file='toto.bin')
    ProbeData(spikes=pd.DataFrame(spikes), clusters=pd.DataFrame(clusters), channels=pd.DataFrame(channels), ap_file='toto.bin')
