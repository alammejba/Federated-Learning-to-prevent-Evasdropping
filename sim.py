from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import speech_recognition as sr

# Create a recognizer object
r = sr.Recognizer()
model = SentenceTransformer('bert-base-nli-mean-tokens')

# Use the default microphone as the audio source
with sr.Microphone() as source:
    # Adjust for ambient noise
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    while True:
        # Listen for audio and convert it to text
        audio = r.listen(source)
        sentences_on = ['Turn the lights on']
        sentences_off = ['Turn the lights off']
        try:
            text = r.recognize_google(audio)
            print("You said:", text)
            sentences_on.append(text)
            sentences_off.append(text)
            sentence_embeddings_on = model.encode(sentences_on)
            sentence_embeddings_off = model.encode(sentences_off)
            prob_on = cosine_similarity(
                [sentence_embeddings_on[0]],
                sentence_embeddings_on[1:]
            )
            prob_off = cosine_similarity(
                [sentence_embeddings_off[0]],
                sentence_embeddings_off[1:]
            )
            # print(prob_on,' - ',prob_off)

            # prob_exit = cosine_similarity(
            #         ["Shut down"],
            #         sentence_embeddings_off[1:]
            #     )
            # if(prob_exit>prob_off):
            #     break

            if(prob_off>0.5 and prob_on>0.5):
                if(prob_on>prob_off):
                    print("Turning Lights ON")
                else:
                    print("Turning Lights OFF")
            else:
                print("I am unable to perform that")
                
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

print('Shutting Down . . .')


