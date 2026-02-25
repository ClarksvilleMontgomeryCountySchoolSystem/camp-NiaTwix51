def main():
    #Collect Input for each
    #Variable: first Prompt: Child's First Name:
    first = 'Alice'
    #Variable: last Prompt: Child's Last Name:
    last = 'Johnson'
    print(f"Camper's Name: {first} {last}")

    #Variable: birth Prompt: In what year was {first} {last} born:
    birth = '2012'
    print(f"Birth Year: {birth}")

    #Variable: days Prompt: How many days will {first} attend?
    days = '5'
    print(f"Camp Duration: {days} days")

    #Variable: p_first Prompt: Parent's First Name:
    p_first = 'Robert'
    #Variable: p_last Prompt: Parent's Last Name:
    p_last = 'Johnson'
    print(f"Parent's Name: {p_first} {p_last}")

    #Variable: phone Prompt: Parent's Phone #:
    phone = '615-555-1234'
    print(f"Phone Number: {phone}")

    #Variable: street Prompt: Street Address:
    street = '123 Main Street'
    #Variable: city Prompt: City:
    city = 'Clarksville'
    #Variable: state Prompt: State Abbreviation:
    state = 'TN'
    #Variable: zip Prompt: Zip Code:
    print(f"Address:\n{street}\n{city}, {state} {zip}")

if __name__ == "__main__":
    main()

