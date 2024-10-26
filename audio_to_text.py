import azure.cognitiveservices.speech as speechsdk

def transcribe_audio(audio_file_path):
    # Set up the subscription info and service region
    subscription_key = "2tSVB58NTiGrDQtHsSNKqaPyre7BD2u3IR5kU8wKFtkOhPuIZyz4JQQJ99AJACGhslBXJ3w3AAAYACOGMT0o"  # Replace with your Azure subscription key
    region = "centralindia"  # Replace with your Azure region

    # Create a speech configuration
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)

    # Create an audio configuration from the audio file
    audio_config = speechsdk.audio.AudioConfig(filename=audio_file_path)

    # Create a speech recognizer
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    # Start the transcription process
    print("Transcribing audio...")
    result = speech_recognizer.recognize_once()  # You can use recognize_continuous() for longer audio

    # Check the result
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Transcription: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))

if __name__ == "__main__":
    audio_file_path = input("Enter the path to the audio file (e.g., audio.wav): ")
    transcribe_audio(audio_file_path)
