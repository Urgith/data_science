# libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# list of words (data)
text = ('Python Python Python Matplotlib')

# create WordCloud object
wordcloud = WordCloud(width=400, height=480, margin=0).generate(text)

# show generated image
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.margins(x=0, y=0)
plt.show()
