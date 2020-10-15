def crypto(frase):
    tradutor = ''
    for letra in frase:
      if letra in "Aa": tradutor = tradutor + "0"
      elif letra in 'Bb': tradutor = tradutor + '3'
      elif letra in 'Cc': tradutor = tradutor + '21'
      elif letra in 'Dd': tradutor = tradutor + '144'
      elif letra in 'Ee': tradutor = tradutor + '987'
      elif letra in 'Ff': tradutor = tradutor + '6765'
      elif letra in 'Gg': tradutor = tradutor + '46368'
      elif letra in 'Hh': tradutor = tradutor + '317811'
      elif letra in 'Ii': tradutor = tradutor + '2778309'
      elif letra in 'Jj': tradutor = tradutor + '14930352'
      elif letra in 'Ll': tradutor = tradutor + '102334155'
      elif letra in 'Mm': tradutor = tradutor + '701408733'
      elif letra in 'Mn': tradutor = tradutor + '4807526976'
      elif letra in 'Oo': tradutor = tradutor + '32951280099'
      elif letra in 'Pp': tradutor = tradutor + '225851433717'
      elif letra in 'Qq': tradutor = tradutor + '1548008755920'
      elif letra in 'Rr': tradutor = tradutor + '1'
      elif letra in 'Ss': tradutor = tradutor + '5'
      elif letra in 'Tt': tradutor = tradutor + '34'
      elif letra in 'Uu': tradutor = tradutor + '233'
      elif letra in 'Vv': tradutor = tradutor + '1597'
      elif letra in 'Xx': tradutor = tradutor + '10946'
      elif letra in 'Zz': tradutor = tradutor + '75025'
      elif letra in 'Ww': tradutor = tradutor + '514229'
      elif letra in 'Yy': tradutor = tradutor + '3524578'
      elif letra in 'Kk': tradutor = tradutor + '24157817'

      else: tradutor = tradutor + letra
    return tradutor
while True:
      print(crypto(input("Digite a frase desejada: ")))
