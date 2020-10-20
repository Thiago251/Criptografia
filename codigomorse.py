def crypto(frase):
    tradutor = ''
    for letra in frase:
      if letra in "A": tradutor = tradutor + "·-"
      elif letra in 'B': tradutor = tradutor + '-···'
      elif letra in 'C': tradutor = tradutor + '-·-·'
      elif letra in 'D': tradutor = tradutor + '-··'
      elif letra in 'E': tradutor = tradutor + '·'
      elif letra in 'F': tradutor = tradutor + '··-·'
      elif letra in 'G': tradutor = tradutor + '--·'
      elif letra in 'H': tradutor = tradutor + '····'
      elif letra in 'I': tradutor = tradutor + '··'
      elif letra in 'J': tradutor = tradutor + '·---'
      elif letra in 'L': tradutor = tradutor + '·-··'
      elif letra in 'M': tradutor = tradutor + '--'
      elif letra in 'M': tradutor = tradutor + '-·'
      elif letra in 'O': tradutor = tradutor + '---'
      elif letra in 'P': tradutor = tradutor + '·--·'
      elif letra in 'Q': tradutor = tradutor + '--·-'
      elif letra in 'R': tradutor = tradutor + '·-·'
      elif letra in 'S': tradutor = tradutor + '···'
      elif letra in 'T': tradutor = tradutor + '-'
      elif letra in 'U': tradutor = tradutor + '··-'
      elif letra in 'V': tradutor = tradutor + '···-'
      elif letra in 'X': tradutor = tradutor + '-··-'
      elif letra in 'Z': tradutor = tradutor + '--··'
      elif letra in 'W': tradutor = tradutor + '·--'
      elif letra in 'Y': tradutor = tradutor + '-·--'
      elif letra in 'K': tradutor = tradutor + '-·-'

      else: tradutor = tradutor + letra
    return tradutor
while True:
      print(crypto(input("Digite a frase desejada: ")))