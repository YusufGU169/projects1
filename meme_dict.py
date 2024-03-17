meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap. Açılışı 'Laugh Out Loud' yani 'Yüksek sesle gülmek' demektir.",
            "BRUH": "Kanka, dostum.",
            "ROFL" : "Açılışı 'Rolling On the Floor Laughing' yani 'Yerde yuvarlanarak gülüyorum' demektir. Aşırı kahkaha veya eğlenceyi ifade eder.",
            "SMH" : "Açılışı 'Shaking My Head' yani 'Başımı sallıyorum' demektir. Onaylamamayı, hayal kırıklığını veya inanmamayı ifade eder.",
            "OMG" : "Açılışı 'Oh My God' yani 'Aman Tanrım' demektir. Şaşkınlığı, heyecanı veya inanmamayı ifade eder."
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
print(" ")

if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print("Anlamı:", meme_dict[word])
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("Anlamı bulunamadı.")
