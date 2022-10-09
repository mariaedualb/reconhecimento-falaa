print("Testando!")

import speech_recognition as sr 
 
import os

#funcao para ouvir e reconhecer a fala
def ouvir_microfone():
    #habilita o microfone do usuario
    microfone = sr.Recognizer() 

    #usando o microfone
    with sr.Microphone() as source:

        #chama algoritmo para reducao de ruidos
        microfone.adjust_for_ambient_noise(source)

        #a deixa para o usuario falar 
        print("Diga alguma coisa:")

        #armazena o que ta sendo dito numa variavel
        audio = microfone.listen(source)

    try:
        
        #passa a variavel para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio, language="pt-BR") 
        
        #essa parte nao ta rodando
        if "criar documento" in frase:
            os.system("start Word.exe")
        
        elif "criar planilha" in frase:
            os.system("start Excel.exe")

        #retorna a frase pronunciada
        print("Você disse: " + frase)

    #se nao reconhecer o padrao de fala exibe a mensagem
    except sr.UnknownValueError:
        print("Desculpe, não entendi.")

        return frase

ouvir_microfone()
