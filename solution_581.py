from collections import OrderedDict
color_orderdict = OrderedDict([('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')]) 
print("Original OrderedDict:")
print(color_orderdict)
print("Insert an element at the beginning of the said OrderedDict:")
color_orderdict.update({'color4':'Orange'})
color_orderdict.move_to_end('color4', last = False)
print("\nUpdated OrderedDict:")
print(color_orderdict)
