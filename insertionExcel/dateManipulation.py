import datetime as dt


def adjustFormatDate(date):
    result = dt.datetime.strptime(date, '%Y-%m-%d')

    return result.strftime('%d/%m/%Y')
