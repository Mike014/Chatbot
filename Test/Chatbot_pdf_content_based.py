import speech_recognition as sr
from PyPDF2 import PdfReader
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import py_compile

def load_pdf(file_path):
    """
    Load and extract text from a PDF file.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF.
    """
    with open(file_path, 'rb') as f:
        reader = PdfReader(f)
        raw = ''
        for i in range(len(reader.pages)):
            raw += reader.pages[i].extract_text()
    return raw

def preprocess_text(raw_text):
    """
    Preprocess the extracted text by tokenizing, removing stopwords, stemming, and lemmatizing.

    Args:
        raw_text (str): The raw text extracted from the PDF.

    Returns:
        nltk.Text: The preprocessed text.
    """
    stopwords_set = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    tokens = nltk.word_tokenize(raw_text)
    tokens = [token for token in tokens if token not in stopwords_set]
    tokens = [stemmer.stem(token) for token in tokens]
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return nltk.Text(tokens)

def recognize_speech():
    """
    Recognize speech from the microphone and return the recognized text.

    Returns:
        str: The recognized text from the speech.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        question = r.recognize_google(audio)
        print("You said: " + question)
        return question
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def main():
    file_path = 'D:\\Roba da autodidatta\\Musica\\Teoria e Armonia Musicale\\Hollywood Chord Progressions.pdf'
    raw_text = load_pdf(file_path)
    processed_text = preprocess_text(raw_text)

    while True:
        question = recognize_speech()
        if question and question.lower() == "stop":
            break

if __name__ == "__main__":
    main()

# Tests
def test_load_pdf():
    with patch("builtins.open", mock_open(read_data="This is a test PDF content.")) as mock_file:
        with patch("PyPDF2.PdfReader") as MockPdfReader:
            mock_reader_instance = MockPdfReader.return_value
            mock_reader_instance.pages = [mock_reader_instance]
            mock_reader_instance.pages[0].extract_text.return_value = "This is a test PDF content."
            result = load_pdf("dummy_path")
            assert result == "This is a test PDF content."

def test_preprocess_text():
    raw_text = "This is a test PDF content."
    result = preprocess_text(raw_text)
    assert isinstance(result, nltk.Text)
    assert "test" in result

@patch("speech_recognition.Recognizer.listen")
@patch("speech_recognition.Recognizer.recognize_google")
@patch("speech_recognition.Microphone")
def test_recognize_speech(mock_microphone, mock_recognize_google, mock_listen):
    mock_recognize_google.return_value = "test speech"
    result = recognize_speech()
    assert result == "test speech"

if __name__ == "__main__":
    pytest.main()
