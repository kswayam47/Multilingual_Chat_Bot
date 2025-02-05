from setuptools import find_packages, setup

setup(
    name="multilingual assistant",
    version="0.0.0",
    author="Swayam",
    author_email="Swayam Kewlani",
    packages=find_packages(),
    install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]
)