from wordcloud import WordCloud


# Testo da usare per la word cloud

testo = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"

# Genera la word cloud
wordcloud = WordCloud(width=800, height=400, background_color='purple').generate(testo)


# Salva l'immagine
wordcloud.to_file("wordcloud.png")
