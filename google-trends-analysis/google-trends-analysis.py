from pytrends.request import TrendReq # importing for making trend analysis
import plotly.express as px # importing for plotting it with Plotly

yourtrends = TrendReq(hl='en-US', tz=360) # here is the initialization process for the trend

keywords_list = ["covid", 'health', 'travel', 'water', 'food'] # here is a list of keywords to get data from

yourtrends.build_payload(keywords_list, cat=0, timeframe='today 12-m') # work with keywords in the timeframe

# here shows interest for keywords in trend over time in a histogram form
data = yourtrends.interest_over_time()
data = data.reset_index()

fig = px.histogram(data, x="date", y=keywords_list, title='Web search interest for certain keywords over time')
fig.show()
