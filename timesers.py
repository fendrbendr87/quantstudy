from bokeh.plotting import figure, output_file, show
import pandas

df=pandas.read_csv("GOOG.csv", parse_dates=["Date"])

p=figure(width=500, height=500, x_axis_type="datetime")

p.line(df["Date"],df["Close"],color="Orange",alpha=0.5)

output_file("Timeseries.html")

show(p)

