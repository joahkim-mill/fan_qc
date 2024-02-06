# Delta (Exhaust) Fan In-House Quality Control Metric

This plots sweep measurements recorded on Room EQ Wizard(REW) to understand differences between good and bad fan quality. The aim is to be able to visualize certain peak frequencies consistent only in bad fans to root them out before being installed in units.

This is available to run on [Streamlit - Fan QC](https://deltafanqc.streamlit.app/) without the code or can be run locally via [fan_qc.py](fan_qc.py). Additionally, the effect of running a good and two bad fans in a 90 degC oven for roughly a week was analyzed to see how the performance compared. This can be seen on [Streamlit - Oven Comparison](https://compareovenfans.streamlit.app/) or locally run through [compare_oven_effect.py](compare_oven_effect.py).
