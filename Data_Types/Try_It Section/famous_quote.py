# 2.5 - 2.6
famous_quote = ' "A person who never made a mistake never tried anything new." '
famous_person = "Albert Einstein"
famous_quote = famous_quote.strip()
print(f"{famous_person} once said, {famous_quote}")

# 2.7
name = "  \tDave Jackson\n  "
print(name)

name = name.lstrip()
# name = name.rstrip()
# name = name.strip()
print(name)