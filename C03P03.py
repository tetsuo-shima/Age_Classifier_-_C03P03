# Age Classifier
# Write a program that asks the user to enter a person’s age. The program should
# display a message indicating whether the person is an infant, a child, a
# teenager, or an adult.
# Following are the guidelines:
# • If the person is 1 year old or less, he or she is an infant.
# • If the person is older than 1 year, but younger than 13 years, he or she is
#   a child.
# • If the person is at least 13 years old, but less than 20 years old, he or
#   she is a teenager.
# • If the person is at least 20 years old, he or she is an adult.


import minimum_age


def main():
    age = float(input("Enter age: "))

    try:
        validate_age(age)
    except ValueError as e:
        print(e)
        exit(1)

    print("Classification:", get_classification(age).title())


def validate_age(age):
    if age < 0:
        raise ValueError('Age must be greater than 0, got {}'.format(age))


def get_classification(age):
    if age >= minimum_age.ADULT:
        classification = "adult"
    elif age >= minimum_age.TEENAGER:
        classification = "teenager"
    elif age >= minimum_age.CHILD:
        classification = "child"
    else:
        classification = "infant"

    return classification





main()
