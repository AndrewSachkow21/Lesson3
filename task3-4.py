alphabet=["Ь","Ю","Я","а","б","в","г","ґ","д","е","э","ж","з","и","і","ї","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ь","ю","я","А","Б","В"]
def Cheasar_code(text,mode):
    done_text=""
    value = 0
    if mode == 1:
        value = 3
    elif value == 0:
        value = -3
    for simvol in text:
        for i in range(len(alphabet)):
            if simvol == alphabet[i]:
                done_text += alphabet[i+value]
    return done_text
print(Cheasar_code(input("text"),int(input("mode(1 or 0):"))))
