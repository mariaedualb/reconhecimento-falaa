print("Testando!")

import speech_recognition as sr 
 
import os

#função para ouvir e reconhecer a fala
def ouvir_microfone():
    #habilita o microfone do usuário
    microfone = sr.Recognizer() 

    #usando o microfone
    with sr.Microphone() as source:

        #chama algoritmo para redução de ruídos
        microfone.adjust_for_ambient_noise(source)

        #a deixa para o usuário falar 
        print("Diga alguma coisa:")

        #armazena o que tá sendo dito numa variável
        audio = microfone.listen(source)

    try:
        
        #passa a variável para o algoritmo reconhecedor de padrões
        frase = microfone.recognize_google(audio, language="pt-BR") 

        if "criar documento" in frase:
            os.system("start Word.exe")
        
        elif "criar planilha" in frase:
            os.system("start Excel.exe")

        #retorna a frase pronunciada
        print("Você disse: " + frase)

    #se nao reconhecer o padrão de fala, exibe a mensagem
    except sr.UnknownValueError:
        print("Desculpe, não entendi.")

        return frase

ouvir_microfone()print("Testando!")

import speech_recognition as sr 
 
import os

#função para ouvir e reconhecer a fala
def ouvir_microfone():
    #habilita o microfone do usuário
    microfone = sr.Recognizer() 

    #usando o microfone
    with sr.Microphone() as source:

        #chama algoritmo para redução de ruídos
        microfone.adjust_for_ambient_noise(source)

        #a deixa para o usuário falar 
        print("Diga alguma coisa:")

        #armazena o que tá sendo dito numa variável
        audio = microfone.listen(source)

    try:
        
        #passa a variável para o algoritmo reconhecedor de padrões
        frase = microfone.recognize_google(audio, language="pt-BR") 

        if "criar documento" in frase:
            os.system("start Word.exe")
        
        elif "criar planilha" in frase:
            os.system("start Excel.exe")

        #retorna a frase pronunciada
        print("Você disse: " + frase)

    #se nao reconhecer o padrão de fala, exibe a mensagem
    except sr.UnknownValueError:
        print("Desculpe, não entendi.")

        return frase

ouvir_microfone()