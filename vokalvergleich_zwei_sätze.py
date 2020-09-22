# Titel: Vokalvergleich zwei Sätze
# Beschreibung: Der Benutzer kann zwei Sätze eingeben. Das Programm zählt dann die Vokale in jedem Satz und gibt Vergleichswerte aus.
# Autor: Michael Migsch
# Email: N.A.
# Version: 1.0.0

print("Gib 'exit' ein um das Programm zu beenden.\n")

while True:

  # Benutzereingaben holen.

  satz_1 = str(input('Gib deinen ersten Satz ein: '))
  if satz_1.lower() == 'exit':
      quit()
  satz_2 = str(input('Gib deinen zweiten Satz ein: '))
  if satz_2.lower() == 'exit':
      quit()

  # Datenstrukturen für die Vokalzählung in den beiden Sätzen erzeugen.

  vokale = ['a', 'e', 'i', 'o', 'u']
  vokale_satz_1 = {v:0 for v in vokale}
  vokale_satz_2 = {v:0 for v in vokale}


  # Vokale in den Sätzen zählen und den entsprechenden Variablen zuweisen.

  for v in vokale:
      vokale_satz_1[v] = satz_1.count(v)
      vokale_satz_2[v] = satz_2.count(v)


  # Prozentanteil der Vokale in den Sätzen berechnen.

  anzahl_vokale_satz_1 = 0
  anzahl_vokale_satz_2 = 0

  for wert in vokale_satz_1.values():
      anzahl_vokale_satz_1 += wert

  for wert in vokale_satz_2.values():
      anzahl_vokale_satz_2 += wert

  anzahl_zeichen_satz_1 = len(satz_1)
  anzahl_zeichen_satz_2 = len(satz_2)

  prozentanteil_vokale_satz_1 = round(100 / anzahl_zeichen_satz_1 * anzahl_vokale_satz_1, 2)
  prozentanteil_vokale_satz_2 = round(100 / anzahl_zeichen_satz_2 * anzahl_vokale_satz_2, 2)


  # Ausgaben für den Benutzer.

  print(f'Der Prozentanteil der Vokale im ersten Satz ist: {prozentanteil_vokale_satz_1}%')
  print(f'Der Prozentanteil der Vokale im zweiten Satz ist: {prozentanteil_vokale_satz_2}%')

  print(f'Der erste Satz hat insgesamt {anzahl_vokale_satz_1} Vokale.')
  print(f'Der zweite Satz hat insgesamt {anzahl_vokale_satz_2} Vokale.')

  if anzahl_vokale_satz_1 > anzahl_vokale_satz_2:
      print('Der erste Satz hat mehr Vokale als der zweite Satz.')
  elif anzahl_vokale_satz_2 > anzahl_vokale_satz_1:
      print('Der zweite Satz hat mehr Vokale als der erste Satz.')
  elif anzahl_vokale_satz_1 == anzahl_vokale_satz_2:
      print('Beide Sätze haben die gleiche Anzahl an Vokalen.')
  else:
      print('Ein unbekannter Fehler ist aufgetreten, bitte kontaktieren Sie den Entwickler.')
