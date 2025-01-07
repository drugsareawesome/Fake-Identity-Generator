import random
import hashlib
from faker import Faker
from datetime import date, timedelta

fake = Faker()
Faker.seed(0)

def generate_random_character():
    # Basic Identity Info
    gender = random.choice(["Male", "Female"])
    first_name = fake.first_name_male() if gender == "Male" else fake.first_name_female()
    middle_name = fake.first_name()
    last_name = fake.last_name()
    initials = f"{first_name[0]}. {middle_name[0]}. {last_name[0]}."
    mothers_maiden_name = fake.last_name()
    
    # Birthday and Zodiac Sign
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=80)
    zodiac_signs = ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"]
    zodiac_dates = [
        (120, 218), (219, 320), (321, 419), (420, 520), (521, 620),
        (621, 722), (723, 822), (823, 922), (923, 1022), (1023, 1121),
        (1122, 1221), (1222, 119)
    ]
    birth_ordinal = int(birth_date.strftime("%m%d"))
    zodiacal_sign = next(z for (z, (start, end)) in zip(zodiac_signs, zodiac_dates) if start <= birth_ordinal <= end or (start > end and (birth_ordinal >= start or birth_ordinal <= end)))
    
    # Login Details
    username = f"{first_name[0].lower()}.{last_name[0].lower()}.{random.randint(100, 999)}"
    password = fake.password(length=10, special_chars=False)
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    sha1_hash = hashlib.sha1(password.encode()).hexdigest()
    
    # Contact Info
    email = fake.email()
    phone = fake.phone_number()
    address = fake.address().replace("\n", ", ")
    
    # Financial Info
    credit_card = fake.credit_card_number()
    ssn = fake.ssn()
    passport_no = f"{random.randint(100000000, 999999999)}"
    passport_issue_date = fake.date_between(start_date="-10y", end_date="-5y")
    passport_expiry_date = passport_issue_date + timedelta(days=3652)
    driver_license_no = f"D{random.randint(1000000, 9999999)}"
    driver_license_issue_date = fake.date_between(start_date="-2y", end_date="today")
    driver_license_expiry_date = driver_license_issue_date + timedelta(days=4 * 365)
    
    # Physical Appearance
    hair_colors = ["Black", "Brown", "Blonde", "Red", "Gray"]
    eye_colors = ["Brown", "Blue", "Green", "Hazel", "Gray"]
    height = random.randint(150, 200)  # cm
    weight = random.randint(50, 100)  # kg
    blood_types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    
    # Personality and Fantasy Features
    religion = random.choice(["Unaffiliated", "Christian", "Muslim", "Jewish", "Buddhist", "Hindu"])
    political_side = random.choice(["Democrat", "Republican", "Independent"])
    favorite_color = random.choice(["Red", "Blue", "Green", "Yellow", "Pink", "Purple"])
    favorite_food = random.choice(["Pizza", "Macaroni and Cheese", "Sushi", "Burgers", "Salad"])
    favorite_season = random.choice(["Winter", "Spring", "Summer", "Fall"])

    alignment = random.choice(["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "True Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"])
    abilities = {"Charisma": random.randint(1, 20), "Constitution": random.randint(1, 20), "Dexterity": random.randint(1, 20), "Intelligence": random.randint(1, 20), "Strength": random.randint(1, 20), "Wisdom": random.randint(1, 20)}

    # Print character information
    print(f"Gender\t{gender}")
    print(f"First name\t{first_name}")
    print(f"Middle name\t{middle_name}")
    print(f"Last name\t{last_name}")
    print(f"Initials\t{initials}")
    print(f"Mother's Maiden name\t{mothers_maiden_name}")
    print(f"Birthday\t{birth_date.strftime('%B, %d %Y')} (Age: {date.today().year - birth_date.year} years)")
    print(f"Zodiacal sign\t{zodiacal_sign}")
    print(f"User name\t{username}")
    print(f"Password\t{password}")
    print(f"Password hash (MD5)\t{md5_hash}")
    print(f"Password hash (SHA1)\t{sha1_hash}")
    print(f"E-Mail\t{email}")
    print(f"Phone\t{phone}")
    print(f"Address\t{address}")
    print(f"Credit Card\t{credit_card}")
    print(f"SSN\t{ssn}")
    print(f"Passport\tNo.: {passport_no}\nissued: {passport_issue_date.strftime('%B/%d/%Y')}\nexpires: {passport_expiry_date.strftime('%B/%d/%Y')}")
    print(f"Driver License\t{driver_license_no} - issued on {driver_license_issue_date.strftime('%m/%d/%Y')}, expires {driver_license_expiry_date.strftime('%m/%d/%Y')}")
    print(f"Hair color\t{random.choice(hair_colors)}")
    print(f"Eyes color\t{random.choice(eye_colors)}")
    print(f"Height\t{height} cm / {round(height / 2.54, 1)} in")
    print(f"Weight\t{weight} Kg / {round(weight * 2.20462, 1)} pounds")
    print(f"Blood Type\t{random.choice(blood_types)}")
    print(f"Religion\t{religion}")
    print(f"Political side\t{political_side}")
    print(f"Favorite Color\t{favorite_color}")
    print(f"Favorite Comfort Food\t{favorite_food}")
    print(f"Favorite Season\t{favorite_season}")
    print(f"Alignment\t{alignment}")
    for ability, value in abilities.items():
        print(f"{ability}: {value}")

# Generate a character
generate_random_character()
