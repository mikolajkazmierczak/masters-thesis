import spacy
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def create_wordcloud_from_file(text):
    # Load the Polish language model
    nlp = spacy.load("pl_core_news_sm")

    # Process the text with SpaCy
    doc = nlp(text)

    # Extract lemmatized tokens, filtering out punctuation and spaces
    words = [token.lemma_ for token in doc if not token.is_punct and not token.is_space]

    # Join words to create a single string for the WordCloud
    words_string = " ".join(words)

    # Generate the word cloud
    wordcloud = WordCloud(
        width=800,
        height=800,
        background_color="white",
        stopwords=set(nlp.Defaults.stop_words),
        min_font_size=10,
    ).generate(words_string)

    # Display the word cloud using matplotlib
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()
    plt.savefig("wordcloud.png")


TEXT = """
## PAR

Grafika 1 (widok produktu)
1. sklep internetowy
2. PAR Bakuła, torba, przycisk dodaj do koszyka, przycisk plusa, można dodać kilka produktów, koszyk w prawym górnym rogu
3. napis PAR Bakuła

Grafika 2 (narzędzie start)
1. edycja slajdów
2. po lewej kilka plansz, literki AB, tekst na środku, zielone guziki
3. slajdy po lewej

Grafika 3 (narzędzie koniec)
1. edycja slajdów
2. torba z logo politechniki, zielone guziki, dużo czerwonego
3. torba z logo politechniki

## MidOcean

Grafika 1 (widok produktu)
1. sklep internetowy
2. logo w lewym górnym rogu z czerwonym akcentem, koszyk w prawym górnym rogu, po lewej stronie od produktu były inne zdjęcia
3. produkt

Grafika 2 (narzędzie start)
1. dostosowanie produktu
2. produkt, torba, czerwony znak z ostrzeżeniem, coś poszło źle, na torbie była żółta ramka, nad zdjęciem produktu napis zaawansowany konfigurator
3. ramka z ostrzeżeniem

Grafika 3 (narzędzie koniec)
1. narzędzie
2. zaawansowane narzędzie, logo, po prawej zielony przycisk, coś do wyboru
3. logo politechniki

## Drukomat

Grafika 1 (widok produktu)
1. coś do drukowania
2. nazwa drukomat, na środku cennik gdzie rosły ceny, napis "standardowy"
3. cennik

Grafika 2 (narzędzie start)
1. konfigurator, tworzenie projektu
2. produkt, dwa niebieskie przyciski jeden od zapisz, w prawym górnym rogu niebieski przycisk, ikonka warstw
3. produkt

Grafika 3 (narzędzie koniec)
1. to samo
2. zapisz projekt, logo pwr, żółta przerywana ramka produktu
3. logo pwr

"""


# Example usage:
create_wordcloud_from_file(TEXT)
