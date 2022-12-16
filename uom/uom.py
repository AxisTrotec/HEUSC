class uom:
    def __init__(self):
        print("Indeed")

    # Deeper analyzing of the string
    def uom_analyze(string):
        From = string.split()[2]
        To = string.split()[3]
        Number = string.split()[1]

        lengths = ["centimeter", "cm", "meter", "m", "kilometer", "km", "millimeter",
                   "mm", "foot", "feet", "ft", "inches", "in", "mile", "mi", "yard", "yd"]
        masses = ["milligram", "gram", "kilogram", "ounce", "pound", "ton"]
        volumes = ["milliletre", "litre", "kilolitre",
                   "cubic_cm", "fluid_ounce", "gallon", "pint"]
        temperatures = ["celcius", "kelvin", "fahrenheit"]

        if any(x in To for x in lengths):
            uom.length(From, To, Number)
        elif any(x in To for x in masses):
            uom.mass(From, To, Number)
        elif any(x in To for x in volumes):
            uom.volume(From, To, Number)
        elif any(x in To for x in temperatures):
            uom.temperature(From, To, Number)

    def length(From, To, Number):
        output = ""

        length_dictionary = [{0: {"cm": "10", "m": "1000", "km": "1000000",
                                  "in": "25.4", "ft": "304.8", "yd": "914.4", "mi": "1609000"}},
                             {1: {"mm": "10", "m": "100", "km": "100000",
                                  "in": "2.54", "ft": "30.48", "yd": "91.44", "mi": "160900"}},
                             {2: {"mm": "1000", "cm": "100", "km": "1000",
                                  "in": " 39.37", "ft": " 3.281", "yd": "1.094", "mi": "1609"}},
                             {3: {"mm": "1000000", "cm": "100000", "m": "1000",
                                  "in": "39370", "ft": "3281", "yd": "1094", "mi": "1.609"}},
                             {4: {"mm": "25.4", "cm": "2.54", "m": "39.37",
                                  "km": "39370", "ft": "12", "yd": "36", "mi": "63360"}},
                             {5: {"mm": "304.8", "cm": "30,48", "m": "3.281",
                                  "km": "3281", "in": "12", "yd": "3", "mi": "5280"}},
                             {6: {"mm": "914.4", "cm": "91.44", "m": "1.094",
                                  "km": "1094", "in": "36", "ft": "3", "mi": "1760"}},
                             {7: {"mm": " 1609000", "cm": "160900", "m": "1609", "km": "1.609", "in": "63360", "ft": "5280", "yd": "1760"}}]

        match To:
            case "millimeter" | "mm":
                length_dictionary[0]
            case "centimeter" | "cm":
                print(length_dictionary[1:To])
            case "meter" | "m":
                length_dictionary[2]
            case "kilometer" | "km":
                length_dictionary[From[To]]
            case "inches" | "inch" | "in":
                length_dictionary[From[To]]
            case "feet" | "foot" | "ft":
                length_dictionary[From[To]]
            case "yard" | "yd":
                length_dictionary[From[To]]
            case "mile" | "mi":
                length_dictionary[From[To]]

        return output

    def mass(From, To, Number):
        # Metric Units
        def milligram():
            return

        def gram():
            return

        def kilogram():
            return

        # Imperial Unit
        def ounce():
            return

        def pound():
            return

        def ton():
            return

        return

    def volume(From, To, Number):
        # Metric Unit
        def milliletre():
            return

        def litre():
            return

        def kilolitre():
            return

        def cubic_cm():
            return

        # Imprial Unit
        def fluid_ounce():
            return

        def gallon():
            return

        def pint():
            return

        return

    def temperature(From, To, Number):
        def celcius():
            return

        def kelvin():
            return

        def fahrenheit():
            return

        return

    def time():
        return

    def chart():
        return
