input = "Салем"

values = (
("А", "A"),
("Ә", "Á"),
("Б", "B"),
("В", "V"),
("Г", "G"),
("Ғ", "Ǵ"),
("Д", "D"),
("Е", "E"),
("Ё", ""  ),
("Ж", "J"),
("З", "Z"),
("И", "I"),
("Й", "I"),
("К", "K"),
("Қ", "Q"),
("Л", "L"),
("М", "M"),
("Н", "N"),
("Ң", "Ń"),
("О", "O"),
("Ө", "Ó"),
("П", "P"),
("Р", "R"),
("С", "S"),
("Т", "T"),
("У", "Ý"),
("Ұ", "U"),
("Ү", "Ú"),
("Ф", "F"),
("Х", "H"),
("Һ", "H"),
("Ц", ""  ),
("Ч", "Ch"),
("Ш", "Sh"),
("Щ", ""  ),
("Ъ", ""  ),
("І", "I"),
("Ь",  "" ),
("Ю", ""  ),
("Я", ""  ),
)

output = ""
for item in input:
    for a in values:
        if(item.upper() == a[0]):
           output += a[1]
print(output)