#andrew
def ticket(a, b):
    ticket_diapozon=[]
    ticket_diapozon.append(a)
    for i in range(b - a):
        ticket_diapozon.append(i + a + 1)
    return ticket_diapozon
print(ticket(5, 9))
