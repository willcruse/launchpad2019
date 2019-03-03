# Imports
import speech_recognition as sr
import sounddevice as sd # Not PortAudio as there was incompatibilities
import numpy as np
import scipy.io.wavfile
import time
import ffmpy # Only one that worked multi platform
import json
import os
import os.path


class SpeechRecognition():
    """ Class used to record and parse a user's mic input """
    def __init__(self, duration, frequency):
        """ Instantiation of variables """
        self.duration = duration # in seconds
        self.frequency = frequency # 48KHz, standard frequency
        self.recordFile = "Speech.wav"
        self.parseFile = "Speech.flac" # File used for the recognition
        self.deleteAudioFiles()

    def setDuration(self, duration):
        """ Sets the duration """
        self.duration = duration

    def setFrequency(self, frequency):
        """ Sets the frequency """
        self.frequency = frequency

    def deleteAudioFiles(self):
        """ Deletes both the audio files if they exist """
        if os.path.isfile(self.recordFile):
            os.remove(self.recordFile)
        if os.path.isfile(self.parseFile):
            os.remove(self.parseFile)

    def takeMicInput(self):
        """ Takes the user's mic input, stores it in a numpy array, then is converted into a wav file"""
        recording = sd.rec(int(self.duration * self.frequency), samplerate=self.frequency, channels=2)
        sd.wait() # Makes sure the mic has finished taking the input before doing anything
        scipy.io.wavfile.write(self.recordFile, self.frequency, recording) # Saves file

    def convertAudioFile(self):
        """ Converts the wav file into a flac file for parsing"""
        ff = ffmpy.FFmpeg(inputs={self.recordFile: None},outputs={self.parseFile: None})
        ff.run()

    def recogniseVoice(self):
        """ Runs the recognition algorithm (google in this example),
            returning the JSON file containing the words the user said"""
        recog = sr.Recognizer()
        audioFile = sr.AudioFile(self.parseFile)
        with audioFile as source: # Takes the audio file as a source
            audio = recog.record(source)
        try:
            spokenWords = recog.recognize_google(audio).lower()
            # Hands the audio to the API for parsing, returning a string of words
        except:
            spokenWords = "." # If no words picked up
        dict = {'message':spokenWords}
        jsonFile = json.dumps(dict) # Dumps the text file into a JSON
        self.deleteAudioFiles()
        return jsonFile
