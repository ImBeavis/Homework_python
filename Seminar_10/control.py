import model


def result_massage(data):
    num = int(data)
    massage = analis(num)
    return massage


def analis(number):
    if 40 > number > 0:
        if number <= model.balance:
            mas = model.calculator(number)
            return mas
        else:
            return "Столько конфет нет"
    else:
        return "Столько брать нельзя"