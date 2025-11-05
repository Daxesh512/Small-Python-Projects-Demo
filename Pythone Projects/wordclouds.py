from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open('wordcloud.txt', 'r') as f:
    text = f.read()

words = WordCloud().generate(text)
plt.imshow(words, interpolation='bilinear')
plt.axis("off")
plt.show()