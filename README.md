# psi-metric2cluster

In cases, where CrUX data isn't available, like in cases we measure performance on stage, Screaming Frog gives us only numeric LightHouse metrics without clustering into poor, needs improvement, good. 
Here is a Python script for Google Colab to cluster LightHouse metrics.
After export of performance data from Screaming Frog upload export CSV to the script, that's all. The script calculates clusters and downloads _clustered.csv. Calculated clusters are on the right table end.
Your CSV should contain these headings (setup in Screaming Frog PageSpeed Insights API settings or just delete other, if not needed):
 - Address
 - Time to First Byte (ms)
 - First Contentful Paint Time (ms)
 - Speed Index Time (ms)
 - Largest Contentful Paint Time (ms)
 - Time to Interactive (ms)
 - Max Potential First Input Delay (ms)
 - Total Blocking Time (ms)
 - Cumulative Layout Shift
