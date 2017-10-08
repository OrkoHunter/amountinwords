# Today's date 8th October, 2017

def numinwordsIntrn(no):
    unit = [
        'ONE',
        'TWO',
        'THREE',
        'FOUR',
        'FIVE',
        'SIX',
        'SEVEN',
        'EIGHT',
        'NINE',
        'TEN',
        'ELEVEN',
        'TWELVE',
        'THIRTEEN',
        'FOURTEEN',
        'FIFTEEN',
        'SIXTEEN',
        'SEVENTEEN',
        'EIGHTEEN',
        'NINETEEN',
        'TWENTY']
    tens = [
        'TEN',
        'TWENTY',
        'THIRTY',
        'FORTY',
        'FIFTY',
        'SIXTY',
        'SEVENTY',
        'EIGHTY',
        'NINETY']
    supers = ['HUNDRED', 'THOUSAND', 'MILLION', 'BILLION']
    no = int(no)
    strno = repr(no)
    digits = len(strno)
    segmented = []
    if digits <= 3:
        segmented.append(strno[-3:])
    elif digits <= 6 and digits > 3:
        segmented.append(strno[-3:])
        segmented.append(strno[-6:-3])
    elif digits <= 9 and digits > 6:
        segmented.append(strno[-3:])
        segmented.append(strno[-6:-3])
        segmented.append(strno[-9:-6])
    elif digits <= 12 and digits > 9:
        segmented.append(strno[-3:])
        segmented.append(strno[-6:-3])
        segmented.append(strno[-9:-6])
        segmented.append(strno[-12:-9])
    #-----------------------------------------------Function to convert digits

    def converter(number):
        number = int(number)
        number = repr(number)
        if len(number) == 3:
            digits = list(number)
            if int(digits[1]) == 0 and int(digits[2]) == 0:
                return unit[int(digits[0]) - 1] + " " + supers[0]
            string = unit[int(digits[0]) - 1]
            string += " " + supers[0] + " "
            if int(digits[1]) > 1:
                string += tens[int(digits[1]) - 1] + " "
                string += unit[int(digits[2]) - 1]
            elif int(digits[1]) == 1:
                string += unit[int(digits[2]) + 9]
            else:
                string += unit[int(digits[2]) - 1]
            return string
        if len(number) == 2:
            digits = list(number)
            if int(digits[1]) == 0:
                return tens[int(digits[0]) - 1]
            if int(digits[0]) > 1:
                string = tens[int(digits[0]) - 1] + " "
                string += unit[int(digits[1]) - 1]
            else:
                string = unit[int(digits[1]) + 9]
            return string
        if len(number) == 1:
            string = unit[int(number) - 1]
            return string

    segmented.reverse()
    if len(segmented) == 1:
        number0 = int(segmented[0])
        if number0 != 0:
            return converter(segmented[0]) + " ONLY"
    elif len(segmented) == 2:
        number0 = int(segmented[1][0])
        number1 = int(segmented[1][1])
        number2 = int(segmented[1][2])

        if number0 == 0 and number1 == 0 and number2 == 0:
            return converter(segmented[0]) + " " + supers[1] + " ONLY"
        else:
            return converter(
                segmented[0]) + " " + supers[1] + " " + converter(segmented[1]) + " ONLY"

    elif len(segmented) == 3:
        sec1 = int(segmented[0])
        sec2 = int(segmented[1])
        sec3 = int(segmented[2])
        if sec1 != 0 and sec2 == 0 and sec3 == 0:
            return converter(segmented[0]) + " " + supers[2] + " ONLY"
        elif sec1 != 0 and sec2 == 0 and sec3 != 0:
            return converter(
                segmented[0]) + " " + supers[2] + " " + converter(segmented[2]) + " ONLY"
        elif sec1 != 0 and sec2 != 0 and sec3 == 0:
            return converter(segmented[0]) + " " + supers[2] + \
                " " + converter(segmented[1]) + " " + supers[1] + " ONLY"
        else:
            return converter(segmented[0]) + " " + supers[2] + " " + converter(segmented[1]) + \
                " " + supers[1] + " " + converter(segmented[2]) + " ONLY"

    elif len(segmented) == 4:
        sec1 = int(segmented[0])
        sec2 = int(segmented[1])
        sec3 = int(segmented[2])
        sec4 = int(segmented[3])
        if sec1 != 0 and sec2 != 0 and sec3 != 0 and sec4 == 0:
            return converter(segmented[0]) + " " + supers[3] + " " + converter(segmented[1]) + \
                " " + supers[2] + " " + converter(segmented[2]) + " " + supers[1] + " ONLY"
        elif sec1 != 0 and sec2 != 0 and sec3 == 0 and sec4 != 0:
            return converter(segmented[0]) + " " + supers[3] + " " + converter(segmented[1]) + \
                " " + supers[2] + " " + converter(segmented[3]) + " ONLY"
        elif sec1 != 0 and sec2 == 0 and sec3 != 0 and sec4 != 0:
            return converter(segmented[0]) + " " + supers[3] + " " + converter(segmented[2]) + \
                " " + supers[1] + " " + converter(segmented[3]) + " ONLY"
        elif sec1 != 0 and sec2 != 0 and sec3 == 0 and sec4 == 0:
            return converter(segmented[0]) + " " + supers[3] + \
                " " + converter(segmented[1]) + " " + supers[2] + " ONLY"
        elif sec1 != 0 and sec2 == 0 and sec3 == 0 and sec4 != 0:
            return converter(
                segmented[0]) + " " + supers[3] + " " + converter(segmented[3]) + " ONLY"
        elif sec1 != 0 and sec2 == 0 and sec3 != 0 and sec4 == 0:
            return converter(segmented[0]) + " " + supers[3] + \
                " " + converter(segmented[2]) + " " + supers[1] + " ONLY"
        elif sec1 != 0 and sec2 == 0 and sec3 == 0 and sec4 == 0:
            return converter(segmented[0]) + " " + supers[3] + " ONLY"
        else:
            return converter(segmented[0]) + " " + supers[3] + " " + converter(segmented[1]) + " " + supers[2] + \
                " " + converter(segmented[2]) + " " + supers[1] + " " + converter(segmented[3]) + " ONLY"

