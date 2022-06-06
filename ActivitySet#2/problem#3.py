

def get_cs():
   x =input('enter the string')
   return x 
def cs_to_lot(cs,lst):
    a=cs.split(';')
    for word in a :
      lst.append()
    return lst 


def main():
    cs = get_cs()
    lot = list()
    lot = cs_to_lot(cs,lot)
    print(lot)

process=input('what process r u doing? \n')
if process == 'strsplit':
    main()
